import json
import logging

JSON_FILE = 'data.json'
logging.basicConfig(filename='log.txt')


def add_student(student_id: int, name: str, age: int, grade: str) -> None:
    """
    Adds a new student record and store in a JSON file.

    Args:
        student_id (int): The student's ID number.
        name (str): The student's name.
        age (int): The student's age.
        grade (str): The student's grade level.
    """

    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        logging.warning('Existing data file not found.')
        data = []  # Create an empty list if file doesn't exist

    try:
        new_student = {"student_id": student_id,
                       "name": name, "age": age, "grade": grade}
        data.append(new_student)

        with open(JSON_FILE, "w", encoding="utf-8") as f:
            # Save data with indentation for readability
            json.dump(data, f, indent=4)
    except:
        logging.error('Failed to add record.')


def search_student(search_term: str) -> dict:
    """
    Searches for a student record by student ID or name.

    Args:
        search_term (str): The term to search for (student ID or name).

    Returns:
        list: A list of dict of matching student's record, otherwise an empty list.
    """
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []  # Return empty dict if file doesn't exist
    try:
        results = []
        for student in data:
            if (str(student["student_id"]) == search_term) or \
                    (search_term.lower() in student["name"].lower()):
                results.append(student)
        return results
    except:
        logging.error('Search Failed')


def update_student(update_term: str, update_value: any, student_id: int) -> bool:
    """
    Updates a student's information based on a search term and update value.

    Args:
        update_term (str): The term to update (name, age or grade).
        update_value (any): The new value to update (age or grade).
        student_id (int): ID of student to update.
        filename (str, optional): The filename of the JSON file containing records. Defaults to "students.json".

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        logging.error('Failed to update record, data file not found')
        return False  # File not found, cannot update

    updated = False
    print('Here')
    try:
        for i, student in enumerate(data):
            if (student_id == student['student_id']):

                # update age
                if update_value.isdigit() and update_term == "age":  # Validate age as integer
                    student["age"] = int(update_value)
                else:
                    # Update name or grade
                    student[update_term] = update_value
                updated = True
                break
    except:
        logging.error('Failed to update record.')

    if updated:
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)


def main() -> None:
    """
    Driver function to manage student records
    """

    try:
        while True:
            print("\n", "*"*10)
            print('Enter your choice')
            print('1. Add student')
            print('2. Search student')
            print('3. Update student record.')
            print('5. Exit')

            ch = input('YOur choice? (1,2,3,4): ')

            if ch == '1':
                student_id, name, age, grade = input(
                    'Enter id, name, age, grade: ').split(",")
                add_student(int(student_id), name, int(age), grade)
            elif ch == '2':
                search_term = input('Enter student name or id to search: ')
                search_result = search_student(search_term)
                print('Record Found:', search_result)
            elif ch == '3':
                student_id = input('Enter student id to update: ')
                update_term = input('Enter entity to update (age,grade): ')
                update_value = input(
                    f'Enter updated value for {update_term}: ')
                update_student(update_term, update_value, student_id)
            elif ch == '4':
                exit()
            else:
                print('Invalid input')
    except:
        logging.info(f'Student management system crashed.')


if __name__ == '__main__':
    main()
