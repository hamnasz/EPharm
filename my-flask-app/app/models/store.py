class Store(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Store {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location
        }