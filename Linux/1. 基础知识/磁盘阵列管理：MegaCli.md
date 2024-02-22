> 下载地址：
> http://www.lsi.com/downloads/Public/RAID%20Controllers/RAID%20Controllers%20Common%20Files/8.07.14_MegaCLI.zip
> http://www.lsi.com/support/downloads/megaraid/miscellaneous/linux/Linux_MegaCLI_1.01.24.zip

# 常用命令
```bash
./MegaCli -LDInfo -Lall -aALL		# 查raid级别
./MegaCli -AdpAllInfo -aALL			# 查raid卡信息
./MegaCli -PDList -aALL				# 查看硬盘信息
./MegaCli -AdpBbuCmd -aAll			# 查看电池信息
./MegaCli -FwTermLog -Dsply -aALL	# 查看raid卡日志
./MegaCli -adpCount					# 【显示适配器个数】
./MegaCli -AdpGetTime –aALL			#【显示适配器时间】
./MegaCli -AdpAllInfo -aAll			#【显示所有适配器信息】
./MegaCli -LDInfo -LALL -aAll		#【显示所有逻辑磁盘组信息】
./MegaCli -PDList -aAll				#【显示所有的物理信息】
./MegaCli -AdpBbuCmd -GetBbuStatus -aALL |grep 'Charger Status'		#【查看充电状态】
./MegaCli -AdpBbuCmd -GetBbuStatus -aALL			# 【显示BBU状态信息】
./MegaCli -AdpBbuCmd -GetBbuCapacityInfo -aALL		#【显示BBU容量信息】
./MegaCli -AdpBbuCmd -GetBbuDesignInfo -aALL		#【显示BBU设计参数】
./MegaCli -AdpBbuCmd -GetBbuProperties -aALL		#【显示当前BBU属性】
./MegaCli -cfgdsply -aALL		#【显示Raid卡型号，Raid设置，Disk相关信息】
```

## 查看硬盘信息
```bash
./MegaCli64 LDPDInfo -Aall
Span: 1 - Number of PDs: 2
PD: 0 Information
Enclosure Device ID: 32
Slot Number: 4
Drive's position: DiskGroup: 1, Span: 1, Arm: 0
Enclosure position: N/A
Device Id: 4
WWN: 5000C500035EF550
Sequence Number: 2
Media Error Count: 90
Other Error Count: 0
Predictive Failure Count: 0
Last Predictive Failure Event Seq Number: 0
PD Type: SAS
Raw Size: 372.528 GB [0x2e90edd0 Sectors]
Non Coerced Size: 372.028 GB [0x2e80edd0 Sectors]
Coerced Size: 372.0 GB [0x2e800000 Sectors]
Sector Size:  0
Firmware state: Online, Spun Up
Device Firmware Level: NS25
Shield Counter: 0
Successful diagnostics completion on :  N/A
SAS Address(0): 0x5000c500035ef551
SAS Address(1): 0x0
Connected Port Number: 1(path0) 
Inquiry Data: SEAGATE ST3400755SS     NS253RJ0NJFA
FDE Capable: Not Capable
FDE Enable: Disable
Secured: Unsecured
Locked: Unlocked
Needs EKM Attention: No
Foreign State: None 
Device Speed: 3.0Gb/s 
Link Speed: 3.0Gb/s 
Media Type: Hard Disk Device
Drive Temperature :28C (82.40 F)
PI Eligibility:  No 
Drive is formatted for PI information:  No
PI: No PI
Port-0 :
Port status: Active
Port's Linkspeed: 3.0Gb/s 
Port-1 :
Port status: Active
Port's Linkspeed: Unknown 
Drive has flagged a S.M.A.R.T alert : No
```

需要关注的信息：

- Slot Number: 4 ：插槽编号：4

- Media Error Count: 90：媒体错误计数：90

- Inquiry Data: SEAGATE ST3400755SS NS253RJ0NJFA：查询数据：SEAGATE ST3400755SS NS253RJ0NJFA

	- SEAGATE：希捷

	- ST3400755SS：磁盘型号（可以通过该型号去京东购买磁盘）

## 查看RAID级别
```bash
./MegaCli64 -LDInfo -Lall -aALL
Virtual Drive: 1 (Target Id: 1)
Name                :
RAID Level          : Primary-1, Secondary-0, RAID Level Qualifier-0
Size                : 744.0 GB
Sector Size         : 512
Mirror Data         : 744.0 GB
State               : Optimal
Strip Size          : 64 KB
Number Of Drives per span:2
Span Depth          : 2
Default Cache Policy: WriteBack, ReadAdaptive, Direct, No Write Cache if Bad BBU
Current Cache Policy: WriteBack, ReadAdaptive, Direct, No Write Cache if Bad BBU
Default Access Policy: Read/Write
Current Access Policy: Read/Write
Disk Cache Policy   : Disk's Default
Encryption Type     : None
Bad Blocks Exist: No
Is VD Cached: Yes
Cache Cade Type : Read Only
```
主要查看以下信息：

`RAIDLevel : Primary-0, Secondary-0, RAID Level Qualifier-0`

raid级别：

- 0 0 0：RAID-0

- 1 0 0：RAID-1

- 5 0 3：RAID-5

- 1 3 0：RAID-10

RAID-1 还需要结合 `Span Depth` 的值来判断：

`Span Depth : 2`：表示共 2 个 RAID1 盘组做成了 RAID10，1 则表示 1 个 RAID1 盘组。

## 使硬盘灯闪烁

如服务器上没有标签，难以找到硬盘时，可以使用该命令使硬盘灯闪烁。

```bash
# 闪烁
./MegaCli64 -PdLocate -start -physdrv [32:0] -aALL
# 停止闪烁
./MegaCli64 -PdLocate -stop -physdrv [32:4] -aALL
```

32：`Enclosure Device ID`，可以通过：`./MegaCli64 LDPDInfo -Aall|grep Enclosure` 命令查看

0：`Slot Number`：硬盘槽位

## 查看硬盘损坏情况

可以使用以下命令查看，主要关注这几个数字即可，数字越大越危险！

```bash
./MegaCli64 LDPDInfo -Aall|grep Media
Media Error Count: 0
Media Type: Hard Disk Device
Media Error Count: 0
Media Type: Hard Disk Device
Media Error Count: 0
Media Type: Hard Disk Device
Media Error Count: 90
Media Type: Hard Disk Device
Media Error Count: 0
Media Type: Hard Disk Device
```

## 卸载硬盘
```bash
./MegaCli64 -PDOffline -PhysDrv[32:4] -a0

# 查看硬盘状态
```

## 查看rebuild进度
```bash
./MegaCli64 -PDRbld -ShowProg -PhysDrv[32:4] -aAll
```
