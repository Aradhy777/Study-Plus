def validate_subject(name):
    if not name or len(name.strip()) == 0:
        return False, "Subject name cannot be empty"
    if len(name) > 100:
        return False, "Subject name too long"
    return True, "Valid"


def validate_session(subject, duration, date):
    if not subject:
        return False, "Subject required"
    if not duration or duration <= 0:
        return False, "Duration must be greater than 0"
    if not date:
        return False, "Date required"
    return True, "Valid"


def validate_marks(marks_obtained, total_marks):
    if marks_obtained < 0 or total_marks <= 0:
        return False, "Invalid marks"
    if marks_obtained > total_marks:
        return False, "Marks obtained cannot exceed total marks"
    return True, "Valid"
