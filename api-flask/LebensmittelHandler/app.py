from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm.attributes import flag_modified
import barcodenumber
import requests
import json
import model

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
host = '127.0.0.1'
port = 5000

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#configurate Database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Weinflasche0815@127.0.0.1/depals" 

db = SQLAlchemy(app)
ma = Marshmallow(app)
db.create_all()

@app.route('/', methods=['GET'])
@app.route('/help', methods=['GET'])
def ping_pong():
    return jsonify('/help')

#TODO: Test Endpoint to get a list 
@app.route('/getalllebensmittel', methods=['GET'])
def getlebensmittel():
    lebensmittelList = model.Lebensmittel.query.all()
    response = model.lebensmittelsSchema.dump(lebensmittelList)
    return jsonify(lebensmittel=response)

@app.route('/getlebensmittelbyinput/<input>/<username>', methods=['GET'])
def getlebensmittelbyinput(input, username):
    if barcodenumber.check_code('ean13', input):
        lebensmittelList = model.Lebensmittel.query.filter_by(barcodeID=input).all()
        response = model.lebensmittelsSchema.dump(lebensmittelList)
        ampelindikator = getAmpelindikatorByUserdata(username, input) #TODO: userbeziehen TODO: indikator richtig im response verbauen
        response.append(ampelindikator)
        return jsonify(lebensmittel=response, ampelindikator=ampelindikator)    
    else:
        lebensmittelList = model.Lebensmittel.query.filter_by(bezeichnung=input).all() #TODO: Suchalog implementieren
        response = model.lebensmittelsSchema.dump(lebensmittelList)
        return jsonify(response)

def getAmpelindikatorByUserdata(username, barcodeid):
    url = 'http://127.0.0.1:5001/getuserbyname/' + username
    print(url)
    response = requests.get(url).text
    nutzerData = json.loads(response)
    print(nutzerData['nutzer'])
    user = model.nutzerSchema.dump(nutzerData['nutzer'])
    userWeight = user['weight']
    userHeight = user['height']
    #TODO: verrückten Algo überlegen 
    return int((userWeight+userHeight)%3)

if __name__ == '__main__':
    app.run(host, port)