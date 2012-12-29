#!/usr/bin/env python
# coding=utf-8
# Contributor:
# Phus Lu <phus.lu@gmail.com>
# Wang Wei Qiang <wwqgtxx@gmail.com>

import sys,os
print('===============================================================')
print('GoAgent服务端部署程序, 开始上传python服务端')
print('===============================================================')
print('')
print('请输入您的appid, 多个appid请用|号隔开')
os.putenv('uploaddir', 'python')
sys.path.insert(0, 'uploader.zip')
import appcfg;appcfg.main()
print('')
print('上传成功，编辑proxy.ini把你的appid填进去，谢谢。请按任意键退出程序。')
print('===============================================================')
print('您可以访问 https://你的APPID.appspot.com/ 查看服务端版本')
print('===============================================================')

