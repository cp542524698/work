### 用户相关
  - 列举db 用户 【uri: /api/v1/account/{region}/{instanceId} GET】
```shell
//resp 
{
    "code": 0,
    "data": [
        {
            "dbs": [],
            "host": "%",
            "user": "newuser"
        },
        {
            "dbs": [],
            "host": "127.0.0.1",
            "user": "userGF"
        }
    ],
    "message": "success"
}
```
  - 创建 db 用户 【uri: /api/v1/account/{region}/{instanceId} POST】
```shell
//post data
{
  "name": "userGF",
  "password": "password2",
  "host": "127.0.0.1"
}
```
```shell
//resp
{"code":0,"data":null,"message":"success"}
```

 - 删除 db 用户 【uri: /api/v1/account/{region}/{instanceId}/{username} DELETE】
```shell
//resp
{"code":0,"data":null,"message":"success"}
```
