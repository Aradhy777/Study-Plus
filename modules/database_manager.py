from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def add_subject(name, target_hours=10.0):
	from models.subject import Subject
	subject = Subject(name=name, target_hours=target_hours)
	db.session.add(subject)
	db.session.commit()
	return subject


def add_session(subject, date, duration, productivity=None):
	from models.session import StudySession
	session = StudySession(
		subject=subject,
		date=date,
		duration=duration,
		productivity=productivity
	)
	db.session.add(session)
	db.session.commit()
	return session


def add_mark(subject, marks_obtained, total_marks, exam_date, exam_type):
	from models.marks import Mark
	mark = Mark(
		subject=subject,
		marks_obtained=marks_obtained,
		total_marks=total_marks,
		exam_date=exam_date,
		exam_type=exam_type
	)
	db.session.add(mark)
	db.session.commit()
	return mark


def get_all_subjects():
	from models.subject import Subject
	return Subject.query.all()


def get_all_sessions():
	from models.session import StudySession
	return StudySession.query.all()


def get_all_marks():
	from models.marks import Mark
	return Mark.query.all()


def get_sessions_by_subject(subject):
	from models.session import StudySession
	return StudySession.query.filter_by(subject=subject).all()


def get_marks_by_subject(subject):
	from models.marks import Mark
	return Mark.query.filter_by(subject=subject).all()


def delete_subject(subject_id):
	from models.subject import Subject
	subject = Subject.query.get(subject_id)
	if subject:
		db.session.delete(subject)
		db.session.commit()
		return True
	return False


def delete_session(session_id):
	from models.session import StudySession
	session = StudySession.query.get(session_id)
	if session:
		db.session.delete(session)
		db.session.commit()
		return True
	return False


def delete_mark(mark_id):
	from models.marks import Mark
	mark = Mark.query.get(mark_id)
	if mark:
		db.session.delete(mark)
		db.session.commit()
		return True
	return False
