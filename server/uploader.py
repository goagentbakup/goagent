#!/usr/bin/env python
# coding=utf-8
# Contributor:
# Phus Lu <phus.lu@gmail.com>
# Wang Wei Qiang <wwqgtxx@gmail.com>

import sys,os
print('===============================================================')
print('GoAgent����˲������, ��ʼ�ϴ�python�����')
print('===============================================================')
print('')
print('����������appid, ���appid����|�Ÿ���')
os.putenv('uploaddir', 'python')
sys.path.insert(0, 'uploader.zip')
import appcfg;appcfg.main()
print('')
print('�ϴ��ɹ����༭proxy.ini�����appid���ȥ��лл���밴������˳�����')
print('===============================================================')
print('�����Է��� https://���APPID.appspot.com/ �鿴����˰汾')
print('===============================================================')

