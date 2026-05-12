import pandas as pd
import numpy as np

from models.session import StudySession
from models.subject import Subject


def get_total_study_hours():
	"""Saare sessions ka total time nikalna."""
	sessions = StudySession.query.all()
	if not sessions:
		return 0
	total_minutes = sum(s.duration for s in sessions)
	return round(total_minutes / 60, 2)


def get_average_productivity():
	"""Average productivity score nikalna."""
	sessions = StudySession.query.all()
	if not sessions:
		return 0
	
	productivity_scores = [s.productivity for s in sessions if s.productivity is not None]
	if not productivity_scores:
		return 0
	
	return round(np.mean(productivity_scores), 2)


def get_weak_subjects():
	"""Weak subject nikalne ka logic - jo subjects mein kam padhai hoi hai."""
	subjects = Subject.query.all()
	if not subjects:
		return []
	
	weak = []
	for subject in subjects:
		sessions = StudySession.query.filter_by(subject=subject.name).all()
		total_hours = sum(s.duration for s in sessions) / 60
		
		if total_hours < subject.target_hours:
			weak.append({
				'name': subject.name,
				'studied': round(total_hours, 2),
				'target': subject.target_hours
			})
	
	return sorted(weak, key=lambda x: x['studied'])


def get_productivity_by_subject():
	"""Subject-wise average productivity."""
	sessions = StudySession.query.all()
	if not sessions:
		return {}
	
	data = {
		'subject': [s.subject for s in sessions],
		'productivity': [s.productivity for s in sessions if s.productivity is not None]
	}
	
	df = pd.DataFrame(data)
	if df.empty:
		return {}
	
	result = df.groupby('subject')['productivity'].mean().round(2).to_dict()
	return result


def get_study_hours_by_subject():
	"""Kaunsa subject pe kitna time laga."""
	sessions = StudySession.query.all()
	if not sessions:
		return {}
	
	subject_hours = {}
	for session in sessions:
		hours = session.duration / 60
		if session.subject not in subject_hours:
			subject_hours[session.subject] = 0
		subject_hours[session.subject] += hours
	
	return {k: round(v, 2) for k, v in subject_hours.items()}


def get_stats_summary():
	"""Quick summary stats dena."""
	return {
		'total_hours': get_total_study_hours(),
		'avg_productivity': get_average_productivity(),
		'weak_subjects': get_weak_subjects(),
		'hours_by_subject': get_study_hours_by_subject()
	}
