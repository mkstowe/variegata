from data import db


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.Integer, db.ForeignKey('action.id'))
    prev_event = db.Column(db.Integer, db.ForeignKey('event.id'))
    text = db.Column(db.String)

    def __repr__(self):
        return f"Event {self.id} \n {self.text}"


class Action(db.Model):
    __tablename__ = 'action'
    id = db.Column(db.Integer, primary_key=True)
    prev_event = db.Column(db.Integer, db.ForeignKey('event.id'))
    next_event = db.Column(db.Integer, db.ForeignKey('event.id'))
    text = db.Column(db.String)

    def __repr__(self):
        return f"Action {self.id} \n Came from: {self.prev_event} \t Leads to: {self.next_event} \n {self.text}"


class Keyword(db.Model):
    __tablename__ = 'keyword'



actions = db.Table('actions',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
)
