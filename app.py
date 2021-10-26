from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import configparser

app = Flask(__name__)
CORS(app)

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

  sql = "SELECT ID, FIRSTNAME from EMPLOYEE where FIRSTNAME='{}'".format(empName.upper())
  print(sql)
  cursor.execute(sql)
  result = cursor.fetchall()
  cursor.close()
  connection.close()
  print(result)
  return jsonify(result)
  # return str(result)

@app.route("/getEmpIds")
def getEmpIds():
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "SELECT ID from EMPLOYEE"
  print(sql)
  cursor.execute(sql)
  result = cursor.fetchall()
  cursor.close()
  connection.close()
  print(result)
  return jsonify(result)

@app.route("/getEmps")
def getEmps():
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()

  sql = "SELECT ID, FIRSTNAME from EMPLOYEE"
  print(sql)
  cursor.execute(sql)
  result = cursor.fetchall()
  cursor.close()
  connection.close()
  print(result)
  return jsonify(result)

# All Configuration Services
# Get list of configurations
@app.route("/getConfs")
def getConfs():
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()

  sql = "SELECT ID, NAME, CREATION_TIME, DESCRIPTION, OWNER from CONFIGURATION"
  print(sql)
  cursor.execute(sql)
  result = cursor.fetchall()
  cursor.close()
  connection.close()
  print(result)
  return jsonify(result)

# Get particular configuration
@app.route("/getConf")
def getConf():
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()

  sql = "SELECT ID, NAME, CREATION_TIME, DESCRIPTION, OWNER from CONFIGURATION where ID = '{}'".format(request.args.get('id'))
  print(sql)
  cursor.execute(sql)
  result = cursor.fetchone()
  cursor.close()
  connection.close()
  print(result)
  return jsonify(result)

# Create a configuration
@app.route("/createConf", methods = ['POST'])
def createConf():
  print("I am here")
  request_data = request.json
  print(request_data)
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "INSERT INTO CONFIGURATION(NAME,CREATION_TIME,DESCRIPTION,OWNER) VALUES ('{}','{}','{}',{});".format(request_data[0], request_data[1], request_data[2], request_data[3])
  print(sql)
  cursor.execute(sql)
  connection.commit()
  cursor.close()
  connection.close()
  resp = jsonify(success=True, status_code = 200)
  return resp

# Update a particular configuration
@app.route("/setConf", methods = ['POST'])
def setConf():
  print("I am here")
  request_data = request.json
  print(request_data)
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "UPDATE CONFIGURATION SET NAME = '{}', CREATION_TIME = '{}', DESCRIPTION = '{}', OWNER = {} WHERE ID = {}".format(request_data[1], request_data[2], request_data[3], request_data[4], request_data[0])
  print(sql)
  cursor.execute(sql)
  connection.commit()
  cursor.close()
  connection.close()
  resp = jsonify(success=True, status_code = 200)
  return resp

# Remove a particular configuration
@app.route("/deleteConf")
def deleteConf():
  print("I am here")
  request_data = request.json
  print(request_data)
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "DELETE FROM CONFIGURATION WHERE ID = {}".format(request.args.get('id'))
  print(sql)
  cursor.execute(sql)
  connection.commit()
  cursor.close()
  connection.close()
  resp = jsonify(success=True, status_code = 200)
  return resp

if __name__ == '__main__':
  app.run(debug = True)