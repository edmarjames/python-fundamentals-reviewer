# 1. Dictionary Manipulation
# You are given a dictionary of students and their corresponding scores. Write a function top_scorer() that returns the student with the highest score.
    # Expected Output:
    # 'Charlie'

# solution
def get_highest_score(students):
    all_scores = students.values()
    max_score = max(all_scores)    

    for student, scores in students.items():
        if max_score == scores:            
            return student    

students_scores = {
    "Alice": 87,
    "Bob": 92,
    "Charlie": 100,
    "David": 95,
    "Eva": 78
}
high_scorer = get_highest_score(students_scores)
print(high_scorer)


print("\n")
# 2. Nested Dictionary Operations
# You have a nested dictionary of employee data. Write a function update_employee_age() that accepts an employee name and a new age, and updates the age in the dictionary.
    # Expected Output:
    # update_employee_age("Charlie", 30)
    # # employees["E003"]["age"] should now be 30

# solution
def update_employee_age(name, age):
    for data in employees.values():        
        if data["name"] == name:                      
            data["age"] = age    

employees = {
    "E001": {"name": "Alice", "age": 29, "department": "HR"},
    "E002": {"name": "Bob", "age": 35, "department": "IT"},
    "E003": {"name": "Charlie", "age": 28, "department": "Finance"}
}
update_employee_age("Charlie", 30)
print(employees["E003"]["age"])


print("\n")
# 3. Dictionary Merge
# You have two dictionaries of stock items from different warehouses. Write a function merge_stocks() that combines them. If an item appears in both, sum their quantities.
    # Expected Output:
    # {
    #   "Apples": 50,
    #   "Bananas": 160,
    #   "Oranges": 115,
    #   "Pears": 100
    # }

# solution
def merge_stocks(stock1, stock2):
    final_stock = {}

    for stock, quantity in stock1.items():
        if stock not in final_stock:
            final_stock[stock] = quantity
        else:
            final_stock[stock] += quantity

    for stock, quantity in stock2.items():
        if stock not in final_stock:
            final_stock[stock] = quantity
        else:
            final_stock[stock] += quantity

    return final_stock

warehouse_a = {
    "Apples": 50,
    "Bananas": 100,
    "Oranges": 75
}

warehouse_b = {
    "Bananas": 60,
    "Oranges": 40,
    "Pears": 100
}
merged_stock = merge_stocks(warehouse_a, warehouse_b)
print(merged_stock)


print("\n")
# 4. Frequency Count
# Write a function word_frequency() that takes a list of words and returns a dictionary with the frequency count of each word. Ignore case when counting.
    # Expected Output:
    # {
    #   "apple": 3,
    #   "banana": 3,
    #   "orange": 1
    # }

# solution
def word_frequency(words):
    word_count = {}

    for word in words:
        if word.lower() not in word_count:
            word_count[word.lower()] = 1
        else:
            word_count[word.lower()] += 1

    return word_count

words = ["apple", "banana", "Apple", "orange", "banana", "apple", "Banana"]
word_counts = word_frequency(words)
print(word_counts)


print("\n")
# 5. Multiple Nested Loops
# You are given a dictionary where keys are strings (cities) and values are dictionaries containing information about the population and area (in km²). Write a function city_density() that computes the population density for each city.
    # Expected Output:
    # {
    #   "New York": 10671.1,
    #   "Los Angeles": 3056.7,
    #   "Chicago": 4609.5
    # }

# solution
def city_density(cities):
    population_density = {}

    for city, data in cities.items():
        population = data.get("population", 0)
        area = data.get("area", 0)

        if population and area:
            density = population / area
            population_density[city] = round(density, 1)

    return population_density

cities = {
    "New York": {"population": 8419600, "area": 789},
    "Los Angeles": {"population": 3980400, "area": 1302},
    "Chicago": {"population": 2716000, "area": 589}
}
population_density = city_density(cities)
print(population_density)


print("\n")
# 6. Remove Duplicates from Dictionary Values
# Write a function remove_duplicates() that accepts a dictionary where the values are lists. The function should remove any duplicate items within each list.
    # Expected Output:
    # {
    #   "group1": [1, 2, 3, 4],
    #   "group2": [4, 5, 6, 7],
    #   "group3": [8, 9, 10]
    # }

# solution
def remove_duplicates(data):
    final_data = {}

    for group, data in data.items():
        final_data[group] = []
        for items in data:
            if items not in final_data[group]:
                final_data[group].append(items)

    return final_data

data = {
    "group1": [1, 2, 3, 3, 4],
    "group2": [4, 5, 6, 6, 7],
    "group3": [8, 9, 9, 10]
}
clean_data = remove_duplicates(data)
print(clean_data)


print("\n")
# 7. Key Transformation
# Write a function keys_to_uppercase() that converts all the keys in a given dictionary to uppercase. Assume all keys are strings.
    # Expected Output:
    # {
    #   "NAME": "Alice",
    #   "AGE": 30,
    #   "CITY": "New York"
    # }

# solution
def keys_to_uppercase(data):
    final_data = {}
    for key, value in data.items():
        final_data[key.upper()] = value
    return final_data

example_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
to_upper_keys = keys_to_uppercase(example_dict)
print(to_upper_keys)