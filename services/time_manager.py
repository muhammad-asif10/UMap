import json
import datetime
import os

class TimeManager:
    def __init__(self, data_file="data/schedules.json"):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        if not os.path.exists(self.data_file):
            return {}
        with open(self.data_file, 'r') as f:
            return json.load(f)

    def get_current_time(self):
        return datetime.datetime.now()

    def is_time_in_range(self, start_str, end_str, current_time):
        try:
            start_time = datetime.datetime.strptime(start_str, "%H:%M").time()
            end_time = datetime.datetime.strptime(end_str, "%H:%M").time()
            current_time = current_time.time()

            if start_time <= end_time:
                return start_time <= current_time <= end_time
            else: # Crosses midnight
                return current_time >= start_time or current_time <= end_time
        except ValueError:
            return False

    def get_current_class(self, location, room):
        if location not in self.data.get("timetables", {}):
            return None
        
        rooms = self.data["timetables"][location]
        if room not in rooms:
            return None

        now = self.get_current_time()
        current_day = now.strftime("%A") # e.g., "Wednesday"
        
        for slot in rooms[room]:
            if slot["day"] == current_day:
                if self.is_time_in_range(slot["start"], slot["end"], now):
                    return slot
        return None

    def check_restriction(self, start_loc, end_loc):
        restrictions = self.data.get("restrictions", [])
        now = self.get_current_time()

        for rule in restrictions:
            if rule["from"] == start_loc and end_loc in rule["to"]:
                if self.is_time_in_range(rule["start"], rule["end"], now):
                    return rule["message"]
        return None

    def get_facility_status(self, facility, gender):
        facilities = self.data.get("facilities", {})
        if facility not in facilities:
            return None
        
        schedule = facilities[facility].get(gender)
        if not schedule:
            return None

        now = self.get_current_time()
        if self.is_time_in_range(schedule["start"], schedule["end"], now):
            return f"Open ({schedule['start']} - {schedule['end']})"
        else:
            return f"Closed (Open: {schedule['start']} - {schedule['end']})"
