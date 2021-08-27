from flask import Flask
from flask import request, render_template
from mysql import connector
from gevent import pywsgi
import redis
import logging

logging.basicConfig(level=logging.INFO)

HOST = '0.0.0.0'
PORT_NUM = 5000

HOST_DB = '172.28.5.102'
TEST_DB = 'testdb'

MYSQL_USER = 'moyk-local'
MYSQL_PASS = 'M0yk-Loc4l'

PLAYERS_COLS = ('id', 'name', 'rank', 'score', 'join_year')

EXPIRATION_SECS = 600

app = Flask(__name__)

class DBInteface:
	def __init__(self):
		self.mysql_db = None
		self.redis = None
	
	def __del__(self):
		self.mysql_db.close()

	def conn_mysql(self):
		self.mysql_db = connector.connect(
			host=HOST_DB,
			user=MYSQL_USER,
			password=MYSQL_PASS,
			database=TEST_DB
		)
		logging.info('Successfully connected to MySQL')

	def conn_redis(self):
		self.redis = redis.Redis(host=HOST_DB, port=6379, db=0)
		logging.info('Successfully connected to Redis')

	def get(self, id):
		if self.redis.exists(id):
			logging.info(f'Cache hit, key found in Redis (id={id})')
			return self.get_redis(id)
		
		logging.info(f'Cache miss, reading from MySQL (id={id})')
		row = self.get_mysql(id)
		hm = {}
		for i in range(len(PLAYERS_COLS)):
			hm[str(PLAYERS_COLS[i])] = row[i]
		self.hmset_redis(id, hm)

		return row
		
	def hmset_redis(self, id, hm):
		self.redis.hmset(id, hm)
		self.redis.expire(id, EXPIRATION_SECS)

	def get_redis(self, id):
		row = self.redis.hgetall(id)
		row = {str(k, 'utf-8'): str(v, 'utf-8') for k, v in row.items()}
		res = []
		for col in PLAYERS_COLS:
			res.append(row[col])
		self.redis.expire(id, EXPIRATION_SECS)
		return tuple(res)

	def get_mysql(self, id):
		cursor = self.mysql_db.cursor()
		cursor.execute(sql_query.format(id))
		return cursor.fetchall()[0]

interface = DBInteface()
interface.conn_mysql()
interface.conn_redis()

@app.route('/')
def home():
	return 'What else did you expect?'

sql_query = 'SELECT * FROM players WHERE id = {0}'

@app.route('/request')
def request_():
	return render_template('request.html')

@app.route('/result')
def result():
	id = request.args.get('id')
	res = interface.get(id)
	return render_template('result.html', res=res)

if __name__ == '__main__':
	server = pywsgi.WSGIServer((HOST, PORT_NUM), app)
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		pass