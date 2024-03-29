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
port = 5002

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#configurate Database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:pw@127.0.0.1/depals" 

db = SQLAlchemy(app)
ma = Marshmallow(app)
db.create_all()

@app.route('/', methods=['GET'])
@app.route('/help', methods=['GET'])
def ping_pong():
    return jsonify('/help')

@app.route('/addtoplan/<planid>/<username>/<barcodeid>', methods=['PUT'])
def addToPlan(planid, username, barcodeid):
    
    #add barcode id to plan 
    try:
        plan = model.Plan.query.filter_by(planID=planid, userName=username).first()
        print(planid)
        print(username)
        print(plan)
        lebensmittel = model.Lebensmittel.query.filter_by(barcodeID=barcodeid).first()
        print(lebensmittel)
        plan.lebensmittelOfPlan.append(lebensmittel)
        db.session.add()
        db.session.commit()
    except Exception as err:
        raise err
    finally:
        cleanup(db.session)

    return jsonify()# return plan

@app.route('/createnewplan/<username>', methods=['POST'])
def createNewPlan(username):
    newPlan = model.Plan(comment = None,
                        stars = None,
                        userName = username)
    try:                                                
        db.session.add(newPlan)
        db.session.commit()
        plan = model.Plan.query.filter_by(userName=username).all()
        res = model.plansSchema.dump(plan)
    except Exception as err:
        raise err
    finally:
        cleanup(db.session)
    return jsonify(planList=res)

@app.route('/getplansbyuser/<username>', methods=['GET'])
def getPlanByUser(username):
    try:
        plans = model.Plan.query.all()
        planlist = model.plansSchema.dump(plans)
    except Exception as err:
        raise err
    finally:
        cleanup(db.session)
    return jsonify(planlist=planlist)

@app.route('/getplanbyidsnduser/<planid>/<username>', methods=['GET'])
def getPlanByIdAndUser(planid):
    try:
        plan = model.Plan.query.filter_by(planID=planid, userName=username).first()
        response = model.planSchema.dump(plan)
    except Exception as err:
        raise err
    finally:
        cleanup(db.session)
    return jsonify(plan=response)

@app.route('/setstarsandcomments/<planid>/<username>', methods=['PUT'])
def setStarsandCommentsOfPlan(planid, username):
    data = request.get_json(silent=True)

    #TODO: check auth
    try:
        plan = model.Plan.query.filter_by(planID=planid, userName=username).first()
    except Exception as err:
        raise err
    finally:
        cleanup(db.session)

    if not plan:
        return jsonify("plan dont exists")

    if 'stars' not in data:
        data['stars'] = plan.stars
    if 'comment' not in data:
        data['comment'] = plan.comment

    plan.stars = data['stars']
    plan.comment = data['comment']

    try:
        flag_modified(plan, "stars")
        flag_modified(plan, "comment")
        db.session.merge(plan)
        db.session.flush()
        db.session.commit()
        responese = model.planSchema.dump(plan)
    except Exception as err:
        raise err
    finally:
        cleanup(db.session)

    return jsonify(plan=responese)

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

def cleanup(session):
    session.close() 
    engine_container = db.get_engine(app)
    engine_container.dispose()

if __name__ == '__main__':
    app.run(host, port)
