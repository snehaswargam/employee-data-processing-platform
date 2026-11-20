
from src.employee_processor import validators,review_func

def main():
    employees = [
        {"employee_id": 101, "name": "Julie", "salary": 75000},
        {"employee_id": 102, "name": "Jenny", "salary": 0},
        {"employee_id": 103, "name": "George", "salary": 70000},
        {"employee_id": 104, "name": "Alex", "salary": -5000},
        {"employee_id": 105, "name": "James", "salary": 60000}
    ]
    gen =validators.validate_salary(employees)
    op=[]
    review_list=[]

    for ele in gen:
        if ele["comments"] == "Review":
            review_list.append(ele)
        else:
            op.append(ele)

    if review_list:

        review_list=review_func.review(review_list)
        gen1 = validators.validate_salary(review_list)
        remaining_review = []
        for ele in gen1:
            if ele["comments"] == "Review":
                remaining_review.append(ele)
            else:
                op.append(ele)

        review_list=remaining_review
    print(f"{len(op)} employees\n{op}")
    print(f"{len(review_list)} review_list\n{review_list}")




if __name__ == '__main__':
    main()


