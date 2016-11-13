"""
A file to convert a .txt file to a JSON file seperated by lines

"""
import sys

def convert(args):
	assert(len(args)==2), "only .txt as arg"

	js = open("index.json", 'w+')
	js.write("{\n")
	with open(args[1]) as f:
		num, line, nextLine = 0, f.readline(), f.readline()
		while True:
			if(nextLine == ''):
				break
			line = nextLine
			js.write('\t"'+str(num)+'": "'+ line.rstrip('\n')+'",\n')
			nextLine = f.readline()
			num+=1
		js.write('\t"'+str(num)+'": "'+ line.rstrip('\n')+'"\n')
	js.write("}")
convert(sys.argv)

