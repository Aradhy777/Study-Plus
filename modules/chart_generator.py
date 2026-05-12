import os

from models.session import StudySession
from models.marks import Mark


def ensure_charts_dir():
    charts_dir = os.path.join('static', 'charts')
    if not os.path.exists(charts_dir):
        os.makedirs(charts_dir)
    return charts_dir


def get_matplotlib():
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        return plt
    except Exception:
        return None


def generate_study_hours_chart():
    plt = get_matplotlib()
    if not plt:
        return None

    sessions = StudySession.query.all()
    if not sessions:
        return None

    subject_hours = {}
    for session in sessions:
        hours = session.duration / 60
        if session.subject not in subject_hours:
            subject_hours[session.subject] = 0
        subject_hours[session.subject] += hours

    if not subject_hours:
        return None

    ensure_charts_dir()
    plt.figure(figsize=(10, 6))
    plt.bar(subject_hours.keys(), subject_hours.values(), color='skyblue')
    plt.xlabel('Subjects')
    plt.ylabel('Hours Studied')
    plt.title('Study Hours by Subject')
    plt.xticks(rotation=45)
    plt.tight_layout()
    chart_path = os.path.join('static', 'charts', 'study_hours.png')
    plt.savefig(chart_path)
    plt.close()
    return chart_path


def generate_marks_chart():
    plt = get_matplotlib()
    if not plt:
        return None

    marks = Mark.query.all()
    if not marks:
        return None

    subject_marks = {}
    for mark in marks:
        if mark.subject not in subject_marks:
            subject_marks[mark.subject] = []
        subject_marks[mark.subject].append(mark.percentage())

    if not subject_marks:
        return None

    avg_marks = {subject: sum(scores) / len(scores) for subject, scores in subject_marks.items()}

    ensure_charts_dir()
    plt.figure(figsize=(10, 6))
    colors = ['green' if value >= 70 else 'orange' if value >= 50 else 'red' for value in avg_marks.values()]
    plt.bar(avg_marks.keys(), avg_marks.values(), color=colors)
    plt.xlabel('Subjects')
    plt.ylabel('Average Percentage')
    plt.title('Marks Performance by Subject')
    plt.xticks(rotation=45)
    plt.tight_layout()
    chart_path = os.path.join('static', 'charts', 'marks_chart.png')
    plt.savefig(chart_path)
    plt.close()
    return chart_path


def generate_productivity_chart():
    plt = get_matplotlib()
    if not plt:
        return None

    sessions = StudySession.query.all()
    sessions = [session for session in sessions if session.productivity is not None]
    if not sessions:
        return None

    ensure_charts_dir()
    dates = [str(session.date) for session in sessions]
    productivity = [session.productivity for session in sessions]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, productivity, marker='o', color='purple')
    plt.xlabel('Date')
    plt.ylabel('Productivity Score')
    plt.title('Productivity Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    chart_path = os.path.join('static', 'charts', 'productivity_chart.png')
    plt.savefig(chart_path)
    plt.close()
    return chart_path
