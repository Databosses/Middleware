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
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "SELECT ID, {} from {}".format(request.args.get('filter'), request.args.get('table'))
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  result = cursor.fetchall()
  cursor.close()
  connection.close()
  print(result)
  return jsonify(result)

@app.route("/getEmpIds")
def getEmpIds():
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "SELECT ID from EMPLOYEE"
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
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
  cursor.execute('PRAGMA foreign_keys = ON;')
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
  cursor.execute('PRAGMA foreign_keys = ON;')
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
  cursor.execute('PRAGMA foreign_keys = ON;')
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
  cursor.execute('PRAGMA foreign_keys = ON;')
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
  cursor.execute('PRAGMA foreign_keys = ON;')
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
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  connection.commit()
  cursor.close()
  connection.close()
  resp = jsonify(success=True, status_code = 200)
  return resp

# All Lot Services
# Get list of lots
@app.route("/getLots")
def getLots():
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "SELECT L.ID, L.NAME, L.MATERIAL_TYPE, L.HEIGHT, L.DIAMETER, L.CONFIGURATION, LO.CITY, L.ASSIGNEE, E.FIRSTNAME from LOT as L INNER JOIN LOCATION AS LO ON L.LOC_ID = LO.ID INNER JOIN EMPLOYEE E ON L.ASSIGNEE = E.ID;"
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  result = cursor.fetchall()
  cursor.close()
  connection.close()
  print(result)
  return jsonify(result)

# Get particular lot
@app.route("/getLot")
def getLot():
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "SELECT ID, NAME, MATERIAL_TYPE, HEIGHT, DIAMETER, CONFIGURATION, LOC_ID, ASSIGNEE from LOT where ID = '{}'".format(request.args.get('id'))
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  result = cursor.fetchone()
  cursor.close()
  connection.close()
  print(result)
  return jsonify(result)

# Create a lot
@app.route("/createLot", methods = ['POST'])
def createLot():
  print("I am here")
  request_data = request.json
  print(request_data)
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "INSERT INTO LOT(NAME,MATERIAL_TYPE,HEIGHT,DIAMETER,CONFIGURATION,LOC_ID,ASSIGNEE) VALUES ('{}','{}','{}',{},'{}','{}','{}');".format(request_data[0], request_data[1], request_data[2], request_data[3], request_data[4], request_data[5], request_data[6])
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  connection.commit()
  cursor.close()
  connection.close()
  resp = jsonify(success=True, status_code = 200)
  return resp

# Update a particular configuration
@app.route("/setLot", methods = ['POST'])
def setLot():
  print("I am here")
  request_data = request.json
  print(request_data)
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "UPDATE LOT SET NAME = '{}', MATERIAL_TYPE = '{}', HEIGHT = {}, DIAMETER = {}, CONFIGURATION = {}, LOC_ID = {}, ASSIGNEE = {} WHERE ID = {}".format(request_data[1], request_data[2], request_data[3], request_data[4], request_data[5], request_data[6], request_data[7], request_data[0])
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  connection.commit()
  cursor.close()
  connection.close()
  resp = jsonify(success=True, status_code = 200)
  return resp

# Remove a particular configuration
@app.route("/delete")
def deleteLot():
  print("I am here")
  request_data = request.json
  print(request_data)
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "DELETE FROM {} WHERE ID = {}".format(request.args.get('table'), request.args.get('id'))
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  connection.commit()
  cursor.close()
  connection.close()
  resp = jsonify(success=True, status_code = 200)
  return resp

# Get particular lot
@app.route("/getLotVisualization")
def getLotVisualization():
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "select PART_DEFECT.SEVERITY, count(*) from lot inner join PART on lot.id = PART.lot inner join PART_DEFECT on PART.id = PART_DEFECT.part_id where lot.id = {} group by (PART_DEFECT.SEVERITY);".format(request.args.get('id'))
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  result = cursor.fetchall()
  cursor.close()
  connection.close()
  print(result)
  return jsonify(result)

