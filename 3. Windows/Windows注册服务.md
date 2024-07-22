# SC 命令
语法
```powershell
命令:
  query-----------查询服务的状态，
                  或枚举服务类型的状态。
  queryex---------查询服务的扩展状态，
                  或枚举服务类型的状态。
  start-----------启动服务。
  pause-----------发送 PAUSE 控制请求到服务。
  interrogate-----发送 INTERROGATE 控制请求到服务。
  continue--------发送 CONTINUE 控制请求到服务。
  stop------------发送 STOP 请求到服务。
  config----------(永久地)更改服务的配置。
  description-----更改服务的描述。
  failure---------更改服务失败时所进行的操作。
  qc--------------查询服务的配置信息。
  qdescription----查询服务的描述。
  qfailure--------查询失败服务所进行的操作。
  delete----------(从注册表)删除服务。
  create----------创建服务(将其添加到注册表)。
  control---------发送控制到服务。
  sdshow----------显示服务的安全描述符。
  sdset-----------设置服务的安全描述符。
  GetDisplayName--获取服务的 DisplayName。
  GetKeyName------获取服务的 ServiceKeyName。
  EnumDepend------枚举服务的依存关系。

下列命令不查询服务名称:
sc <server> <command> <option>
  boot------------(ok | bad) 表明是否将上一次启动保存为
                  最后所知的好的启动配置
  Lock------------锁定服务数据库
  QueryLock-------查询 SCManager 数据库的 LockStatus
```

## 创建服务
```powershell
sc create test_services binpath= "C:\test" type= own start= auto
```

## 查询服务
```powershell
sc query redis
```
