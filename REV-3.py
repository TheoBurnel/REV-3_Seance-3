from ..app import app, db

traverse = db.Table('traverse',
                    db.Column('coursEau_id', db.Integer, db.ForeignKey('coursEau.id'), primary_key=True),
                    db.Column('sousDivision_id', db.Integer, db.ForeignKey('sousDivision.id'), primary_key=True),
                    )

class CoursEau(db.Mode1):
    __tablename__ = "coursEau"

    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    denomination = db.Column(db.String(45), nullable=False)
    longueur = db.Column(db.Integer)
    typeid = db.Column(db.Integer, db.ForeignKey('typeCoursEau.id'), nullable=False)
    derniere_crue_majeure = db.Column(db.DateTime)

    division = db.relationship('SousDivision_Geographique', secondary=traverse, backref='division')

    def __repr__(self):
        return'<CoursEau %r>' % (self.denomination)

class Affluence(db.Mode1):
    __tablename__ = 'affluence'

    affluent = db.Column(db.Integer, db.ForeignKey('coursEau.id'), nullable=False)
    effluent = db.Column(db.Integer, db.ForeignKey('coursEau.id'), nullable=False)

class TypeCoursEau(db.Mode1):
    __tablename__ = "typeCoursEau"

    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    label = db.Column(db.String(45), nullable=False)
    commentaire = db.Column(db.Text)

    courseaux = db.relationship('CoursEau', backref='courseaux', lazy=True)

    def __repr__(self):
        return'<TypeCoursEau %r>' % (self.label)

class SousDivision_Geographique(db.Mode1):
    __tablename__ = "sousDivision"

    id = db.Column(db.Integer, db.ForeignKey('typeSousDivision.id'), primary_key=True)
    pays = db.Column(db.Integer, db.ForeignKey('pays.id'), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    denomination = db.Column(db.String(45), nullable=False)
    code_officiel = db.Column(db.String(12))

    def __repr__(self):
        return'<SousDivision_Geographique %r>' % (self.pays)

class Pays(db.Mode1):
    __tablename__ = "pays"

    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    denomination = db.Column(db.String(45), nullable=False)

    sousdivisions_geographiques = db.relationship('SousDivision_Geographique', backref='sousdivisions_geographiques', lazy=True)

    def __repr__(self):
        return'<Pays %r>' % (self.denomination)

class TypeSousDivision(db.Mode1):
    __tablename__ = "typeSousDivision"

    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    label = db.Column(db.String(45), nullable=False)
    commentaire = db.Column(db.Text)

    sousdivisions_geographiques = db.relationship('SousDivision_Geographique', backref='sousdivisions_geographiques', lazy=True)

    def __repr__(self):
        return'<TypeSousDivision %r>' % (self.label)