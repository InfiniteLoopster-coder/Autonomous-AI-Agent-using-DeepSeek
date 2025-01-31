from autogen import UserProxyAgent
import integrations.google_calendar as google_calendar

scheduler_agent = UserProxyAgent(
    name="Scheduler_Agent",
    human_input_mode="ALWAYS",
    system_message="You manage scheduling tasks and interact with Google Calendar."
)

def schedule_meeting(time, participants):
    event_details = {
        "summary": "Meeting with AI Assistant",
        "time": time,
        "attendees": participants
    }
    return google_calendar.create_event(event_details)
