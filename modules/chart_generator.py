import matplotlib.pyplot as plt
import pandas as pd
import os
from models.session import StudySession
from models.marks import Mark


def ensure_charts_dir():
    if not os.path.exists("static/charts"):
        os.makedirs("static/charts")


def generate_study_hours_chart():
    ensure_charts_dir()
    
    sessions = StudySession.query.all()
    if not sessions:
        return None
    
    subjects = {}
    for session in sessions:
        hours = session.duration / 60
        if session.subject not in subjects:
            subjects[session.subject] = 0
        subjects[session.subject] += hours
    
    if not subjects:
        return None
    
    plt.figure(figsize=(10, 6))
    plt.bar(subjects.keys(), subjects.values(), color='skyblue')
    plt.xlabel('Subjects')
    plt.ylabel('Hours Studied')
    plt.title('Study Hours by Subject')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    chart_path = 'static/charts/study_hours.png'
    plt.savefig(chart_path)
    plt.close()
    return chart_path


def generate_marks_chart():
    ensure_charts_dir()
    
    marks = Mark.query.all()
    if not marks:
        return None
    
    subjects = {}
    for mark in marks:
        percentage = mark.percentage()
        if mark.subject not in subjects:
            subjects[mark.subject] = []
        subjects[mark.subject].append(percentage)
    
    if not subjects:
        return None
    
    avg_marks = {subject: sum(marks) / len(marks) for subject, marks in subjects.items()}
    
    plt.figure(figsize=(10, 6))
    colors = ['green' if v >= 70 else 'orange' if v >= 50 else 'red' for v in avg_marks.values()]
    plt.bar(avg_marks.keys(), avg_marks.values(), color=colors)
    plt.xlabel('Subjects')
    plt.ylabel('Average Percentage')
    plt.title('Marks Performance by Subject')
    plt.axhline(y=70, color='green', linestyle='--', alpha=0.5, label='Good')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    
    chart_path = 'static/charts/marks_chart.png'
    plt.savefig(chart_path)
    plt.close()
    return chart_path


def generate_productivity_chart():
    ensure_charts_dir()
    
    sessions = StudySession.query.all()
    if not sessions:
        return None
    
    sessions = [s for s in sessions if s.productivity is not None]
    if not sessions:
        return None
    
    dates = [str(s.date) for s in sessions]
    productivity = [s.productivity for s in sessions]
    
    plt.figure(figsize=(10, 6))
    plt.plot(dates, productivity, marker='o', color='purple')
    plt.xlabel('Date')
    plt.ylabel('Productivity Score')
    plt.title('Productivity Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    chart_path = 'static/charts/productivity_chart.png'
    plt.savefig(chart_path)
    plt.close()
    return chart_path
