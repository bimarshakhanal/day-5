import json


def add_student(student_id: int, name: str, age: int, grade: str, filename: str = "students.json") -> None:
    """
    Adds a new student record to the specified JSON file.

    Args:
        student_id (int): The student's ID number.
        name (str): The student's name.
        age (int): The student's age.
        grade (str): The student's grade level.
        filename (str, optional): The filename of the JSON file to store records. Defaults to "students.json".
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []  # Create an empty list if file doesn't exist

    new_student = {"student_id": student_id,
                   "name": name, "age": age, "grade": grade}
    data.append(new_student)

    with open(filename, "w", encoding="utf-8") as f:
        # Save data with indentation for readability
        json.dump(data, f, indent=4)


def search_student(search_term: str, search_by: str = "student_id", filename: str = "students.json") -> dict:
    """
    Searches for a student record by student ID or name.

    Args:
        search_term (str): The term to search for (student ID or name).
        search_by (str, optional): The field to search by ("student_id" or "name"). Defaults to "student_id".
        filename (str, optional): The filename of the JSON file containing records. Defaults to "students.json".

    Returns:
        dict: A dictionary containing the student's age and grade if found, otherwise an empty dictionary.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return {}  # Return empty dict if file doesn't exist

    for student in data:
        if (search_by == "student_id" and student["student_id"] == search_term) or \
           (search_by == "name" and student["name"] == search_term):
            return {"age": student["age"], "grade": student["grade"]}
    return {}  # Return empty dict if student not found


def update_student(update_term: str, update_value: any, search_by: str = "student_id", filename: str = "students.json") -> bool:
    """
    Updates a student's information based on a search term and update value.

    Args:
        update_term (str): The term to search for (student ID or name).
        update_value (any): The new value to update (age or grade).
        search_by (str, optional): The field to search by ("student_id" or "name"). Defaults to "student_id".
        filename (str, optional): The filename of the JSON file containing records. Defaults to "students.json".

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return False  # File not found, cannot update

    updated = False
    for i, student in enumerate(data):
        if (search_by == "student_id" and student["student_id"] == update_term) or \
           (search_by == "name" and student["name"] == update_term):
            if update_value.isdigit() and update_term == "age":  # Validate age as integer
                student["age"] = int(update_value)
            else:
                # Update age or grade
                student["age"] = update_value if update_term == "age" else student["age"]
                student["grade"] = update_value if update_term == "grade" else student["grade"]
            updated = True
            break

    if updated:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f)
