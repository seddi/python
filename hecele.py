#!/usr/bin/python3
#-*- coding:utf-8 -*-

import sys
import re

sesli  = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü', 'A', 'E', 'I', 'i', 'O', 'Ö', 'U', 'Ü']
sessiz = ['b', 'c', 'ç', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z', 'B', 'C', 'Ç', 'D', 'F', 'G', 'Ğ', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'Ş', 'T', 'V', 'Y', 'Z' ]

def reg_exp(list):
	for i in list:
		c = re.compile("^[rskmn]|[rskmn]$")
		t = re.compile("[^çÇğĞıİöÖşŞüÜ]+")
		if c.search(i):
			str = list_to_str(list)
			if len(t.search(str).group()) == len(str):
				return str+"\n"

def list_to_str(list):
	return ''.join(list)

def spell(w):
	w = w[::-1]
	s_list = list()
	while True:
		state = True
		for chr in w:
			if chr in sesli:
				state = False
				break
		if state or not len(w):
			if not s_list:
				return reg_exp(s_list.insert(0, w))
			else:
				s_list[0] = (s_list[0][::-1] + w[::-1])[::-1]
				return reg_exp(s_list)
		i = w.find(chr)
		if len(w) == i+1 or ((not w[i+1] in sessiz) and i+1 < len(w)):
			s_list.insert(0, w[:i+1][::-1])
			w = w[i+1:]
		elif w[i+1] in sessiz and len(w) >= i+2:
			s_list.insert(0, w[:i+2][::-1])
			w = w[i+2:]

def word_list(liste):
	name_list = list()
	for word in liste:
		if len(word):
			word = spell(word)
			if word:
				name_list.append(word)
	return name_list
def write_to_file(list):
	f_name = input("yazilacak dosya adi giriniz (uzantısız olarak <isimler> gibi ) : ")
	try:
		file = open(f_name + ".txt" , "w")
		file.writelines(list)
	except IOError as error:
		error_msg(error)
	finally:
		file.close()
def error_msg(msg):
	print("{0} ".format(msg))
	sys.exit()

state = True
while state:
	f_name = input("okunacak dosya adi (uzantısı ile  <isimler.txt> gibi ) : ")
	if f_name:
		try:
			file = open(f_name, "r", encoding="utf-8")
			print ("Okuma yapılıyor... ")
			data = [i for i in file.read().splitlines() if len(i) == 5 or len(i) == 4 or len(i) == 6 ]
			write_to_file(word_list(data))
			state = False
		except IOError as error:
			error_msg(error)
		finally:
			file.close()
	else:
		print ("Dosya adi belirtmediniz!...")
		state = True