##################################Surbhi

#Get all parts
@app.route("/getParts")
def getLotParts():
  #lotId = request.args.get("lotId")
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "select * from part " #where lot = '{}'".format(lotId)
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  result = cursor.fetchall()
  print(result)
  cursor.close()
  connection.close()
  return jsonify(result)

#Insert a part
@app.route("/addPart", methods = ['POST'])
def insertPart():
  data = request.json
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = 'INSERT INTO PART (TEST_START_TIME,TEST_END_TIME,BUCKET,LOT) VALUES ({},{},{},{});'.format(data[0], data[1], data[2], data[3])
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  connection.commit() 
  print("inserted")
  cursor.close()
  connection.close()
  return jsonify(success=True, status_code = 200)

# Update a part
@app.route("/updatePart", methods = ['POST'])
def updatePart():
  data = request.json
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "UPDATE PART SET TEST_START_TIME = '{}', TEST_END_TIME = '{}', BUCKET = '{}', LOT = '{}' WHERE ID = '{}';".format(data[0], data[1], data[2], data[3], data[4])
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  connection.commit() 
  print("inserted")
  cursor.close()
  connection.close()
  return jsonify(success=True, status_code = 200)

# Delete a Part
@app.route("/deletePart", methods = ['DELETE'])
def deletePart():
  partId = request.args.get("partId")
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "DELETE FROM PART WHERE ID = {}".format(partId)
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  connection.commit()
  cursor.close()
  connection.close()
  resp = jsonify(success=True, status_code = 200)
  return resp

#Get all parts-defects
@app.route("/getPartDefects")
def getPartDefects():
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "Select defect_id, type, part_id, severity, defect_count from Defect d, part p, part_defect pd where d.id = pd.defect_id and p.id = pd.part_id;"
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  result = cursor.fetchall()
  print(result)
  cursor.close()
  connection.close()
  return jsonify(result)

#Insert a part defect
@app.route("/addPartDefect", methods = ['POST'])
def insertPartDefect():
  data = request.json
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = 'INSERT INTO PART_DEFECT (DEFECT_ID, PART_ID, SEVERITY, DEFECT_COUNT) VALUES ({},{},{},{});'.format(data[0], data[1], data[2], data[3])
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  connection.commit() 
  print("inserted")
  cursor.close()
  connection.close()
  return jsonify(success=True, status_code = 200)

# Update part-defect
@app.route("/updatePartDefect", methods = ['POST'])
def updatePartDefect():
  data = request.json
  print(data)
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "UPDATE PART_DEFECT SET DEFECT_ID = '{}', SEVERITY = '{}',  DEFECT_COUNT = '{}' WHERE PART_ID = {}".format(data[0], data[2], data[3], data[1])
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  connection.commit() 
  print("inserted")
  cursor.close()
  connection.close()
  return jsonify(success=True, status_code = 200)

# Delete a Part-defect
@app.route("/deletePartDefect", methods = ['DELETE'])
def deletePartDefect():
  partId = request.args.get("partId")
  defectId = request.args.get("defectId")
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "DELETE FROM PART_DEFECT WHERE PART_ID = {} AND DEFECT_ID= {}".format(partId, defectId)
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  connection.commit()
  cursor.close()
  connection.close()
  resp = jsonify(success=True, status_code = 200)
  return resp

#Get details of a defectId
@app.route("/getDefectDetails")
def getDefectsDetails():
  defectId = request.args.get("defectId")
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "select d.id, ds.depth, ds.aspect_ratio, dh.diameter, dh.circular_ratio, dd.actual_diameter, dd.actual_height from defect as d left outer join defect_scratch as ds on d.id = ds.defect_id left outer join defect_hole as dh on d.id = dh.defect_id left outer join defect_dimension_error as dd on d.id = dd.defect_id where d.id = {}".format(defectId)
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  result = cursor.fetchall()
  print(result)
  cursor.close()
  connection.close()
  return jsonify(result)

