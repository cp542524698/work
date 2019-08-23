### 用户属性
 - 用户属性修改，比如：修改密码、用户名、指定host等 【/api/v1/attribute/{region}/{instanceId}/{username} POST】
 ```shell
 //post data: 比如修改密码
 {
    "user": {"password": "XXXX"}
} 
 //post data: 比如修改用户名
 {
    "user": {"name": "userC"} 
 } 
 //post data: 比如修改host
 {
    "user": {"host": "192.168.3.8"} 
 } 
 ```
 ```shell
 //resp
 {"code":0,"data":null,"message":"success"}
 ```
