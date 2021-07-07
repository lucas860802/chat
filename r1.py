
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding ='utf-8-sig')as f:
		for line in f:
			lines.append(line.strip()) #strip去掉\n
	return lines

def convert(lines):
	new = []
	person = None #其他語言None = null
	for line in lines: #把lines的東西一個一個叫出來
		if line == 'Allen':
			person = 'Allen'
			continue 
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ':' + line)
	return new

def write_file(filename, lines):
	with open (filename, 'w')as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()  #使用function