#Get all defects all details
@app.route("/getAllDefectDetails")
def getAllDefectsDetails():
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "select d.id, ds.depth, ds.aspect_ratio, dh.diameter, dh.circular_ratio, dd.actual_diameter, dd.actual_height from defect as d left outer join defect_scratch as ds on d.id = ds.defect_id left outer join defect_hole as dh on d.id = dh.defect_id left outer join defect_dimension_error as dd on d.id = dd.defect_id"
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  result = cursor.fetchall()
  print(result)
  cursor.close()
  connection.close()
  return jsonify(result)  


#Get all defects all details
@app.route("/getAllDefectDetails1")
def getAllDefectsDetails1():
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "select d.id, ds.depth, ds.aspect_ratio, dh.diameter, dh.circular_ratio, dd.actual_diameter, dd.actual_height, d.type from defect as d left outer join defect_scratch as ds on d.id = ds.defect_id left outer join defect_hole as dh on d.id = dh.defect_id left outer join defect_dimension_error as dd on d.id = dd.defect_id"
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  result = cursor.fetchall()
  print(result)
  cursor.close()
  connection.close()
  return jsonify(result)  

#Get defects
@app.route("/getDefects")
def getDefects():
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "SELECT * FROM  DEFECT"
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  result = cursor.fetchall()
  print(result)
  cursor.close()
  connection.close()
  return jsonify(result)  

#Get Lot Ids
@app.route("/getLotIds")
def getLotIds():
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "SELECT DISTINCT(ID) FROM  LOT"
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  result = cursor.fetchall()
  print(result)
  cursor.close()
  connection.close()
  return jsonify(result)  

#Insert a scratch defect
@app.route("/addScratchDefect", methods = ['POST'])
def addScratchDefect():
  data = request.json
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = 'INSERT INTO DEFECT (ID, TYPE) VALUES ({},{});'.format(data[0], data[1])
  sql1 = "INSERT INTO DEFECT_SCRATCH (DEFECT_ID, DEPTH, ASPECT_RATIO) VALUES({},{},{})".format(data[0], data[2], data[3])
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  cursor.execute(sql1)
  connection.commit() 
  print("inserted")
  cursor.close()
  connection.close()
  return jsonify(success=True, status_code = 200)

  #Insert a hole defect
@app.route("/addHoleDefect", methods = ['POST'])
def addHoleDefect():
  data = request.json
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = 'INSERT INTO DEFECT (ID, TYPE) VALUES ({},{});'.format(data[0], data[1])
  sql1 = "INSERT INTO DEFECT_HOLE (DEFECT_ID, DIAMETER, CIRCULAR_RATIO) VALUES({},{},{})".format(data[0], data[2], data[3])
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  cursor.execute(sql1)
  connection.commit() 
  print("inserted")
  cursor.close()
  connection.close()
  return jsonify(success=True, status_code = 200)

  #Insert a dim-err defect
@app.route("/addDimErrDefect", methods = ['POST'])
def addDimErrDefect():
  data = request.json
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = 'INSERT INTO DEFECT (ID, TYPE) VALUES ({},{});'.format(data[0], data[1])
  sql1 = "INSERT INTO DEFECT_DIMENSION_ERROR (DEFECT_ID, ACTUAL_DIAMETER ,ACTUAL_HEIGHT) VALUES({},{},{})".format(data[0], data[2], data[3])
  print(sql)
  print(sql1)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  cursor.execute(sql1)
  connection.commit() 
  print("inserted")
  cursor.close()
  connection.close()
  return jsonify(success=True, status_code = 200)


