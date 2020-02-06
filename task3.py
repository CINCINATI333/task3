l = open('lessons.txt','r')
q = open('quality.txt','r')
p = open('participants.txt','r')
u = open('users.txt','r')
les = l.read()
qua = q.read()
part = p.read()
users = u.read()
def unique(x):
    x = set(x)
    x = list(x)
    return x

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
teach = [] # - все учителя
for k in range(len(users)):
    if users[k][1] == 'tutor':
        teach.append(users[k])
#print(teach)

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
d = [[],[],[],[],[],[],[],[],[],[]] # массив с уроками за каждый день
for k in range(len(date)):
    for i in range(len(a)):
        if a[i][3][0] == date[k]:
            d[k].append(a[i])
#print(d[0])
event = []
#for j in range(len)
for k in range(len(d)):
    for i in range(len(part)):
        if d[0][k][1] == part[i][0]:
            event.append(part[i][1]) # - ID всех пользователей, которые были в этот день
event = set(event)
event = list(event)
teaevent = []
for k in range(len(event)):
    for i in range(len(teach)):
        if event[k] == teach[i][0]: #Если ID человека совпадает с ID учителя, то он учитель)))
            teaevent.append(event[k])
            teaevent = unique(teaevent)  #ID Учителей, которые преподавали в этот день (11 янв. например)
#print(teaevent) 

#print(teach) # - Тут все чуваки, которые были на уроках 11 января
#print(part)
lesday = [] #- тут будут уроки, которые вели учителя
for k in range(len(teaevent)):
    for i in range(len(d)):
        if d[0][i][1] == teaevent[k]: #Если ID учителя, который преподавал в этот день равен другому ID, значит вытягиваем номер урока
            lesday.append()

l.close
q.close
p.close
u.close
