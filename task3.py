import pymysql;
from pymysql.cursors import DictCursor

#database connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='lolkek',
    charset='utf8mb4',
    cursorclass=DictCursor
)

#file connection
lessons_handle = open('lessons.txt','r')
quality_handle = open('quality.txt','r')
participants_handle = open('participants.txt','r')
users_handle = open('users.txt','r')

#read data
les = lessons_handle.read()
qua = quality_handle.read()
part = participants_handle.read()
users = users_handle.read()

# функция выводит данные из массива в читаемом виде
# Параметры:
# - массив (спсисок)
# - заголовок
# - лимит
def output_array( arr, title = "", limit = 0 ):
    print( '----------' + '\n' + title + '\n' )
    col = 0
    for el in arr:
        if limit and col > limit:
            break
        col += 1
        print( str( el ) )

#parse all stuff
les = les.split('\n ')
qua = qua.split('\n ')
part = part.split('\n ')
users = users.split('\n ')
for k in range(len(qua)):
    qua[k] = qua[k].split('|')
    qua[k][0] = qua[k][0].replace(' ','')
    qua[k][1] = qua[k][1].replace(' ','')
output_array(qua, "quality", 20 )
for k in range(len(part)):
    part[k] = part[k].split('|')
    part[k][0] = part[k][0].replace(' ','')
    part[k][1] = part[k][1].replace(' ','')
output_array(part, "part",  20 )
for k in range(len(users)):
    users[k] = users[k].split('|')
    users[k][0] = users[k][0].replace(' ','')
    users[k][1] = users[k][1].replace(' ','')
output_array(users, "users", 20 )
for k in range(len(les)):
    les[k] = les[k].split('|')
    les[k][0] = les[k][0].replace(' ','')
    les[k][1] = les[k][1].replace(' ','')
    les[k][2] = les[k][2].replace(' ','')
output_array(les, "lessons", 20 )

#get info from db
cur = connection.cursor()
cur.execute( "select * from lessons" )
output_array( cur, "SQL query", 20 )

# Завершаем подключение.
cur.close()
connection.close()