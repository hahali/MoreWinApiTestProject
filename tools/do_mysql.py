# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host='192.168.10.16',user='testMysqlAll',password='ZXZBWmXxB54Fns',database='db_kxlive_members',charset='utf8')
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# 定义要执行的SQL语句
# sql ='select * from live_anchor where id=170538'
#sql ='select * from live_anchor where db_kxlive_chat_room.live_anchor.id>=170552'
sql='select max(phone) from member'
# 执行SQL语句
cursor.execute(sql)
result=cursor.fetchall()
print(result)

# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()