class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicines.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    user = db.relationship('User', backref=db.backref('reviews', lazy=True))
    medicine = db.relationship('Medicine', backref=db.backref('reviews', lazy=True))

    def __repr__(self):
        return f'<Review {self.id} - User {self.user_id} - Medicine {self.medicine_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'medicine_id': self.medicine_id,
            'content': self.content
        }