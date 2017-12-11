## ceph结合iscsi ##

### iscsi Target 安装 ###

1、安装SCST

- tar -jxf scst-3.0.1.tar.bz2
- cd scst-3.0.1
- make && make install

2、安装iscsi-scst

- tar -jxf iscsi-scst-3.0.1.tar.bz2
- cd iscsi-scst-3.0.1
- make && make install

3、安装scstadmin

- tar -jxf scstadmin-3.0.1.tar.bz2
- cd scstadmin-3.0.1
- make && make install

4、载入内核

- modprobe scst
- modprobe scst_vdisk
- modprobe iscsi-scst 

5、启动进程

- /etc/init.d/scst start
- /usr/local/sbin/iscsi-scstd

### 配置Target ###

1、创建target：

- scstadmin -add\_target {TARGET_NAME}  -driver iscsi

2、激活target：

- enable系统scst： echo 1 > /sys/kernel/scst_tgt/targets/iscsi/enabled

3、激活target：

- scstadmin -enable\_target {TARGET_NAME}  -driver iscsi

4、创建ceph rbd并映射到系统：

- rbd create  --size 10240 rbd/{RBD_NAME}

5、映射到系统：

- rbd map rbd/{rbd_name}

6、分配Lun（logic unit number）

- 创建lun： scstadmin -open\_dev {自定义DEV_NAME} -handler vdisk\_blockio -attributes filename=/dev/rbd/rbd/{RBD_NAME}

7、将lun加入target端【lun 号，这个号必须在这个机器唯一】：

- scstadmin -add\_lun 0 -driver iscsi -target {TARGET_NAME} -device {'6'中定义的DEV_NAME}

8、写入配置文件

- scstadmin -write\_config /etc/scst.conf

9、启停服务命令

- service scst start/stop/restart/status


### 在Initiator端测试Target配置 ### [open-iscsi initiator-utils提供的管理命令为iscsiadm]

1、查找target：

- iscsiadm -m discovery -t st -p {TARGET_IP}

2、连接target：

- iscsiadm -m node -T {TARGET\_NAME} -p {TARGET\_IP}:{PORT,default:3260} -l

3、登出target：

- iscsiadm -m node -T {TARGET\_NAME} -p {TARGET\_IP}:{PORT,default:3260} -u

4、查看已连接的target

- iscsiadm -m session

5、lsscsi命令查看target端的lun映射的块设备

- lsscsi

6、断开所有targets的连接

- iscsiadm -m node --logoutall=all

### iscsi 认证###
1、使用iscsiadm命令对登录某个target的CHAP认证参数进行修改

- iscsiadm -m node -T {TARGET\_NAME} -p {TARGET\_IP}:{PORT,default:3260} -o update --name=node.session.auth.authmethod --value=CHAP
- iscsiadm -m node -T {TARGET\_NAME} -P {TARGET\_IP}:{PORT, default:3260} -o update --name=node.session.auth.username --value={USERNAME}
- iscsiadm -m node -T {TARGET\_NAME} -P {TARGET\_IP}:{PORT, default:3260} -o update --name=node.session.auth.password --value={PASSWORD}  	#强制至少12个字符


### 多路径配置 ###

1、编辑/etc/multipath.conf

	# This is a template multipath-tools configuration file
	# Uncomment the lines relevent to your environment
	
	defaults {
		udev_dir /dev
		polling_interval 10
		selector "round-robin 0"
		path_grouping_policy multibus
		getuid_callout "/lib/udev/scsi_id --whitelisted --device=/dev/%n"
		prio const
		path_checker directio
		rr_min_io 100
		flush_on_last_del no
		max_fds 8192
		rr_weight priorities
		failback immediate
		no_path_retry fail
		queue_without_daemon no
		user_friendly_names no
		mode 644
		uid 0
		gid disk
	}

	blacklist {
		wwid 26353900f02796769
		devnode "^(ram|raw|loop|fd|md|dm-|sr|scd|st)[0-9]*"
		devnode "^hd[a-z][[0-9]*]"
		device {
			vendor DEC.*
			product MSA[15]00
		}
	}

	blacklist_exceptions {
		devnode "^dasd[c-d]+[0-9]*"
		wwid "IBM.75000000092461.4d00.34"
	}

2、启动multipath-tool 进程

- 安装multipath: yum install -y device-mapper-multipath.x86_64 
- 启动multipath-tools: systemctl start multipathd
- 查看多路径：multipath -ll

### Q&A ###

1、scst target开机无法自启动问题：

- 修改/etc/scst.conf文件：
	
		TARGET_DRIVER iscsi {
			enabled 0
		}

- 更改scstadmin-3.0.1的Makefile文件

		echo $$chr update-rc.d "$(1)" defaults;
		改为:
		$$chr update-rc.d "$(1)" defaults;
