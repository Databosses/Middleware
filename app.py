from flask import Flask, request, jsonify
import sqlite3
import configparser

app = Flask(__name__)

config = configparser.RawConfigParser()
config.read('db.conf')
configDict = dict(config.items('DB_DETAILS'))
print(configDict)

app.config['CONNECTION'] = configDict['path']

@app.route("/")
def index():
  return jsonify({'message': 'Application Started'})

@app.route("/getDBPath")
def getDBPath():
  return jsonify({'dbPath': app.config['CONNECTION']})

@app.route("/getIds")
def getIds():
  empName = request.args.get('name')
  print(empName)
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "SELECT id, sharktype from sharks where name='{}'".format(empName)
  print(sql)
  cursor.execute(sql)
  result = cursor.fetchall()
  print(result)
  return str(result)

if __name__ == '__main__':
  app.run(debug = True)