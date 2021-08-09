from flask import Flask
from flask import request, render_template
from mysql import connector

HOST = '0.0.0.0'
PORT_NUM = 10000

HOST_DB = '172.28.5.102'
TEST_DB = 'testdb'

MYSQL_USER = 'moyk-local'
MYSQL_PASS = 'M0yk-Loc4l'

app = Flask(__name__)

class DBInteface:
	def __init__(self):
		self.mysql_db = None
	
	def __del__(self):
		self.mysql_db.close()

	def conn_mysql(self):
		self.mysql_db = connector.connect(
			host=HOST_DB,
			user=MYSQL_USER,
			password=MYSQL_PASS,
			database=TEST_DB
		)
		print('Successfully connected to mysql')

	def get(self, id):
		cursor = self.mysql_db.cursor()
		cursor.execute(sql_query.format(id))
		return cursor.fetchall()

interface = DBInteface()
interface.conn_mysql()

@app.route('/')
def home():
	return 'What else did you expect?'

sql_query = 'SELECT * FROM players WHERE id = {0}'

@app.route('/result')
def result():
	id = request.args.get('id')
	res = interface.get(id)
	return render_template('result.html', res=res[0])

if __name__ == '__main__':
	app.run(host=HOST, port=PORT_NUM)