#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file	   : demo
# @Date    : 2018-07-02 09:23:15
# @Author  : Destroyers (https://github.com/lguobin)
# @Link    : https://github.com/lguobin
# @Version : $1.0$


from subprocess import call
from pip._internal.utils.misc import get_installed_distributions

import os
from sys import version_info


class _check():
	def __init__(self):
		print(u"\n\t\t请输入你配置的pip文件名，是pip2还是pip3")
		print(u"\t\t请输入你配置的pip文件名，是pip2还是pip3")
		print(u"\t\t请输入你配置的pip文件名，是pip2还是pip3\n")
		self._pip = raw_input("Please input your code? ") if version_info.major == 2 else input("Please input your code? ") if version_info.major == 3 else 1

	def index(self):
		'''Start'''
		try:
			while True:
				print("===" *20)
				print("")
				print("")
				print(u"\t\t 1、查看已安装的包")
				print(u"\t\t 2、查看包有无更新")
				print(u"\t\t 3、更新所有的包")
				print(u"\t\t 4、单独更新某个包例如：A")
				print(u"\t\t 5、卸载包")
				print(u"\t\t 6、安装 requirement 包，请把 requirement.txt 文件放在脚本同路径下")
				print(u"\t\t 7、导出 requirement 包")
				print("")
				print("")
				print(u"\t\t退出输入：0")
				print("")
				print(u"\t\t输入对应的数字进入不同的功能")
				print("===" *20)
				print("")
				n = int(raw_input("Please enter the number (1,2,3,4,5/0)? ")) if version_info.major == 2 else int(input("Please enter the number (1,2,3,4,5/0)? ")) if version_info.major == 3 else 1
				if n == 1:
					self._Package_ALL_()
				elif n == 2:
					self._Check_Package_()
				elif n == 3:
					self._Upgrade_()
				elif n == 4:
					Pack = raw_input("Please Pack? ") if version_info.major == 2 else input("Please Pack? ") if version_info.major == 3 else 1
					self._Alone(Pack)
				elif n == 5:
					Pack = raw_input("Please Pack? ") if version_info.major == 2 else input("Please Pack? ") if version_info.major == 3 else 1
					self._Uninstall(Pack)
				elif n == 6:
					print("Please wait... ")
					self._requirement()

				elif n == 7:
					print("Please wait... ")
					self._Pull_requirement()

				elif n == 0:
					break
				else:
					print("input Error~")
					continue
		except ValueError as e:
			raise ValueError("number input Error")

# # # # # ================
# # # # # ================
# # # # # ================
	def _Check_Python_(self, command):
		print(" ======  Check Python  ====== ")
		call("%s install --upgrade  %s" %(self._pip, data.project_name), shell=True)


	def _Package_ALL_(self):
		print(" ======  Upgrade Package  ====== ")
		call("%s list " %self._pip, shell=True)
		print("\n")
		print("\t\tDone~~\n\n\n")

	def _Check_Package_(self):
		call("%s list --outdated " %self._pip, shell=True)
		self._Proceed()

	def _Upgrade_(self):
		number = 0
		for data in get_installed_distributions():
			number += 1
			call("%s install --upgrade  %s" %(self._pip, data.project_name), shell=True)
		print("\n")
		print("\t\tDone~~\n\n\n")

	def _Alone(self, Package):
		URL = "https://pypi.tuna.tsinghua.edu.cn/simple"
		call("%s install %s -i %s" %(self._pip, Package, URL), shell=True)
		print("\n")
		print("\t\tDone~~\n\n\n")

	def _Uninstall(self, Package):
		call("%s uninstall  %s " %(self._pip, Package), shell=True)
		print("\n")
		print("\t\tDone~~\n\n\n")

	def _requirement(self):
		call("%s install -r requirements.txt " %self._pip, shell=True)
		print("\n")
		print("\t\tDone~~\n\n\n")

	def _Pull_requirement(self):
		call("%s freeze > requirements.txt " %self._pip, shell=True)
		print("\n")
		print("\t\tDone~~\n\n\n")


	def _Proceed(self):
		if version_info.major == 2:
			ask = raw_input("Proceed (y/n)? ")
		elif version_info.major == 3:
			ask = input("Proceed (y/n)? ")
		if ask == "y" or ask == "yes" or ask == "Yes":
			self._Upgrade_()
		elif ask == "n" or ask == "no" or ask == "NO":
			self._Done()
		else:
			print("Error~")

	def _Done(self):
		'''End'''
		print("\n \n \t\t\t======  Ok~ OK~  ======\n \n")
		print("\t \t======  You are the Boss!  ======")

	def log(self):
		call("%s list " %self._pip, shell=True)

if __name__ == '__main__':
	test = _check()
	test.index()