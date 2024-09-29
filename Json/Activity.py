# Exercise 1: Complex JSON Parsing and Data Extraction
# You are given the following JSON string representing multiple people's details:
# json_string = '''
# {
#     "people": [
#         {"name": "Alice", "age": 28, "city": "Seattle", "pets": null},
#         {"name": "Bob", "age": 35, "city": "New York", "pets": ["Dog", "Cat"]},
#         {"name": "Charlie", "age": 42, "city": "Chicago", "pets": []}
#     ]
# }
# '''
# Write a Python function that parses this JSON and returns a list of dictionaries where each dictionary contains the name and pet count for people who have pets.
# #### **Input**:
# extract_pets(json_string)
# #### **Expected Output**:
# [{'name': 'Bob', 'pet_count': 2}]

# solution
import json
json_string = '''
{
    "people": [
        {"name": "Alice", "age": 28, "city": "Seattle", "pets": null},
        {"name": "Bob", "age": 35, "city": "New York", "pets": ["Dog", "Cat"]},
        {"name": "Charlie", "age": 42, "city": "Chicago", "pets": []}
    ]
}
'''
def extract_pets(input_json):
    to_dict = json.loads(input_json)
    with_pets = [{"name": data["name"], "pet_count": len(data["pets"])}
                 for data in to_dict["people"] if "pets" in data and data["pets"]]
    print(with_pets)

extract_pets(json_string)


print("\r")
# Exercise 2: JSON String Manipulation
# Given the following Python dictionary:
# person_info = {
#     "name": "Emma",
#     "age": 32,
#     "address": {
#         "street": "5th Ave",
#         "city": "New York"
#     },
#     "contact": {
#         "phone": "123-456-7890",
#         "email": "emma@mail.com"
#     }
# }
# Convert this dictionary to a JSON string, but modify the output format such that:
# - The keys are sorted alphabetically.
# - Use the `indent` parameter to format the JSON with 3 spaces.
# - Use custom separators: a colon followed by a space (`": "`), and no space after commas.
# #### **Input**:
# convert_to_custom_json(person_info)
# #### **Expected Output**:
# {
#    "address": {
#       "city": "New York",
#       "street": "5th Ave"
#    },
#    "age": 32,
#    "contact": {
#       "email": "emma@mail.com",
#       "phone": "123-456-7890"
#    },
#    "name": "Emma"
# }

# solution
person_info = {
    "name": "Emma",
    "age": 32,
    "address": {
        "street": "5th Ave",
        "city": "New York"
    },
    "contact": {
        "phone": "123-456-7890",
        "email": "emma@mail.com"
    }
}
def convert_to_custom_json(input_json):
    print(json.dumps(input_json, indent=3, sort_keys=True, separators=(",", ": ")))

convert_to_custom_json(person_info)


print("\r")
# Exercise 3: JSON Transformation
# You have a JSON structure of a company and employees, and you need to convert it into a specific output format. Here's the input JSON:
# company_data = {
#     "company": "TechCorp",
#     "employees": [
#         {"name": "Jake", "department": "Engineering", "salary": 70000},
#         {"name": "Laura", "department": "Marketing", "salary": 60000},
#         {"name": "John", "department": "Sales", "salary": 50000}
#     ]
# }
# Your task is to write a function that returns a JSON string where:
# - The employee data is sorted by salary in descending order.
# - The `salary` field is removed from the final JSON output.
# #### **Input**:
# transform_company_data(company_data)
# #### **Expected Output**:
# {
#    "company": "TechCorp",
#    "employees": [
#       {"name": "Jake", "department": "Engineering"},
#       {"name": "Laura", "department": "Marketing"},
#       {"name": "John", "department": "Sales"}
#    ]
# }

# solution
company_data = {
    "company": "TechCorp",
    "employees": [
        {"name": "Jake", "department": "Engineering", "salary": 70000},
        {"name": "Laura", "department": "Marketing", "salary": 60000},
        {"name": "John", "department": "Sales", "salary": 50000}
    ]
}
def transform_company_data(input_dict):
    employees = input_dict["employees"]
    employees.sort(key = lambda data: data["salary"], reverse = True)
    for data in employees: del data["salary"]
    input_dict["employees"] = employees
    print(json.dumps(input_dict, indent=3))

transform_company_data(company_data)


print("\r")
# Exercise 4: Nested JSON Modification
# You have the following nested JSON object:
# data = {
#     "university": {
#         "departments": [
#             {
#                 "name": "Computer Science",
#                 "courses": [
#                     {"course_name": "Data Structures", "students_enrolled": 50},
#                     {"course_name": "AI", "students_enrolled": 40}
#                 ]
#             },
#             {
#                 "name": "Mathematics",
#                 "courses": [
#                     {"course_name": "Algebra", "students_enrolled": 35},
#                     {"course_name": "Statistics", "students_enrolled": 30}
#                 ]
#             }
#         ]
#     }
# }
# Write a function that will:
# - Iterate through the JSON object.
# - Find and return a list of all courses where more than 35 students are enrolled.
# #### **Input**:
# find_popular_courses(data)
# #### **Expected Output**:
# ['Data Structures', 'AI', 'Algebra']

# solution
data = '''
{
    "university": {
        "departments": [
            {
                "name": "Computer Science",
                "courses": [
                    {"course_name": "Data Structures", "students_enrolled": 50},
                    {"course_name": "AI", "students_enrolled": 40}
                ]
            },
            {
                "name": "Mathematics",
                "courses": [
                    {"course_name": "Algebra", "students_enrolled": 35},
                    {"course_name": "Statistics", "students_enrolled": 30}
                ]
            }
        ]
    }
}
'''
def find_popular_courses(input_json):
    data = json.loads(input_json)
    courses = [courses["course_name"]
               for data in data["university"]["departments"]
               for courses in data["courses"]
               if courses["students_enrolled"] >= 35]
    print(courses)

find_popular_courses(data)


print("\r")
# Exercise 5: JSON File Handling
# Create a Python script that reads a JSON file containing multiple records of users (name, age, email), filters out users who are below 18 years of age, and writes the filtered users back to a new JSON file.
# #### **Input**:
# A JSON file named `users.json` with the following content:
# [
#     {"name": "Tom", "age": 16, "email": "tom@mail.com"},
#     {"name": "Jerry", "age": 22, "email": "jerry@mail.com"},
#     {"name": "Spike", "age": 15, "email": "spike@mail.com"},
#     {"name": "Tyke", "age": 18, "email": "tyke@mail.com"}
# ]
# #### **Expected Output**:
# A new JSON file `filtered_users.json` containing:
# [
#     {"name": "Jerry", "age": 22, "email": "jerry@mail.com"},
#     {"name": "Tyke", "age": 18, "email": "tyke@mail.com"}
# ]

# solution
json_file = open("users.json", "r")
reader = json_file.read()
to_list = json.loads(reader)
json_file.close()

legal_age = list(filter(lambda data : data["age"] >= 18, to_list))
to_json = json.dumps(legal_age, indent=3)

new_file = open("filtered_users.json", "w")
new_file.write(to_json)
new_file.close()