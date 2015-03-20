# coding=utf-8
# the above line is necessary to tell python what kind of encoding we're working with
# see: http://www.python.org/dev/peps/pep-0263/

from pinyin import *

class Word():
	
	def __init__(self, hanzi, pinyin, definition):
		self.hanzi = hanzi
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
				#partition out definition text, replace slshes with semicolons, normalize quotations, get rid of any \n
				defi = l.partition('/')[2].replace('/','; ').replace("\"", "'").strip()
				#Get trad and simpl hanzis then split and take only the simplified
				han = l.partition('[')[0].split(' ', 1)[1].strip(" ")
				#Take the content in between the two brackets
				pin = l.partition('[')[2].partition(']')[0]
				
				pin = convert(pin);			
				
				items.append(Word(han,pin,defi))
		
		return items
			
