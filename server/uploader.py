#!/usr/bin/env python
# coding=utf-8
# Contributor:
# Phus Lu <phus.lu@gmail.com>
# Wang Wei Qiang <wwqgtxx@gmail.com>

__uploaddir__ = 'python'

import sys,os
os.remove('.appcfg_cookies') 
print('===============================================================')
print('GoAgent����˲������, ��ʼ�ϴ�'+__uploaddir__+'�����')
print('===============================================================')
print('')
print('����������appid, ���appid����|�Ÿ���')
os.putenv('uploaddir', __uploaddir__)
sys.path.insert(0, 'uploader.zip')
import appcfg;appcfg.main()
print('')
print('�ϴ��ɹ����༭proxy.ini�����appid���ȥ��лл���밴������˳�����')
print('===============================================================')
print('�����Է��� https://���APPID.appspot.com/version �鿴����˰汾')
print('===============================================================')

