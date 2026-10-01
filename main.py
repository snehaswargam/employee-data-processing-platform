# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    employees = [{
        "employee_id": 101,
        "name": "Julie",
        "department": "HR",
        "salary": 75000,
        "joining_date": "2024-04-22",
        "status": "Active"

    },
        {
            "employee_id": 102,
            "name": "Jenny",
            "department": "Finance",
            "salary": 90000,
            "joining_date": "2022-03-22",
            "status": "Active"

        },
        {
            "employee_id": 103,
            "name": "Gorge",
            "department": "Sales",
            "salary": 70000,
            "joining_date": "2024-02-02",
            "status": "InActive"
        },
        {
            "employee_id": 202,
            "name": "Alex",
            "department": "Sales",
            "salary": 85000,
            "joining_date": "2022-05-30",
            "status": "Active"
        },
        {
            "employee_id": 333,
            "name": "James",
            "department": "Sales",
            "salary": 60000,
            "joining_date": "2022-06-30",
            "status": "Active"
        }
    ]
    print(f"{len(employees)} employees")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
