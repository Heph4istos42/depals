from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

#configurate Database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://user:pw@server/db" #TODO: db config data
#mysql = MySQL(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
db.create_all()

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

lebensmitelTags = db.Table('lebensmitel_tags',
    db.Column('tagid', db.Integer, db.ForeignKey('tag.tagid'), primary_key=True),
    db.Column('barcodeid', db.Integer, db.ForeignKey('lebensmittel.barcodeid'), primary_key=True)
)

class Tag(db.Model):    
    tagid = db.Column(db.Integer, primary_key=True)
    beschreibung = db.Column(db.String(255))
    
    def __init__(self, tagid, beschreibung):
        self.tagid = tagid
        self.beschreibung = beschreibung

connectedLebensmittel = db.Table('lebensmittel_lebensmittel',
    db.Column('lebensmittel1', db.Integer, db.ForeignKey('lebensmittel.barcodeid'), primary_key=True),
    db.Column('lebensmittel2', db.Integer, db.ForeignKey('lebensmittel.barcodeid'), primary_key=True)
)

class Lebensmittel(db.Model):    
    barcodeid = db.Column(db.String(255), primary_key=True)
    bezeichnung = db.Column(db.String(255))
    kcal = db.Column(db.Integer(255))
    contains = db.Column(db.String(512)) #TODO: langer String oder extra Table 
    fat = db.Column(db.Integer)
    carbohydrates = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    ampelindikator = db.Column(db.Integer)
    andereLebensmittel = db.relationship("Lebensmittel",
                               secondary=connectedLebensmittel)
    tagOfLebensmittel = db.relationship("Tag",
                               secondary=connectelebensmitelTagsdLebensmittel)
            
    def __init__(self, barcodeid, bezeichnung, kcal, contains, fat, carbohydrates, protein, ampelindikator):
        self.barcodeid = barcodeid
        self.bezeichnung = bezeichnung
        self.kcal = kcal
        self.contains = contains
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein
        self.ampelindikator = ampelindikator

planLebensmittel = db.Table('plan_lebensmittel',
    db.Column('plan', db.Integer, db.ForeignKey('plan.planid'), primary_key=True),
    db.Column('lebensmittel', db.Integer, db.ForeignKey('lebensmittel.barcodeid'), primary_key=True)
)

class Plan(db.Model):    
    planid = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    stars = db.Column(db.Integer)
    lebensmittelOfPlan = db.relationship("Lebensmittel",
                    secondary=planLebensmittel)

    def __init__(self, planid, comment, stars):
        self.planid = planid
        self.comment = comment
        self.stars = stars

class Nutzer(db.Model):    
    username = db.Column(db.String(255), primary_key=True)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    #hashedpassword = db.Column(db.String(255), nullable=False)
    #authCookie = db.Column(db.String(255), nullable=False)
    
    def __init__(self, username, weight, height):
        self.username = username
        self.weight = weight
        self.height  = height 

class NutzerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Nutzer
        
class PlanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Plan

class LebensmittelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Lebensmittel

nutzerSchema = NutzerSchema()
nutzersSchema = NutzerSchema(many=True)

planSchema = PlanSchema()
plansSchema = PlanSchema(many=True)

lebensmittelSchema = LebensmittelSchema()
lebensmittelsSchema = LebensmittelSchema(many=True)

# sanity check route
@app.route('/help', methods=['GET'])
def ping_pong():
    return jsonify('/help')

@app.route('/getlebensmittelbyinput/<input>', methods=['GET'])
def getlebensmittelbyinput(input):
    #check if input id
        #datensatz beziehen 
    #check if input text 
        #datensätze beziehen 
    #todoList = Todoevent.query.all()
    return jsonify('/getlebensmittelbyinput/<input>') #todoeventsSchema.dump(todoList))

def getAmpelindikatorByUserdata(username, barcodeid):
    #verrückten Algo überlegen 
    return ""


@app.route('/addtoplan/<planid>/<barcodeid>', methods=['PUT'])
def addToPlan(planid, barcodeid):
    #add barcode id to plan 
    return jsonify()# return plan

@app.route('/createnewplan/<username>', methods=['POST'])
def createNewPlan(username):
    #create new plan 
    return jsonify()# return new plan

@app.route('/getplansbyuser/<username>', methods=['GET'])
def getPlanByUser(username):
    #check auth 
    #get plans
    return jsonify()# return plans

@app.route('/getPlanById/<planid>', methods=['GET'])
def getPlanByUser(planid):
    #check auth 
    #get plan by id
    return jsonify()# return plan

@app.route('/setStartsandComments/<planid>', methods=['POST'])
def getPlanByUser(planid):
    #check auth 
    #get request body data
    #set plan
    return jsonify()# return plan

@app.route('/deleteplan/<planid>', methods=['DELETE'])
def deletePlan(planid):
    #check auth 
    #kill this shit
    return jsonify()# return mt

@app.route('/removefromplan/<planid>/<barcodeid>', methods=['PUT'])
def removeFromPlan(planid, barcodeid):
    #auth
    #check if item in plan 
    #remove item from plan  
    return jsonify()# return plan


@app.route('/updateuser', methods=['PUT'])
def updateUser():
    #get request data 
    #auth 
    #change data
    return jsonify()# return user
    
@app.route('/createuser', methods=['POST'])
def createUser():
    #get request data 
    #auth 
    #create user
    return jsonify()# return user

@app.route('/authuser', methods=['GET'])
def authUser():
    #get request data 
    #auth 
    return jsonify()# return true if auth
    
if __name__ == '__main__':
    app.run()