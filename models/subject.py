from modules.database_manager import db


class Subject(db.Model):
    __tablename__ = "subjects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    target_hours = db.Column(db.Float, nullable=False, default=10.0)

    def __repr__(self):
        return f"<Subject {self.name}>"
