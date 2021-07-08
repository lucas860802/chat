


def read_file(filename):
	lines = []
	with open(filename, 'r', encoding ='utf-8-sig')as f:
		for line in f:
			lines.append(line.strip()) #strip去掉\n
	return lines


def convert(lines):
	person = None #其他語言None = null
	lucas_word_count = 0
	lucas_sticker_count = 0
	lucas_image_count = 0
	sandy_word_count = 0
	sandy_sticker_count = 0
	sandy_image_count = 0
	for line in lines: #把lines的東西一個一個叫出來
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == '黃衍凱Lucas':
			if s[2] == '貼圖':
				lucas_sticker_count += 1
			elif s[2] == '圖片':
				lucas_image_count += 1
			else:
				for m in s[2:]:
					lucas_word_count += len(m)
		if name == 'SandyYu':
			if s[2] == '貼圖':
				sandy_sticker_count += 1
			elif s[2] == '圖片':
				sandy_image_count += 1
			else:
				for m in s[2:]:
					sandy_word_count += len(m)
	print('黃衍凱Lucas說了', lucas_word_count, '個字')
	print('黃衍凱Lucas傳了', lucas_sticker_count, '個貼圖' )
	print('黃衍凱Lucas傳了', lucas_sticker_count, '張圖片' )

	print('SandyYu說了', sandy_word_count, '個字')
	print('SandyYu傳了', lucas_sticker_count, '個貼圖' )
	print('Sandy傳了', lucas_sticker_count, '張圖片' )


def write_file(filename, lines):
	with open (filename, 'w')as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('[LINE]Sandy Yu.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)


main()  #使用function
