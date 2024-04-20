# Kubernetes
# 1.简介

## 1.1 什么是Kubernetes

Kubernetes （通常称为K8s，K8s是将8个字母 “ubernete” 替换为 “8” 的缩写）

是用于**自动部署、扩展和管理容器化（containerized）应用程序的开源系统**。

它旨在提供“跨主机集群的自动部署、扩展以及运行应用程序容器的平台”。它支持一系列容器工具, 包括Docker等。

CNCF于2017年宣布首批Kubernetes认证服务提供商（KCSPs），包含IBM、MIRANTIS、华为、inwinSTACK迎栈科技等服务商。

## 1.2 发展史

Kubernetes (希腊语"舵手" 或 "飞行员") 由Joe Beda，Brendan Burns和Craig McLuckie创立，并由其他谷歌工程师，包括Brian Grant和Tim Hockin进行加盟创作，并由谷歌在2014年首次对外宣布 。它的开发和设计都深受谷歌的Borg系统的影响，它的许多顶级贡献者之前也是Borg系统的开发者。在谷歌内部，Kubernetes的原始代号曾经是Seven，即星际迷航中友好的Borg(博格人)角色。Kubernetes标识中舵轮有七个轮辐就是对该项目代号的致意。

Kubernetes v1.0于2015年7月21日发布。随着v1.0版本发布，谷歌与Linux 基金会合作组建了Cloud Native Computing Foundation (CNCF)并把Kubernetes作为种子技术来提供。

Rancher Labs在其Rancher容器管理平台中包含了Kubernetes的发布版。Kubernetes也在很多其他公司的产品中被使用，比如Red Hat在OpenShift产品中，CoreOS的Tectonic产品中， 以及IBM的IBM云私有产品中。

## 1.3 特点

- 可移植: 支持公有云，私有云，混合云，多重云（multi-cloud）
- 可扩展: 模块化, 插件化, 可挂载, 可组合
- 自动化: 自动部署，自动重启，自动复制，自动伸缩/扩展
- 快速部署应用，快速扩展应用
- 无缝对接新的应用功能
- 节省资源，优化硬件资源的使用

## 1.4 规划组件

Kubernetes定义了一组构建块，它们可以共同提供部署、维护和扩展应用程序的机制。组成Kubernetes的组件设计为松耦合和可扩展的，这样可以满足多种不同的工作负载。可扩展性在很大程度上由**Kubernetes API**提供——它被作为扩展的内部组件以及Kubernetes上运行的容器等使用。

**Pod**

Kubernetes的基本调度单元称为“pod”。它可以把更高级别的抽象内容增加到容器化组件。一个pod一般包含一个或多个容器，这样可以保证它们一直位于主机上，并且可以共享资源。Kubernetes中的每个pod都被分配一个唯一的（在集群内的）IP地址这样就可以允许应用程序使用端口，而不会有冲突的风险。

Pod可以定义一个卷，例如本地磁盘目录或网络磁盘，并将其暴露在pod中的一个容器之中。pod可以通过Kubernetes API手动管理，也可以委托给控制器来管理。

**标签和选择器**

Kubernetes使客户端（用户或内部组件）将称为“标签”的键值对附加到系统中的任何API对象，如pod和节点。相应地，“标签选择器”是针对匹配对象的标签的查询。

标签和选择器是Kubernetes中的主要分组机制，用于确定操作适用的组件。

例如，如果应用程序的Pods具有系统的标签 tier ("front-end", "back-end", for example) 和一个 release_track ("canary", "production", for example)，那么对所有"back-end" 和 "canary" 节点的操作可以使用如下所示的标签选择器：

 tier=back-end AND release_track=canary 

**控制器**

控制器是将实际集群状态转移到所需集群状态的对帐循环。它通过管理一组**pod**来实现。一种控制器是一个“复制控制器”，它通过在集群中运行指定数量的pod副本来处理复制和缩放。如果基础节点出现故障，它还可以处理创建替换pod。

其它控制器，是核心Kubernetes系统的一部分包括一个“DaemonSet控制器”为每一台机器（或机器的一些子集）上运行的恰好一个pod，和一个“作业控制器”用于运行pod运行到完成，例如作为批处理作业的一部分。控制器管理的一组pod由作为控制器定义的一部分的标签选择器确定。

**服务**

Kubernetes服务是一组协同工作的pod，就像多层架构应用中的一层。构成服务的pod组通过标签选择器来定义。

Kubernetes通过给服务分配静态IP地址和域名来提供服务发现机制，并且以轮询调度的方式将流量负载均衡到能与选择器匹配的pod的IP地址的网络连接上（即使是故障导致pod从一台机器移动到另一台机器）。默认情况下，一个服务会暴露在集群中（例如，多个后端pod可能被分组成一个服务，前端pod的请求在它们之间负载平衡）；但是，一个服务也可以暴露在集群外部（例如，从客户端访问前端pod）。

1.5 核心组件

Kubernetes遵循*master-slave architecture*。Kubernetes的组件可以分为管理单个的 node 组件和控制平面的一部分的组件。

Kubernetes Master是集群的主要控制单元，用于管理其工作负载并指导整个系统的通信。Kubernetes控制平面由各自的进程组成，每个组件都可以在单个主节点上运行，也可以在支持*high-availability clusters*的多个主节点上运行。

Kubernetes主要由以下几个核心组件组成：

| **组件名称**           | **说明**                                                     |
| ---------------------- | ------------------------------------------------------------ |
| **etcd**               | 保存了整个集群的状态；                                       |
| **apiserver**          | 提供了资源操作的唯一入口，并提供认证、授权、访问控制、API注册和发现等机制； |
| **controller manager** | 负责维护集群的状态，比如故障检测、自动扩展、滚动更新等；     |
| **scheduler**          | 负责资源的调度，按照预定的调度策略将Pod调度到相应的机器上；  |
| **kubelet**            | 负责维护容器的生命周期，同时也负责Volume（CVI）和网络（CNI）的管理； |
| **Container runtime**  | 负责镜像管理以及Pod和容器的真正运行（CRI）；                 |
| **kube-proxy**         | 负责为Service提供cluster内部的服务发现和负载均衡；           |

2.部署 Kubernetes 集群

2.1 主机环境说明

关闭防火墙



参考文档

> https://www.cnblogs.com/gaoyuechen/p/8685771.html