def validate_salary(employees):
    for ele in employees:
        salary = ele.get("salary")
        if salary is None:
            ele["comments"] = "Review"
            yield ele
        else:
            if isinstance(salary, (int, float)) and not isinstance(salary, bool) and salary > 0:
                ele["comments"] = "Valid"
                yield ele
            else:
                ele["comments"] = "Review"
                yield ele
