import pymorphy2
import string
import codecs
import re

morp = pymorphy2.MorphAnalyzer()
filesPath = 'C:\\Users\\Kirill\\Desktop\\Site\\' 
for i in range(1,101):
	nameFile = filesPath + str(i) + '.txt'
	f = codecs.open(nameFile, 'r', 'utf_8_sig')
	data = f.read()
	out = data.translate(str.maketrans('', '', string.punctuation + string.ascii_letters + string.digits + '@' + u"\u00A9")).split()
	f.close()
	w = codecs.open(nameFile, 'w', 'utf_8_sig')
	for word in out:
		infWord = morp.parse(word)[0]
		if not infWord is None:
			w.write(infWord.normal_form+"\r\n")
	w.close()