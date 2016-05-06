# coding=utf-8
# the above line is necessary to tell python what kind of encoding we're working with
# see: http://www.python.org/dev/peps/pep-0263/

from .pinyin import *

import os
import re

class Word():
	
	def __init__(self, traditional, simplified, pinyin, definition):
		self.traditional = traditional
		self.simplified = simplified
		self.pinyin = pinyin
		self.definition = definition


class CEDictParser():
	
	def parse_file(self, file_name):
		
		# EXAMPLE INPUT LINE:   㐖 㐖 [Ye4] /see
		# TRADITIONAL_HANZI SIMPLIFIED_HANZI [PINYIN] /TRANSLATION
		
		# Put each dictionary item into the array
		items = []

		f = open(file_name, "r")

		lines = f.readlines()
		
		for line in lines:
			l = line
			
			#These are info lines at the beginning of the file
			#NOTE: Might be useful to store version #, date, etc for dictionary reference
			if l.startswith(("#", "#!")):
				continue
			else:
				#partition out definition text, replace slahes with semicolons, normalize quotations, get rid of any \n
				defi = l.partition('/')[2].replace('/','; ').replace("\"", "'").strip()
				
				# defi might contain pinyin too
				try:
					defi_pin = defi.partition('[')[2].partition(']')[0]
					defi_pin = convert(defi_pin)
				except:
					defi_pin = ""

				defi = defi.partition('[')[0] + " " + defi_pin

				# defi might contain hanzi too, keep only simplified (\2 inst. \3)
				defi = re.sub(r'(.*)\s(\W*)\|(\W*)\s(.*)', r'\1 \2 \4', defi)

				#Get traditional hanzi
				trad = l.partition('[')[0].split(' ', 1)[0].strip(" ")
				# simpl hanzi
				simpl = l.partition('[')[0].split(' ', 1)[1].strip(" ")

				#Take the content in between the two brackets
				pin = l.partition('[')[2].partition(']')[0]
				
				pin = convert(pin);
				
				items.append(Word(trad,simpl,pin,defi))
		
		return items
			
