def review(e_list):
    print(f"Review records are found\n{e_list}")
    user_ip = input("Do you want to update the list?Y/N")
    if user_ip.upper() == "Y":
        for ele in e_list:
            print(f"{ele}")
            ip = input("Do you want to update this employee Data?Y/N")
            if ip.upper() == "Y":
                sal=int(input("Enter the updated Salary:"))
                ele["salary"] = sal
    return e_list
