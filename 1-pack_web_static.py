#!/usr/bin/python3
""" Compress before sending"""


from fabric.api import *
import os.path
from os import path
from datetime import datetime
from os.path import exists


def do_pack():
    """ creates tar archive"""
    if path.exists("versions") is False:
        local("mkdir versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    pathfile = "versions/web_static" + date + ".tgz"
    local('tar cvfz ' + pathfile + ' web_static')
    if exists(pathfile):
        return (pathfile)
    return None
