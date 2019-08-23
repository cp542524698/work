db相关：
  - 列出database 【 uri: /api/v1/dbbase/{region}/{instanceId}  GET 】
  ```shell
  //resp:
  {
    "code": 0,
    "data": [
        {
            "CharSet": "",
            "Collate": "",
            "Name": "data"
        },
        {
            "CharSet": "",
            "Collate": "",
            "Name": "DemoA1"
        },
        {
            "CharSet": "",
            "Collate": "",
            "Name": "DemoA2"
        },
        {
            "CharSet": "",
            "Collate": "",
            "Name": "myDB"
        },
        {
            "CharSet": "",
            "Collate": "",
            "Name": "myDB2"
        }
    ],
    "message": "success"
}
  ```
  - 创建database 【 uri: /api/v1/dbbase/{region}/{instanceId}  POST 】
  ```shell
  //post data
  {
"databases":[                 
    {"name": "DemoA1",         
         "charset": "gdk",        
          "collate": "utf8_general_ci"
    },
    {"name": "DemoA2",         
         "charset": "utf8",       
          "collate": "utf8_general_ci"
     } 
  ]
}
  ```
  ```shell
  //resp
  {"code":0,"data":null,"message":"success"}
  ```
  
  - 删除database 【 uri: /api/v1/dbbase/{region}/{instanceId}/{dbName}  DELETE 】
  ```shell
  //resp
  {"code":0,"data":null,"message":"success"}
  ```
