import json
import configparser

# Test if the application 
def test_index(app, client):
  res = client.get('/')
  assert res.status_code == 200
  expected = {'message': 'Application Started'}
  assert expected == json.loads(res.get_data(as_text=True))

# Test if dbPath is valid
def test_db_path(app, client):
  config = configparser.RawConfigParser()
  config.read('db.conf')
  configDict = dict(config.items('DB_DETAILS'))
  res = client.get('/getDBPath')
  assert res.status_code == 200
  expected = {'dbPath': configDict['path']}
  assert expected == json.loads(res.get_data(as_text=True))