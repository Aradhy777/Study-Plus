from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from models.session import StudySession


db = SQLAlchemy()


# subject add karne ka function
def add_subject(subject_name):
    """Simple function to track a subject name."""
    # Yahan pe subject ko session ke through add karte hain
    # Real implementation mein alag Subject table banate
    pass


def add_session(subject, date, duration, productivity=None):
	"""Study session ko database mein save karne ke liye."""
	session = StudySession(
		subject=subject,
		date=date,
		duration=duration,
		productivity=productivity
	)
	db.session.add(session)
	db.session.commit()
	return session


def add_marks(session_id, productivity):
	"""Productivity score update karne ka simple function."""
	session = StudySession.query.get(session_id)
	if session:
		session.productivity = productivity
		db.session.commit()
		return session
	return None


def get_all_sessions():
	"""Saare study sessions ko fetch karna."""
	return StudySession.query.all()


def get_sessions_by_subject(subject):
	"""Kisi particular subject ke sessions nikaalne ke liye."""
	return StudySession.query.filter_by(subject=subject).all()


def get_total_study_hours():
	"""Total padhai ke ghante calculate karna."""
	sessions = StudySession.query.all()
	total_minutes = sum(s.duration for s in sessions)
    return total_minutes / 60


def delete_session(session_id):
    """Koi session delete karna padhe toh."""
    session = StudySession.query.get(session_id)
    if session:
        db.session.delete(session)
        db.session.commit()
        return True
    return False
