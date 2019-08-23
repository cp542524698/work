### 数据库配置

  - 获取所有配置项 【 /api/v1/cfg/{region}/{instanceID}/1 GET】 
  ```shell
  //resp data
  {
    "code": 0,
    "data": {
        "basedir": "/usr",
        "connect_timeout": "15",
        "datadir": "/var/lib/mysql/data",
        "default_storage_engine": "innodb",
        "innodb_buffer_pool_size": "1200M",
        "innodb_data_file_path": "ibdata1:10M:autoextend",
        "innodb_file_per_table": "1",
        "innodb_log_buffer_size": "25M",
        "innodb_log_file_size": "50M",
        "innodb_log_files_in_group": "2",
        "join_buffer_size": "1M",
        "key_buffer_size": "400M",
        "local-infile": "0",
        "max_allowed_packet": "8192K",
        "max_connections": "1000",
        "max_heap_table_size": "128M",
        "max_user_connections": "800",
        "myisam-recover-options": "BACKUP,FORCE",
        "open_files_limit": "4096",
        "performance_schema": "ON",
        "pid-file": "/var/run/mysqld/mysqld.pid",
        "port": "3306",
        "query_cache_limit": "1M",
        "query_cache_size": "64M",
        "query_cache_type": "1",
        "read_buffer_size": "512K",
        "read_rnd_buffer_size": "512K",
        "server_id": "240870679",
        "skip-external-locking": "1",
        "socket": "/var/run/mysqld/mysqld.sock",
        "sort_buffer_size": "1M",
        "table_definition_cache": "2048",
        "table_open_cache": "2048",
        "thread_cache_size": "32",
        "thread_stack": "192K",
        "tmp_table_size": "128M",
        "tmpdir": "/var/tmp",
        "user": "mysql",
        "wait_timeout": "120"
    },
    "message": "success"
}
  ```
 - 获取用户自定义的配置项 【 /api/v1/cfg/{region}/{instanceID}/0 GET】  
  ```shell
  //resp 
  {
    "code": 0,
    "data": {
        "max_connections": "1000",
        "wait_timeout": "120"
    },
    "message": "success"
}
  ```
  - 用户自定义配置项 【 /api/v1/cfg/{region}/{instanceID} POST】
  ```shell
  //post data
  {
    "configurations": {
            "wait_timeout": 120,
            "max_connections": 1000
        }
}
  ```
  ```shell
  //resp
  {"code":0,"data":null,"message":"success"}
  ```
  
