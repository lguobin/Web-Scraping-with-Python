#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-20 10:12:42
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup

import os
import re
import urllib.request
from sys import version_info
from time import sleep as xxxxx


class Myjob():
	'''
		# 抓取51job相关职位信息
	'''

	def __init__(self):
		connect = MongoClient(host='127.0.0.1', port=27017)
		data = connect.job
		self.table = data.job_work

	def _Mongo_Connect_(self, save_db):
		self.table.save(save_db)

	def _del(self):
		self.table.remove()

	def _Get_Jobs_(self):
			print(u"请启动 MongoDB port 27017 不然会闪退哦！")
			print(u"请启动 MongoDB port 27017 不然会闪退哦！")
			print(u"请启动 MongoDB port 27017 不然会闪退哦！\n\n\n")
			print("=" *38)
			print(u"如果你的 MongoDB 没有 job_work 表，那证明没有找到数据！")
			print(u"你想在哪里工作 / 你想在哪里浪：？\n")
			self.location = self._City(raw_input("Please input your City? \n") if version_info.major == 2 else input("Please input your City? \n") if version_info.major == 3 else 1)
			print(u"\n你想打工 / 搬砖？还是搬黄金：？\n")
			self.name = raw_input("Please input your jobs? \n") if version_info.major == 2 else input("Please input your jobs? \n") if version_info.major == 3 else 1
			self._del()
			#初始化数据
			frequency = True
			line = 1
			url_name = urllib.request.quote(self.name.encode('utf-8'))
			header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87'}
			while frequency:
				url = 'http://search.51job.com/list/{},000000,0000,00,9,99,{},2,{}.html'.format(self.location, url_name.replace('%','%25'),line)
				# url = 'http://search.51job.com/list/020000,000000,0000,00,9,99,{},2,{}.html'.format(url_name.replace('%','%25'),line)
				req = requests.get(url,headers=header)
				bs = BeautifulSoup(req.content,'html.parser')
				page = bs.find('span',class_="td").string
				page_num = re.search('\d{1,}',page).group()
				if line <= int(page_num):
					print('\n搜索结果共有 %s 页，\t 正在抓取 %s 页面信息 \n'%(page_num, line))
					div = bs.find_all('div',class_="el")
					for data in div:
						if data.find_all('p', class_="t1 "):
							save={}
							save['Salary_money'] = data.find('span',class_="t4").string
							save['Job_title'] = data.p.span.a.attrs['title']
							save['company_name'] = data.find('span',class_="t2").a.attrs['title']
							save['location'] = data.find('span',class_="t3").string
							save['job_pushtime'] = data.find('span',class_="t5").string
							save['Url'] = data.p.span.a.attrs['href']
							self._Mongo_Connect_(save)
					line += 1
				else:
					frequency = False


	def _City(self, code):
		if code == "北京":
			return "010000"
		elif code == "上海":
			return '020000'
		elif code == "广州":
			return '030200'
		elif code == "深圳":
			return '040000'
		elif code == "武汉":
			return '180200'
		elif code == "西安":
			return '200200'
		elif code == "杭州":
			return '080200'
		elif code == "南京":
			return '070200'
		elif code == "成都":
			return '090200'
		elif code == "重庆":
			return '060000'
		elif code == "东莞":
			return '030800'
		elif code == "大连":
			return '230300'
		elif code == "沈阳":
			return '230200'
		elif code == "苏州":
			return '070300'
		elif code == "昆明":
			return '250200'
		elif code == "长沙":
			return '190200'
		elif code == "合肥":
			return '150200'
		elif code == "宁波":
			return '080300'
		elif code == "郑州":
			return '170200'
		elif code == "天津":
			return '050000'
		elif code == "青岛":
			return '120300'
		elif code == "济南":
			return '120200'
		elif code == "哈尔滨":
			return '220200'
		elif code == "长春":
			return '240200'
		elif code == "福州":
			return '110200'
		elif code in "珠三角（惠州、汕头、珠海、佛山、中山、江门、湛江、肇庆、清远）":
			return '01'
		else:
			print("您输入的城市暂时无法获得招聘信息，需要开通请联系作者购买专业版即可查看更多城市招聘信息")
			print("您输入的城市暂时无法获得招聘信息，需要开通请联系作者购买专业版即可查看更多城市招聘信息")
			print("您输入的城市暂时无法获得招聘信息，需要开通请联系作者购买专业版即可查看更多城市招聘信息")


if __name__=='__main__':
	j = Myjob()
	j._Get_Jobs_()