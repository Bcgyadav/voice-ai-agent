appointments = []

def check_availability(doctor, date):
    return ["10:00 AM", "2:00 PM", "4:00 PM"]

def book_appointment(data):
    appointments.append(data)
    return f"Appointment booked with {data['doctor']} on {data['date']} at {data['time']}"

def cancel_appointment(data):
    return "Appointment cancelled"

def reschedule_appointment(data):
    return "Appointment rescheduled"