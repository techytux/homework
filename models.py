from app import db

class Rides(db.Model):
    __tablename__ = 'rides'

    ride_id = db.Column(db.Integer, primary_key=True)
    from_stop = db.Column(db.Integer)
    to_stop = db.Column(db.Integer)
    route_id = db.Column(db.Integer)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)
