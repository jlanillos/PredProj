filename = '50newprot_asa_thr_5to40.txt'
f = open(filename,'r')
cont = list()
for line in f.readlines():
	cont.append(line.rstrip())
import math

acc_list = list()
f1_list = list()
matt_list = list()

for i in cont:
	if i[0] == '[':
		t = i
		t = t[1:len(t)-2]
		t = t.split()
		t = list(map(int, t))


		acc =(t[0]+t[3])/(t[0]+t[1]+t[2]+t[3])
		f1 = (2*t[3])/((2*t[3])+ t[1] + t[2])
		matt = (sum(t))/(math.sqrt((t[1]+t[3])*(t[2]+t[3])*(t[0]+t[1])*(t[0]+t[2])))
		acc_list.append(acc)
		f1_list.append(f1)
		matt_list.append(matt)
	elif i[0] == 'C':
		time = i.split()
		time = time[len(time)-1]
	elif i[0] == 'K':
		param = i.split()
		ws = param[4]
		trainsets = param[7]
	else:
		print(i)

