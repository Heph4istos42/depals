from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

lebensmitelTags = db.Table('tag_has_lebensmitel',
    db.Column('Tag_tagID', db.Integer, db.ForeignKey('tag.tagID'), primary_key=True, nullable=False),
    db.Column('Lebensmittel_barcodeID', db.Integer, db.ForeignKey('lebensmittel.barcodeID'), primary_key=True, nullable=False)
)

class Tag(db.Model):    
    tagID = db.Column(db.Integer, primary_key=True, nullable=False)
    beschreibung = db.Column(db.String(50), nullable=False)
    
    def __init__(self, tagID, beschreibung):
        self.tagID = tagID
        self.beschreibung = beschreibung

connectedLebensmittel = db.Table('lebensmittel_has_lebensmittel',
    db.Column('Lebensmittel_barcodeID', db.String(50), db.ForeignKey('lebensmittel.barcodeID'), primary_key=True),
    db.Column('Lebensmittel_barcodeID1', db.String(50), db.ForeignKey('lebensmittel.barcodeID'), primary_key=True)
)

class Lebensmittel(db.Model):    
    barcodeID = db.Column(db.String(50), primary_key=True, nullable=False)
    bezeichnung = db.Column(db.String(50), nullable=False)
    img = db.Column(db.String(100))
    kcal = db.Column(db.Integer)
    contains = db.Column(db.String(500))
    fat = db.Column(db.Integer)
    carbohydrates = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    #lebensmittel_id = db.Column(db.String(50), db.ForeignKey('lebensmittel.barcodeID'))
    # mainLebensmittel = db.Column(db.String(50), db.ForeignKey('lebensmittel_has_lebensmittel.Lebensmittel_barcodeID')) 
    # #andereLebensmittel = db.relation('Lebensmittel', remote_side=[barcodeID], uselist=True)
    # andereLebensmittel = db.relationship("Lebensmittel",
    #                             secondary=connectedLebensmittel, remote_side='Lebensmittel.barcodeID',
    #                             backref=db.backref('lebensmittel_has_lebensmittel'))
    tagOfLebensmittel = db.relationship("Tag",
                               secondary=lebensmitelTags)
            
    def __init__(self, barcodeID, bezeichnung, img, kcal, contains, fat, carbohydrates, protein):
        self.barcodeID = barcodeID
        self.bezeichnung = bezeichnung
        self.img = img
        self.kcal = kcal
        self.contains = contains
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein

planLebensmittel = db.Table('lebensmittel_has_plan',
    db.Column('plan', db.Integer, db.ForeignKey('plan.planID'), primary_key=True),
    db.Column('lebensmittel', db.String(50), db.ForeignKey('lebensmittel.barcodeID'), primary_key=True)
)

class Plan(db.Model):    
    planID = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(400))
    stars = db.Column(db.Integer)
    userName = db.Column(db.String(100), db.ForeignKey('nutzer.username'), primary_key=True)
    lebensmittelOfPlan = db.relationship("Lebensmittel",
                    secondary=planLebensmittel)

    def __init__(self, planID, comment, stars, userName):
        self.planID = planID
        self.comment = comment
        self.stars = stars
        self.userName = userName

class Nutzer(db.Model):    
    username = db.Column(db.String(100), primary_key=True, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    hashedPassword = db.Column(db.String(450))
    authCookie = db.Column(db.String(100))
    
    def __init__(self, username, weight, height, hashedPassword):
        self.username = username
        self.weight = weight
        self.height  = height 
        self.hashedPassword = hashedPassword

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