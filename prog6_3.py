#!/usr/bin/python3
from prog6_1 import*
from prog6_2 import*
import sys
print("Assignment #6-3, Christopher Yee, christopheryee@att.net")
filename = (str(sys.argv[1]))

tokenizedFile2DArray = []

tokenizedFile2DArray = Tokenize(filename)

for line in tokenizedFile2DArray:
	lines = line
	for word in lines:
		if word.isdigit():
			wordInt = LiteralIntToken(word)
			print(wordInt.GetElementType(),end=" ")
		
		elif type(word) is str:
			wordStr = NameToken(word)
			print(wordStr.GetElementType(),end=" ")
	print()
