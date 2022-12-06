#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    tag- Web Application Security Scanner
# @repo:    https://github.com/tag888/tag.git
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

def UTF8(string):
	if isinstance(string,unicode):
		return string.encode('UTF-8')
	else:
		return str(string)