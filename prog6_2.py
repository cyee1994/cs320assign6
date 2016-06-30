#!/usr/bin/python3

class Token:
	
	def __init__(self,tokenString):
		self.tokenString = tokenString
	
	def GetStringValue(self):
		stringVal = self.tokenString
		return stringVal
	def GetElementType(self):
		type = "Unknown"
		return type

class LiteralIntToken:
	def __init__(self,tokenString):
		self.tokenString = tokenString
	
	def GetStringValue(self):
		stringVal = self.tokenString
		return stringVal
	def GetElementType(self):
		type = "Literal-Int"
		return type


class NameToken:

	def __init__(self,tokenString):
		self.tokenString = tokenString
	
	def GetStringValue(self):
		stringVal = self.tokenString
		return stringVal
	def GetElementType(self):
		type = "Name"
		return type



