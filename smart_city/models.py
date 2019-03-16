from smart_city import db

class smart_home_db(db.Model):
    """
    Database model for storing information on commands received from Smart Home. 
    """

    id = db.Column(db.Integer, primary_key=True)
    push_btn_1 = db.Column(db.Boolean)
    push_btn_2 = db.Column(db.Boolean)
    push_btn_3 = db.Column(db.Boolean)
    push_btn_4 = db.Column(db.Boolean)

    def __repr__(self):
        return '<smart_home {}>'.format("database")

    
class smart_hospital_db(db.Model):
    """
    Database model for storing information on commands received from Smart Hospital. 
    """

    id = db.Column(db.Integer, primary_key=True)
    push_btn_1 = db.Column(db.Boolean)
    push_btn_2 = db.Column(db.Boolean)
    push_btn_3 = db.Column(db.Boolean)
    push_btn_4 = db.Column(db.Boolean)

    def __repr__(self):
        return '<smart_hospital {}>'.format("database")

    
class smart_mall_db(db.Model):
    """
    Database model for storing information on commands received from Smart Mall. 
    """

    id = db.Column(db.Integer, primary_key=True)
    push_btn_1 = db.Column(db.Boolean)
    push_btn_2 = db.Column(db.Boolean)
    push_btn_3 = db.Column(db.Boolean)
    push_btn_4 = db.Column(db.Boolean)

    def __repr__(self):
        return '<smart_mall {}>'.format("database")


class smart_school_db(db.Model):
    """
    Database model for storing information on commands received from Smart School. 
    """

    id = db.Column(db.Integer, primary_key=True)
    push_btn_1 = db.Column(db.Boolean)
    push_btn_2 = db.Column(db.Boolean)
    push_btn_3 = db.Column(db.Boolean)
    push_btn_4 = db.Column(db.Boolean)

    def __repr__(self):
        return '<smart_school {}>'.format("database")