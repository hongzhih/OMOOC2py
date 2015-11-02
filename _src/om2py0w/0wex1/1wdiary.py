#!usr/bin/env python
#-*- coding:utf-8 -*-

import datetime

def main():
	read_diary()
	while True:
		content = raw_input('What do you want to write:')
		if content == 'quit':
			print u"再见！"
			break
		elif content == 'history':
			read_diary()
		else:
			content_append(content)
			
def read_diary():
	diary = open("diary2v.txt", "a+")
	for line in diary:
		print line

def content_append(content):
	diary_c = open ("diary2v.txt", "a")
	now = datetime.datetime.now()
	curr = now.strftime ("%Y-%m-%d %H:%M:%S")
	diary_c.write (curr+":"+content+"\n")
	
if __name__=="__main__":
	main()