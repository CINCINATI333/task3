l = open('lessons.txt','r')
q = open('quality.txt','r')
p = open('participants.txt','r')
u = open('users.txt','r')
les = l.read()
qua = q.read()
part = p.read()
users = u.read()

les = les.split('\n ')
qua = qua.split('\n ')
part = part.split('\n ')
users = users.split('\n ')
for k in range(len(qua)):
    qua[k] = qua[k].split('|')
    qua[k][0] = qua[k][0].replace(' ','')
    qua[k][1] = qua[k][1].replace(' ','')
for k in range(len(part)):
    part[k] = part[k].split('|')
    part[k][0] = part[k][0].replace(' ','')
    part[k][1] = part[k][1].replace(' ','')
for k in range(len(users)):
    users[k] = users[k].split('|')
    users[k][0] = users[k][0].replace(' ','')
    users[k][1] = users[k][1].replace(' ','')
#print(qua)
for k in range(len(les)):
    les[k] = les[k].split('|')
    les[k][0] = les[k][0].replace(' ','')
    les[k][1] = les[k][1].replace(' ','')
    les[k][2] = les[k][2].replace(' ','')
#print(les)
a = []
for k in range(len(les)):
    if str(les[k][2]) == 'phys':
        a.append(les[k])
for k in range(len(les)):
    les[k][3] = les[k][3].split()
    #print(les[k][3])
b = []
i = 0
date = []
for k in range(len(a)):
    date.append(a[k][3][0])
date = set(date)
date = list(date)
date.sort()
#print(date)
d = [[],[],[],[],[],[],[],[],[],[]]
for k in range(len(date)):
    for i in range(len(a)):
        if a[i][3][0] == date[k]:
            d[k].append(a[i])
#print(part)
'''mbydate = []
for k in range(len(a)):
    for i in range(len(qua)):
        if a[k][0] == qua[i][0]:
            mbydate.append(qua[i])'''
#mbydate = set(mbydate)
#bydate = list(mbydate)
#print(mbydate)
#print(len(mbydate))

'''
print('-----------------------------') 
print(d[0])    #Все Уроки по физике 11 января
print('-----------------------------')       
print(d[0][0])
print('-----------------------------')

marks = []
for k in range(len(d)):
    for i in range(len(qua)):
        if d[k][0][0] == qua[i][0]:
'''
print(int(qua[0][1])+int(qua[1][1]))
#print(d[k])
    # print(a[k][3],'---',a[k][3][0][8],a[k][3][0][9],'---', a[k][0])


#for k in range(len(les)):
    #if les[k][3][1][0] == '2' and les[k][3][1][1] >= '1':
        #print(les[k][3]) # ['2020-01-16', '21:34:17.949531'] - только в этом случае из-за часового пояса изменится дата 

l.close
q.close
p.close
u.close