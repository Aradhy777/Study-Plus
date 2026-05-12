from pathlib import Path
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, flash

from modules.database_manager import db
from modules import database_manager as db_mgr
from modules import analytics as anal
from modules import chart_generator as charts
from modules.validators import validate_subject, validate_session, validate_marks
from models.session import StudySession  # noqa: F401
from models.subject import Subject  # noqa: F401
from models.marks import Mark  # noqa: F401


app = Flask(__name__)
app.secret_key = 'study_pulse_secret'

base_dir = Path(__file__).resolve().parent
db_path = base_dir / "database" / "study_tracker.db"

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path.as_posix()}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
	db.create_all()


@app.route("/")
def index():
	stats = anal.get_stats_summary()
	return render_template("index.html", stats=stats)


@app.route("/dashboard")
def dashboard():
	stats = anal.get_stats_summary()
	weak_subjects = anal.get_weak_subjects()
	return render_template("dashboard.html", stats=stats, weak_subjects=weak_subjects)


@app.route("/subjects")
def subjects():
	all_subjects = db_mgr.get_all_subjects()
	return render_template("subjects.html", subjects=all_subjects)


@app.route("/add_subject", methods=['GET', 'POST'])
def add_subject():
	if request.method == 'POST':
		name = request.form.get('name')
		target_hours_raw = request.form.get('target_hours')
		target_hours = float(target_hours_raw) if target_hours_raw else 10.0
        
		valid, msg = validate_subject(name)
		if not valid:
			flash(msg, 'danger')
			return redirect(url_for('subjects'))
        
		try:
			db_mgr.add_subject(name, target_hours)
			flash(f'Subject {name} added!', 'success')
		except Exception as e:
			flash(f'Error: {str(e)}', 'danger')
        
		return redirect(url_for('subjects'))
    
	return render_template("add_subject.html")


@app.route("/delete_subject/<int:subject_id>")
def delete_subject(subject_id):
	try:
		db_mgr.delete_subject(subject_id)
		flash('Subject deleted!', 'success')
	except Exception as e:
		flash(f'Error: {str(e)}', 'danger')
    
	return redirect(url_for('subjects'))


@app.route("/sessions")
def sessions():
	all_sessions = db_mgr.get_all_sessions()
	return render_template("sessions.html", sessions=all_sessions)


@app.route("/add_session", methods=['GET', 'POST'])
def add_session():
	if request.method == 'POST':
		subject = request.form.get('subject')
		date_str = request.form.get('date')
		duration = int(request.form.get('duration', 0))
		productivity = float(request.form.get('productivity')) if request.form.get('productivity') else None
        
		valid, msg = validate_session(subject, duration, date_str)
		if not valid:
			flash(msg, 'danger')
			return redirect(url_for('sessions'))
        
		try:
			date = datetime.strptime(date_str, '%Y-%m-%d').date()
			db_mgr.add_session(subject, date, duration, productivity)
			flash('Study session added!', 'success')
		except Exception as e:
			flash(f'Error: {str(e)}', 'danger')
        
		return redirect(url_for('sessions'))
    
	subjects = db_mgr.get_all_subjects()
	return render_template("add_session.html", subjects=subjects)


@app.route("/delete_session/<int:session_id>")
def delete_session(session_id):
	try:
		db_mgr.delete_session(session_id)
		flash('Session deleted!', 'success')
	except Exception as e:
		flash(f'Error: {str(e)}', 'danger')
    
	return redirect(url_for('sessions'))


@app.route("/marks")
def marks():
	all_marks = db_mgr.get_all_marks()
	return render_template("marks.html", marks=all_marks)


@app.route("/add_mark", methods=['GET', 'POST'])
def add_mark():
	if request.method == 'POST':
		subject = request.form.get('subject')
		marks_obtained_raw = request.form.get('marks_obtained')
		total_marks_raw = request.form.get('total_marks')
		
		try:
			marks_obtained = float(marks_obtained_raw) if marks_obtained_raw else 0.0
			total_marks = float(total_marks_raw) if total_marks_raw else 100.0
		except ValueError:
			flash("Invalid marks format", 'danger')
			return redirect(url_for('marks'))
			
		exam_date_str = request.form.get('exam_date')
		exam_type = request.form.get('exam_type')
        
		valid, msg = validate_marks(marks_obtained, total_marks)
		if not valid:
			flash(msg, 'danger')
			return redirect(url_for('marks'))
        
		try:
			exam_date = datetime.strptime(exam_date_str, '%Y-%m-%d').date()
			db_mgr.add_mark(subject, marks_obtained, total_marks, exam_date, exam_type)
			flash('Marks added!', 'success')
		except Exception as e:
			flash(f'Error: {str(e)}', 'danger')
        
		return redirect(url_for('marks'))
    
	subjects = db_mgr.get_all_subjects()
	return render_template("add_mark.html", subjects=subjects)


@app.route("/delete_mark/<int:mark_id>")
def delete_mark(mark_id):
	try:
		db_mgr.delete_mark(mark_id)
		flash('Mark deleted!', 'success')
	except Exception as e:
		flash(f'Error: {str(e)}', 'danger')
    
	return redirect(url_for('marks'))


@app.route("/analytics")
def analytics():
	stats = anal.get_stats_summary()
	charts.generate_study_hours_chart()
	charts.generate_marks_chart()
	charts.generate_productivity_chart()
	return render_template("analytics.html", stats=stats)



if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=False)
