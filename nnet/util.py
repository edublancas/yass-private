import datetime

def directory():
    """Generate a valid directory name with the current datetime
    """
    now = datetime.datetime.now()
    return now.strftime('%d-%b-%Y@%H-%M-%S')