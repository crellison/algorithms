# XOR DEMONSTRATION

import sys

def printDict(dict):
	for key in dict:
		print(key+' = '+str(dict[key]))

def xor(a,b):
	dict = {
		'var1': a,
		'var2': b
	}
	printDict(dict)
	print('XOR-ing values...')
	dict['var1'] = dict['var1'] ^ dict['var2']
	dict['var2'] = dict['var1'] ^ dict['var2']
	dict['var1'] = dict['var1'] ^ dict['var2']
	printDict(dict)

def printUsage():
	print('\n***')
	print('File takes two integer arguments to use as variables')
	print('The purpose of this is to show how to swap variable \nvalues without using a temp var')
	print('Run again as: python3 xor.py <var1> <var2>')
	print('***\n')

def isNumber(num):
	try:
		int(num)
		return True
	except ValueError:
		return False

if __name__ == '__main__':
	if len(sys.argv) != 3 or (not isNumber(sys.argv[1])) or (not isNumber(sys.argv[2])):
		printUsage()
	else:
		xor(int(sys.argv[1]), int(sys.argv[2]))