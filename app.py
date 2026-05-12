from pathlib import Path

from flask import Flask, render_template

from modules.database_manager import db
from models.session import StudySession  # noqa: F401
from models.subject import Subject  # noqa: F401


def create_app():
	app = Flask(__name__)

	base_dir = Path(__file__).resolve().parent
	db_path = base_dir / "database" / "study_tracker.db"

	app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path.as_posix()}"
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

	db.init_app(app)

	with app.app_context():
		db.create_all()

	return app


app = create_app()


@app.route("/")
def index():
	# yaha homepage render ho rha hai
	return render_template("index.html")


@app.route("/dashboard")
def dashboard():
	return render_template("dashboard.html")


@app.route("/subjects")
def subjects():
	return render_template("subjects.html")


@app.route("/sessions")
def sessions():
	return render_template("sessions.html")


@app.route("/marks")
def marks():
	return render_template("marks.html")


@app.route("/analytics")
def analytics():
	return render_template("analytics.html")


if __name__ == "__main__":
	app.run(debug=True)
