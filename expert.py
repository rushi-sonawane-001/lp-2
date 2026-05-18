# Information Management Expert System

info_dict = {

    "student record":
    "Student records are stored successfully.",

    "library data":
    "Library database updated successfully.",

    "fees information":
    "Fees details are available in the accounts section.",

    "attendance":
    "Attendance records updated successfully.",

    "exam schedule":
    "Exam timetable uploaded on the portal."
}

# Function
def handle_request(user_input):

    if user_input == "exit":
        return "Thank you for using Information Management Expert System"

    elif user_input in info_dict:
        return info_dict[user_input]

    else:
        return "Information not found."

# Welcome Message
print("===== Information Management Expert System =====")

while True:

    print("\nAvailable Queries:")

    for query in info_dict:
        print("-", query)

    user_input = input("\nEnter your query: ").lower()

    response = handle_request(user_input)

    print("Response:", response)

    if user_input == "exit":
        break
    

# Hospital Expert System

hospital_dict = {

    "fever":
    "Take rest and drink plenty of water.",

    "headache":
    "Take proper sleep and consult doctor if needed.",

    "cold":
    "Drink warm water and take medicine.",

    "stomach pain":
    "Avoid outside food and consult doctor.",

    "cough":
    "Use cough syrup and drink warm water."
}

# Function
def handle_request(user_input):

    if user_input == "exit":
        return "Thank you for using Hospital Expert System"

    elif user_input in hospital_dict:
        return hospital_dict[user_input]

    else:
        return "Please consult a doctor."

# Welcome Message
print("===== Hospital Expert System =====")

while True:

    print("\nAvailable Symptoms:")

    for symptom in hospital_dict:
        print("-", symptom)

    user_input = input("\nEnter symptom: ").lower()

    response = handle_request(user_input)

    print("Solution:", response)

    if user_input == "exit":
        break


# Help Desk Expert System

problem_dict = {

    "printer not working":
    "Check that the printer is turned on and connected properly.",

    "can't log in":
    "Make sure you are using the correct username and password.",

    "software not installing":
    "Check system requirements and available storage.",

    "internet connection not working":
    "Restart your modem or router.",

    "email not sending":
    "Check your email server settings.",

    "keyboard not working":
    "Reconnect the keyboard or restart the computer.",

    "system running slow":
    "Close unwanted programs and scan for viruses."
}

# Function to handle requests
def handle_request(user_input):

    if user_input == "exit":
        return "Thank you for using Help Desk Expert System"

    elif user_input in problem_dict:
        return problem_dict[user_input]

    else:
        return "Problem not found. Please choose from the list."

# Welcome Message
print("===== Help Desk Expert System =====")

while True:

    print("\nAvailable Problems:")

    for problem in problem_dict:
        print("-", problem)

    user_input = input("\nEnter your problem: ").lower()

    response = handle_request(user_input)

    print("Solution:", response)

    if user_input == "exit":
        break
    

# Employee Performance Evaluation Expert System

employee_dict = {

    "excellent":
    "Employee is eligible for promotion.",

    "good":
    "Employee performance is very good.",

    "average":
    "Employee performance is satisfactory.",

    "poor":
    "Employee needs improvement and training.",

    "attendance issue":
    "Employee attendance should be improved."
}

# Function
def handle_request(user_input):

    if user_input == "exit":
        return "Thank you for using Employee Expert System"

    elif user_input in employee_dict:
        return employee_dict[user_input]

    else:
        return "Evaluation not available."

# Welcome Message
print("===== Employee Performance Expert System =====")

while True:

    print("\nAvailable Performance Types:")

    for performance in employee_dict:
        print("-", performance)

    user_input = input("\nEnter performance type: ").lower()

    response = handle_request(user_input)

    print("Evaluation:", response)

    if user_input == "exit":
        break
    

# Stock Market Expert System

stock_dict = {

    "amazon":
    "Amazon stock is performing well.",

    "tesla":
    "Tesla stock is highly volatile.",

    "google":
    "Google stock is stable.",

    "apple":
    "Apple stock is good for long-term investment.",

    "microsoft":
    "Microsoft stock shows steady growth."
}

# Function
def handle_request(user_input):

    if user_input == "exit":
        return "Thank you for using Stock Market Expert System"

    elif user_input in stock_dict:
        return stock_dict[user_input]

    else:
        return "Stock information not available."

# Welcome Message
print("===== Stock Market Expert System =====")

while True:

    print("\nAvailable Companies:")

    for company in stock_dict:
        print("-", company)

    user_input = input("\nEnter company name: ").lower()

    response = handle_request(user_input)

    print("Suggestion:", response)

    if user_input == "exit":
        break
    

# Airline Scheduling Expert System

airline_dict = {

    "cargo flight":
    "Cargo flight scheduled at 8 PM.",

    "passenger flight":
    "Passenger flight scheduled at 10 AM.",

    "international flight":
    "International flight scheduled at 6 AM.",

    "domestic flight":
    "Domestic flight scheduled at 2 PM.",

    "delayed flight":
    "Flight delayed due to weather conditions."
}

# Function
def handle_request(user_input):

    if user_input == "exit":
        return "Thank you for using Airline Expert System"

    elif user_input in airline_dict:
        return airline_dict[user_input]

    else:
        return "Schedule not available."

# Welcome Message
print("===== Airline Scheduling Expert System =====")

while True:

    print("\nAvailable Flight Types:")

    for flight in airline_dict:
        print("-", flight)

    user_input = input("\nEnter flight type: ").lower()

    response = handle_request(user_input)

    print("Schedule:", response)

    if user_input == "exit":
        break
    