# Update a scratch defect
@app.route("/updateScratchDefect", methods = ['POST'])
def updateScratchDefect():
  data = request.json
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "UPDATE DEFECT SET TYPE = {} where ID = {}".format(data[1], data[0])
  sql1 = "DELETE FROM DEFECT_SCRATCH where DEFECT_ID = {}".format(data[0])
  sql2 = "DELETE FROM DEFECT_HOLE where DEFECT_ID = {}".format(data[0])
  sql3 = "DELETE FROM DEFECT_DIMENSION_ERROR where DEFECT_ID = {}".format(data[0])
  sql4 = "INSERT INTO DEFECT_SCRATCH (DEFECT_ID, DEPTH, ASPECT_RATIO) VALUES({},{},{})".format(data[0], data[2], data[3])
  #sql2 = "UPDATE DEFECT_SCRATCH SET DEPTH = {}, ASPECT_RATIO = {} where DEFECT_ID={}".format( data[2], data[3], data[0])
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  cursor.execute(sql1)
  cursor.execute(sql2)
  cursor.execute(sql3)
  cursor.execute(sql4)
  connection.commit() 
  print("inserted")
  cursor.close()
  connection.close()
  return jsonify(success=True, status_code = 200)


  # Update a hole defect
@app.route("/updateHoleDefect", methods = ['POST'])
def updateHoleDefect():
  data = request.json
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "UPDATE DEFECT SET TYPE = {} where ID = {}".format(data[1], data[0])
  sql1 = "DELETE FROM DEFECT_SCRATCH where DEFECT_ID = {}".format(data[0])
  sql2 = "DELETE FROM DEFECT_HOLE where DEFECT_ID = {}".format(data[0])
  sql3 = "DELETE FROM DEFECT_DIMENSION_ERROR where DEFECT_ID = {}".format(data[0])
  sql4 = "INSERT INTO DEFECT_HOLE (DEFECT_ID, DIAMETER, CIRCULAR_RATIO) VALUES({},{},{})".format(data[0], data[2], data[3])
  print(sql)
  print(sql1)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  cursor.execute(sql1)
  cursor.execute(sql2)
  cursor.execute(sql3)
  cursor.execute(sql4)
  connection.commit() 
  print("inserted")
  cursor.close()
  connection.close()
  return jsonify(success=True, status_code = 200)


  # Update a dim_err defect
@app.route("/updateDimErrDefect", methods = ['POST'])
def updateDimErrDefect():
  data = request.json
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "UPDATE DEFECT SET TYPE = {} where ID = {}".format(data[1], data[0])
  sql1 = "DELETE FROM DEFECT_SCRATCH where DEFECT_ID = {}".format(data[0])
  sql2 = "DELETE FROM DEFECT_HOLE where DEFECT_ID = {}".format(data[0])
  sql3 = "DELETE FROM DEFECT_DIMENSION_ERROR where DEFECT_ID = {}".format(data[0])
  sql4 = "INSERT INTO DEFECT_DIMENSION_ERROR (DEFECT_ID, ACTUAL_DIAMETER ,ACTUAL_HEIGHT) VALUES({},{},{})".format(data[0], data[2], data[3])
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  cursor.execute(sql1)
  cursor.execute(sql2)
  cursor.execute(sql3)
  cursor.execute(sql4)
  connection.commit() 
  print("inserted")
  cursor.close()
  connection.close()
  return jsonify(success=True, status_code = 200)


  # Delete a Part
@app.route("/deleteDefect", methods = ['DELETE'])
def deleteDefect():
  defectId = request.args.get("defectId")
  connection = sqlite3.connect(app.config['CONNECTION'])
  cursor = connection.cursor()
  sql = "DELETE FROM DEFECT WHERE ID = {}".format(defectId)
  print(sql)
  cursor.execute('PRAGMA foreign_keys = ON;')
  cursor.execute(sql)
  connection.commit()
  cursor.close()
  connection.close()
  resp = jsonify(success=True, status_code = 200)
  return resp


##################################

if __name__ == '__main__':
  app.run(debug = True)