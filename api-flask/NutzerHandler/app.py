from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm.attributes import flag_modified
import barcodenumber
import json
import model
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
host = '127.0.0.1'
port = 5001

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

@app.route('/getuserbyname/<username>', methods=['GET'])
def getUserByName(username):
    #TODO: user auth 
    user = model.Nutzer.query.filter_by(username=username).first()
    if not user:
        return jsonify("User not found")
    response = model.nutzerSchema.dump(user)
    return jsonify(nutzer=response)
    
@app.route('/updateuser/<username>', methods=['PUT'])
def updateUser(username):
    data = request.get_json(silent=True)

    #TODO: check auth
    user = model.Nutzer.query.get(username)
    if not user:
        return jsonify("user dont exists")

    if 'weight' not in data:
        data['weight'] = user.weight
    if 'height' not in data:
        data['height'] = user.height
    if 'hashedPassword' not in data:
        data['hashedPassword'] = user.hashedPassword

    user.hashedPassword = data['hashedPassword']
    user.height = data['height']
    user.weight = data['weight']

    flag_modified(user, "hashedPassword")
    flag_modified(user, "height")
    flag_modified(user, "weight")
    db.session.merge(user)
    db.session.flush()
    db.session.commit()
    responese = model.nutzerSchema.dump(user)
    return jsonify(nutzer=responese)
        
@app.route('/createuser', methods=['POST'])
def createUser():
    data = request.get_json(silent=True)

    if 'username' not in data:
        return jsonify("No username")
    if 'weight' not in data:
        data['weight'] = None
    if 'height' not in data:
        data['height'] = None
    if 'hashedPassword' not in data:
        data['hashedPassword'] = None

    #TODO: check if user already exists
    user = model.Nutzer.query.filter_by(username=data['username']).first()
    if user:
        return jsonify("username exists")
    

    newUser = model.Nutzer(username = data['username'],
                        weight = data['weight'],
                        height = data['height'],
                        hashedPassword = data['hashedPassword'])
    
    db.session.add(newUser)
    db.session.commit()
    responese = model.nutzerSchema.dump(newUser)
    return jsonify(nutzer=responese)

@app.route('/authuser/<username>/<userauth>', methods=['GET'])
def authUser(username, userauth):
    #TODO: auth  mechanisim
    return jsonify(auth=True) #dummy true
    
if __name__ == '__main__':
    app.run(host, port)