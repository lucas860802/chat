
lines = []
with open('3.txt', 'r', encoding ='utf-8-sig')as f:
		for line in f:    #每一行檔案的line加進lines清單
			lines.append(line.strip())   

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:] #第五個字開始到結尾
	print(time)
	print(name)
	
