#!/usr/bin/python3

def Tokenize( fileName ):
	with open (fileName) as f:
		tokens = [line.split() for line in f]
	f.close()
	return tokens




