#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    tag - Web Application Security Scanner
# @repo:    https://github.com/m4ll0k/tag
# @author:   (tag)
# @license: See the file 'LICENSE.txt

import os
import sys
from colors import Colors

class Banner:

	r  = Colors().red(1)
	nr = Colors().red(0) 
	g  = Colors().green(1)
	ng = Colors().green(0)
	y  = Colors().yellow(9)
	ny = Colors().yellow(0)
	b  = Colors().blue(1)
	nb = Colors().blue(0)
	c  = Colors().cyan(1)
	nc = Colors().cyan(0)
	p  = Colors().purple(1)
	np = Colors().purple(7)
	w  = Colors().white(1)
	nw = Colors().white(0)
	e  = Colors().end()

	# def banner(self):
	# 	print self.nw+"~/#"+self.e+" tag - Web Application Security Scanner"+self.e
	# 	print self.nw+"~/#"+self.e+" Codename - "+self.y+"tag"+self.e
	# 	print self.nw+"~/#"+self.e+" Momo Outaadi (@M4ll0k)"+self.e
	# 	print self.nw+"~/#"+self.e+" https://github.com/tag888/tag.git"+self.e

	def usage(self,exit=False):
		name = os.path.basename(sys.argv[0])
		self.banner()
		print ("Usage:\n")
		print ("\t-u --url\tTarget URL (eg: http://example.com)")
		print ("\t-s --scan\tScan Options (default=0):\n")
		print ("\t\t0:\tFull Scan")
		print ("\t\t1:\tBruteforce (dirs,files,..)")
		print ("\t\t2:\tDisclosure (ip,emails,..)")
		print ("\t\t3:\tAttacks (sql,lfi,..)")
		print ("\t\t4:\tOthers (webdav,..)")
		print ("\t\t5:\tVulns (shellshock,..)\n")
		print ("\t--crawler\tDeep crawling (slow)")
		print ("\t--agent\t\tUse the specified user-agent")
		print ("\t--random-agent\tUse a random user-agent")
		print ("\t--redirect\tRedirect target URL, default=True")
		print ("\t--timeout\tSet timeout, default=None")
		print ("\t--cookie\tSet cookie, default=None")
		print ("\t--proxy\t\tSet proxy, (host:port)")
		print ("\t--verbose\tVerbose output")
		print ("\t--version\tShow version")
		print ("\t--help\t\tShow this help and exit\n")
		print ("Examples:\n")
		print ("\t"+name+" --url http://example.com")
		print ("\t"+name+" --url http://example.com --scan [0-5]")
		print ("\t"+name+" --url http://example.com --scan 1 --crawler\n")
		if exit:
			sys.exit(0)

	def version(self,exit=False):
		self.banner()
		print ("~/# tag - Web Application Security Scanner (v0.1.1)\n")
		if exit:
			sys.exit(0)