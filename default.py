#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, urllib, urllib2

sys.path.append(os.path.join(os.getcwd().replace(';', ''), 'resources', 'lib'))


if (__name__ == "__main__" ):
    import addon
    addon.addon_main()

# vim:set tabstop=4 softtabstop=4 shiftwidth=4 expandtab: 
