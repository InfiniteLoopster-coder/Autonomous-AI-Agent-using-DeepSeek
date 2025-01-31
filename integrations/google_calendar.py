import requests
import config

def create_event(event_details):
    headers = {"Authorization": f"Bearer {config.GOOGLE_CALENDAR_API_KEY}"}
    payload = {
        "summary": event_details["summary"],
        "start": {"dateTime": event_details["time"]},
        "attendees": [{"email": email} for email in event_details["attendees"]]
    }
    response = requests.post("https://www.googleapis.com/calendar/v3/calendars/primary/events", json=payload, headers=headers)
    return response.json()
