try:
    import pandas as pd
except Exception:
    pd = None

try:
    import numpy as np
except Exception:
    np = None

from models.session import StudySession
from models.subject import Subject
from models.marks import Mark


def get_total_study_hours():
    sessions = StudySession.query.all()
    if not sessions:
        return 0
    total_minutes = sum(session.duration for session in sessions)
    return round(total_minutes / 60, 2)


def get_average_productivity():
    sessions = StudySession.query.all()
    scores = [session.productivity for session in sessions if session.productivity is not None]
    if not scores:
        return 0

    # numpy ho to usse use kar lete hain, warna simple average
    if np:
        return round(float(np.mean(scores)), 2)
    return round(sum(scores) / len(scores), 2)


def get_weak_subjects():
    subjects = Subject.query.all()
    weak_subjects = []

    for subject in subjects:
        sessions = StudySession.query.filter_by(subject=subject.name).all()
        studied_hours = sum(session.duration for session in sessions) / 60

        if studied_hours < subject.target_hours:
            weak_subjects.append({
                'name': subject.name,
                'studied': round(studied_hours, 2),
                'target': subject.target_hours
            })

    weak_subjects.sort(key=lambda item: item['studied'])
    return weak_subjects


def get_average_marks_by_subject():
    marks = Mark.query.all()
    if not marks:
        return {}

    subject_scores = {}
    for mark in marks:
        percentage = mark.percentage()
        if mark.subject not in subject_scores:
            subject_scores[mark.subject] = []
        subject_scores[mark.subject].append(percentage)

    if pd:
        rows = []
        for subject, scores in subject_scores.items():
            for score in scores:
                rows.append({'subject': subject, 'percentage': score})
        df = pd.DataFrame(rows)
        if df.empty:
            return {}
        grouped = df.groupby('subject')['percentage'].mean().round(2)
        return grouped.to_dict()

    return {
        subject: round(sum(scores) / len(scores), 2)
        for subject, scores in subject_scores.items()
    }


def get_study_hours_by_subject():
    sessions = StudySession.query.all()
    subject_hours = {}

    for session in sessions:
        hours = session.duration / 60
        if session.subject not in subject_hours:
            subject_hours[session.subject] = 0
        subject_hours[session.subject] += hours

    return {subject: round(hours, 2) for subject, hours in subject_hours.items()}


def get_stats_summary():
    return {
        'total_hours': get_total_study_hours(),
        'avg_productivity': get_average_productivity(),
        'weak_subjects': get_weak_subjects(),
        'hours_by_subject': get_study_hours_by_subject(),
        'marks_by_subject': get_average_marks_by_subject(),
    }
