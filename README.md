# StudyPulse 📚

A simple Flask-based web application for tracking study sessions, subjects, marks, and productivity. Built like a real BTech 2nd semester student project.

## Features

- **Subject Management**: Add and manage subjects with target study hours
- **Study Sessions**: Log study hours with productivity scores
- **Marks Tracking**: Record exam marks and calculate percentages
- **Analytics Dashboard**: View study statistics and weak subjects
- **Charts & Visualization**: Generate matplotlib charts for progress tracking
- **Clean UI**: Bootstrap-based responsive interface

## Tech Stack

- **Backend**: Flask, Flask-SQLAlchemy
- **Database**: SQLite
- **Data Analysis**: Pandas, NumPy
- **Visualization**: Matplotlib
- **Frontend**: Bootstrap 5, HTML, CSS

## Project Structure

```
StudyPulse/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── database/
│   └── study_tracker.db   # SQLite database
├── static/
│   ├── css/
│   │   └── style.css      # Custom styling
│   ├── js/                # JavaScript (if needed)
│   └── charts/            # Generated chart images
├── templates/
│   ├── base.html          # Base template
│   ├── index.html         # Home page
│   ├── dashboard.html     # Dashboard
│   ├── subjects.html      # Subjects list
│   ├── sessions.html      # Study sessions list
│   ├── marks.html         # Marks list
│   ├── analytics.html     # Analytics & charts
│   ├── add_subject.html   # Add subject form
│   ├── add_session.html   # Add session form
│   └── add_mark.html      # Add mark form
├── modules/
│   ├── database_manager.py    # Database operations
│   ├── analytics.py           # Analytics functions
│   ├── chart_generator.py     # Chart generation
│   ├── validators.py          # Form validation
│   └── utilities.py           # Helper functions
├── models/
│   ├── subject.py         # Subject model
│   ├── session.py         # StudySession model
│   └── marks.py           # Mark model
└── exports/               # Export directory
```

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Aradhy777/Study-Plus.git
cd StudyPulse
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

The app will be running at `http://localhost:5000`

## Usage

1. **Add Subjects**: Go to Subjects → Add a new subject with target study hours
2. **Log Sessions**: Sessions → Log your study hours with productivity score
3. **Record Marks**: Marks → Add exam marks and track performance
4. **View Analytics**: Dashboard & Analytics show study statistics and charts

## Features Breakdown

### Dashboard
- Total hours studied
- Average productivity score
- Study hours by subject
- Weak subjects identification

### Analytics
- Study hours trend
- Subject-wise marks performance
- Productivity tracking over time
- Auto-generated matplotlib charts

### Data Management
- Add/Delete subjects
- Add/Delete study sessions
- Add/Delete marks
- Real-time statistics calculation

## Deployment

Can be deployed on:
- Railway.app
- PythonAnywhere
- Heroku
- AWS/DigitalOcean

## Notes

- Database is stored as SQLite file locally
- Charts are regenerated on each analytics page visit
- No user authentication - single user app
- Responsive design works on mobile and desktop

## Author

Built like a real Indian BTech student project. Yeh sirf learning purposes ke liye bana hai! 🎓

## License

This project is open source and available for educational purposes.
