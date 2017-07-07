（1.2.4）.243.227.224 5522
页面设计图：
     ![image](gitlab.ztgame.com.cn/chengpeng/gaint_zabbix/blob/master/pic/login.png)
                    图1
    【图1】说明：
        1、点击“监控按钮”，检测后端该instance是否安装监控：
                a、没有安装监控，
                        检测是否设置zabbix server：
                                1、未设置：跳转到监控设置页面
                                2、已设置：调用后端api直接安装；
                                        安装结果返回：
                                            a、success：弹框提示“安装成功”，并进入该instance的监控项页面
                                            b、fail：对提示信息进行分类 【待讨论】
                b、已安装监控：
                        直接跳转到监控项页面

     ![image](http://gitlab.ztgame.com.cn/chengpeng/gaint_zabbix/blob/master/pic/monitor_default.png)
                图2
    【图2】说明：
        1、进入监控页面，判断是否该项目是否进行过监控server端设置：
                a、未设置，显示【图2】
                        1、点击：“创建自己的zabbix-server”，调用api创建云主机[注意参数传递、server端必须同网段]
                        2、返回：zabbix-server的相关信息；
                        3、点击：“统一zabbix-server”， 调用api进行相关配置[报警邮箱等等...]
                        4、返回：success：成功， fail： 失败及原因
                b、已设置：
                        1、设置的是“自己的zabbix server”，显示【图3】
                        2、设置的是“统一的zabbix server”， 显示【图4】
    
     ![image](http://gitlab.ztgame.com.cn/chengpeng/gaint_zabbix/blob/master/pic/myzabbix.png)
                    图3
     ![image](http://gitlab.ztgame.com.cn/chengpeng/gaint_zabbix/blob/master/pic/allzabbix.png)
                    图4
