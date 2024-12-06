employees = {"Antony":55000,"Susan":45000,"Kiran":60000}
cate_employees ={n:'high' if salary <50000 else 'low' for n,salary in employees.items()}
print(cate_employees)