from flask import Flask, request
import pymysql.cursors
import configparser

app = Flask(__name__)

config = configparser.RawConfigParser()
config.read('db.conf')
configDict = dict(config.items('DB_DETAILS'))
print(configDict)

app.config['MYSQL_USER'] = configDict['mysql_user']
app.config['MYSQL_PASSWORD'] = configDict['mysql_password']
app.config['MYSQL_HOST'] = configDict['mysql_host']
app.config['MYSQL_DB'] = configDict['mysql_db']

@app.route("/")
def index():
  return "Application Works"

@app.route("/getEmployeeIds")
def getEmployeeIds():
  empName = request.args.get('name')
  connection = pymysql.connect( host=app.config['MYSQL_HOST'],
                              user=app.config['MYSQL_USER'],
                              password=app.config['MYSQL_PASSWORD'],
                              database=app.config['MYSQL_DB'],
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor )
  with connection:
    with connection.cursor() as cursor:
      sql = "SELECT emp_no from employees where first_name=%s"
      print(sql)
      cursor.execute(sql, (empName,))
      result = cursor.fetchone()
  return result

if __name__ == '__main__':
  app.run(debug = True)