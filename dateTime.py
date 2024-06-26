from datetime import datetime, timedelta

now = datetime.now()
print("Current time:", now)

one_week_later = now + timedelta(weeks=1)
print("One week later:", one_week_later)
