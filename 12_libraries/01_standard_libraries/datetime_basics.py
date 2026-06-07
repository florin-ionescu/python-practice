"""
datetime module

What it does:
- Works with dates and times.
- Useful for timestamps, deadlines, logs, reports, ticket age calculations.
"""
from datetime import datetime, date, timedelta

# current date and time
now = datetime.now()
print("Current datetime: ", now)

# current date only
today = date.today()
print("Today", today)

# Format datetime as string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# strftime means “string format time”.
# "%Y-%m-%d %H:%M:%S" mean -> Year-Month-Day Hour:Minute:Second
print("Formatted: ", formatted_date)

# Convert string to datetime
date_text = "2026-06-07"
# strptime means “string parse time”.
converted_date = datetime.strptime(date_text, "%Y-%m-%d")
print("Converted:", converted_date)

# Add days
future_date = today + timedelta(days=3)
print("One week from today:", future_date)

# Subtract days
past_date = today - timedelta(days=30)
# timedelta is used for adding or subtracting time.
print("30 days ago:", past_date)

# Example: calculate ticket age
ticket_created = datetime(2026, 6, 1, 10, 30)
ticket_age = now - ticket_created

# ticket_age.days Returns only the number of full days.
print("Ticket age:", ticket_age.days, "days")


