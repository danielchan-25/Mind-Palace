# 背景
家里的网络支持IPV6，但24小时变动一次，每次都需要获取地址好麻烦，所以使用 CloudFlare 进行域名解析，一劳永逸。

# 流程

CloudFlare 开通 DNS 服务 -> 使用 Python 获取 IPV6 地址 -> 通过 CloudFlare API 同步到 CloudFlare 上

# 开始

准备：
1. 域名
2. CloudFlare 账号
3. CloudFlare API

首先需要手动在 CloudFlare 域名解析里面，添加一次记录：
DNS记录->添加类型（AAAA、IPV6地址）

以后就运行以下程序自动更新

```python
# -*- coding: utf-8 -*-
import json
import socket
import requests

dns_name = ''  # DNS记录名称
zone_id = ''  # 区域ID
token = ''  # API地址

def get_record_id(dns_name, zone_id, token):
    ''' 获取CloudFlare上的 dns_id'''
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    resp = requests.get(url, headers=headers)

    if not json.loads(resp.text)['success']:
        return None
    domains = json.loads(resp.text)['result']
    for i in domains:
        if dns_name == i['name']:
            return i['id']
    return None

def update_dns_record(dns_name, zone_id, token, dns_id, ip, proxied=False):
    ''' 更新DNS记录 '''
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_id}'
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    payload = {'type': 'AAAA', 'name': dns_name, 'content': ip, 'proxied': proxied}
    resp = requests.put(url, headers=headers, json=payload)

    if not json.loads(resp.text)['success']:
        return None
    return True

if __name__ == '__main__':
    dns_id = get_record_id(dns_name, zone_id, token)
    if update_dns_record(dns_name, zone_id, token, dns_id, ip) is False:
        print('更新失败')
```
