

filename = '50newproteins_asa.txt'
f = open(filename,'r')

cont = list()

for lines in f.readlines():
	line = lines.rstrip()
	cont.append(line)

f.close()

F = list() #feature list
S = list() #sequence list
T = list() #title list

f = ''
s = ''


aux = cont[18].split()[2]

for line in cont[18:len(cont)]:
	line_aux = line
	line = line.split()
	
	if line[2] == aux:

		f = f + line[0]
		s = s + line[1]
		if line_aux == cont[len(cont)-1]:
			F.append(f)
			S.append(s)
			T.append(aux)
	else:
		F.append(f)
		S.append(s)
		T.append(aux)
		f = line[0]
		s = line[1]
		aux = line[2]


f = open('database_50newproteins_asa.txt','w')

counter = 0

for i in S:
	f.write('>'+T[counter]+'\n')
	f.write(S[counter]+'\n')
	f.write(F[counter].lower()+'\n')
	counter = counter + 1
f.close()
		





