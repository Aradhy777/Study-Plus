from modules.database_manager import db


class StudySession(db.Model):
	__tablename__ = "study_sessions"

	id = db.Column(db.Integer, primary_key=True)
	subject = db.Column(db.String(100), nullable=False)
	study_date = db.Column(db.Date, nullable=False)
	duration_minutes = db.Column(db.Integer, nullable=False)
	marks = db.Column(db.Float, nullable=True)
