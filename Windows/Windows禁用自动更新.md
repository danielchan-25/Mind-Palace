# Windows禁用自动更新

## 禁用 Windows Update 服务

1. 按下 `Win + R` ，输入 `services.msc` 
2. 找到 `Windows Update` 这一项，并双击打开
3. 双击打开它，点击 「停止」，把启动类型选为 「禁用」，最后点击应用

## 在组策略里关闭自动更新相关服务

1. 按下 `Win + R` ，输入 `gpedit.msc`

2. 在组策略编辑器中，依次展开：

   **计算机配置 -> 管理模板 -> Windows组件 -> Windows更新**

3. 然后在右侧 "配置自动更新" 设置中，将其设置为「已禁用」 ，并点击下方的「应用」

4. 之后还需要再找到 "删除使用所有Windows更新功能的访问权限"，选择 「已启用」

## 禁用任务计划里边的自动更新

1. 按下 `Win + R` ，输入 `taskschd.msc`

2. 在任务计划程序的设置界面，依次展开

   **任务计划程序库 -> Microsoft -> Windows -> WindowsUpdate**

   把里面的项目都设置为 「禁用」 

## 在注册表中关闭自动更新

1. 按下 `Win + R` ，输入 `regedit`

2. 在注册表设置中，找到并定位到

   **[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\UsoSvc]**

   在右侧找到 "Start" 键

   点击修改，把 "start" 值改成 16 进制，值改为 "4"

3. 继续在右侧找到 `FailureActions` 键，右键点击修改该键的二进制数据，将 “0010”、“0018” 行的左起第 5 个数值由原来的 “01”改为“00”



---



> 参考文档：https://baijiahao.baidu.com/s?id=1732432888882246429&wfr=spider&for=pc&qq-pf-to=pcqq.temporaryc2c