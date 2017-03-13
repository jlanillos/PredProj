# This script reads the document of asa of the new 50 proteins and creates a database with the threshold for buried or exposed that the user chooses manually.
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

th = input('Introduce a threshold (from 0 to 1)')
th = float(th)
filesave = '50newprot_asa_thr_' + str(int(th*100)) + '.txt'


aux = cont[18].split()[2]

for line in cont[18:len(cont)]:
	line_aux = line
	line = line.split()
	
	if line[2] == aux:
		
		eb = float(line[4])
		if eb >= th:
			eb = 'e'
		else:
			eb = 'b'

		f = f + eb
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


f = open(filesave,'w')

counter = 0

for i in S:
	f.write('>'+T[counter]+'\n')
	f.write(S[counter]+'\n')
	f.write(F[counter].lower()+'\n')
	counter = counter + 1
f.close()
		


