#!/usr/bin/env python
# coding=utf-8
# Contributor:
# Phus Lu <phus.lu@gmail.com>
# Wang Wei Qiang <wwqgtxx@gmail.com>

__uploaddir__ = 'python' # Which Dir You Need To Upload
__proxy__= '' # Your Proxy Server Address
__need_cookies__= False # If You Want Don't Remove .appcfg_cookies,Please Set "__need_cookies__= True"


import sys,os
print('===============================================================')
print('GoAgent����˲������, ��ʼ�ϴ�'+__uploaddir__+'�����')
print('===============================================================')
print('')
print('����������appid, ���appid����|�Ÿ���')
if __need_cookies__== False:
    if os.path.isfile('.appcfg_cookies'):
        os.remove('.appcfg_cookies') 
os.putenv('uploaddir', __uploaddir__)
os.putenv('http_proxy', __proxy__)
os.putenv('https_proxy', __proxy__)
sys.path.insert(0, 'uploader.zip')
import appcfg;appcfg.main()
print('')
print('�ϴ��ɹ����༭proxy.ini�����appid���ȥ��лл���밴������˳�����')
print('===============================================================')
print('�����Է��� https://���APPID.appspot.com/version �鿴����˰汾')
print('===============================================================')

