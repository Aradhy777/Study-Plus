from modules.database_manager import db


class StudySession(db.Model):
	__tablename__ = "study_sessions"

	id = db.Column(db.Integer, primary_key=True)
	subject = db.Column(db.String(100), nullable=False)
	date = db.Column(db.Date, nullable=False)
	duration = db.Column(db.Integer, nullable=False)
	productivity = db.Column(db.Float, nullable=True)

	def __repr__(self):
		return f"<StudySession {self.subject} on {self.date}>"
