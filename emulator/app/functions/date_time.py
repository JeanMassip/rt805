from datetime import datetime
import pytz

def get_datetime_now():
    tz_FR = pytz.timezone('Europe/Paris')
    datetime_FR = datetime.now(tz_FR)
    
    return datetime_FR.strftime("%d/%m/%Y - %H:%M:%S")