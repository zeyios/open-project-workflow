# coding: utf-8
#
# Copyright (c) 2020 zey <zeyio.com>
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2020-04-09
#
import sys
from workflow import Workflow3, web, ICON_WEB

from os import listdir
from os.path import isdir, join, expanduser

# 获取文件列表
def getFileList():
   path = wf.args[1]
   log.debug('path: ' + path)
   path = expanduser(path)
   return [f for f in listdir(path) if isdir(join(path, f))]

def main(wf):
    # 获取搜索参数
    searchKey = wf.args[0]
    log.debug('searchKey: ' + searchKey)
    # 文件列表缓存3s
    fileList = wf.cached_data('projects', getFileList, max_age=3)
    # 根据query过滤目录
    for x in fileList:
        if (searchKey and (searchKey in x)):
            wf.add_item(title=x, arg=x, valid=True);
    
    # 把应该展示的内容发送给Alfred
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))