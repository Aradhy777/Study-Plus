from modules.database_manager import db


class Mark(db.Model):
    __tablename__ = "marks"

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    marks_obtained = db.Column(db.Float, nullable=False)
    total_marks = db.Column(db.Float, nullable=False, default=100.0)
    exam_date = db.Column(db.Date, nullable=False)
    exam_type = db.Column(db.String(50), nullable=False)

    def percentage(self):
        if not self.total_marks or self.total_marks == 0:
            return 0.0
        return round((self.marks_obtained / self.total_marks) * 100, 2)

    def __repr__(self):
        return f"<Mark {self.subject} - {self.percentage()}%>"
