class department:
    dept_count = 0

    def __init__(self, dt_name, dt_id, dt_loc, dt_head):
        self.dt_name = dt_name
        self.dt_id = dt_id
        self.dt_loc = dt_loc
        self.dt_head = dt_head
        department.dept_count += 1

    def display_dept_info(self):
        print("\nDepartment Information")
        print("----------------------")
        print(f"Dept Name: {self.dt_name}")
        print(f"Dept ID: {self.dt_id}")
        print(f"Dept Location: {self.dt_loc}")
        print(f"Dept Head: {self.dt_head}")

    @classmethod
    def get_total_dept(cls):
        return cls.dept_count

# Input number of departments
dt_total = int(input("Enter the total number of departments: "))
departments = []

# Collecting department details
for i in range(dt_total):
    print(f"\nEnter details for Department {i+1}:")
    dt_name = input("Enter the dept_name: ")
    dt_id = input("Enter the dept_id: ")
    dt_loc = input("Enter the dept_loc: ")
    dt_head = input("Enter the dept_head: ")

    dept = department(dt_name, dt_id, dt_loc, dt_head)
    departments.append(dept)

# Displaying all department info
for dept in departments:
    dept.display_dept_info()

print(f"\nTotal number of departments: {department.get_total_dept()}")

# Function to search department by ID
def search_by_dept_id(dept_list, search_id):
    for dept in dept_list:
        if dept.dt_id == search_id:
            print("\nDepartment found (by ID):")
            dept.display_dept_info()
            return
    print("\nNo department found with the given ID.")

# Function to search department by Name
def search_by_dept_name(dept_list, search_name):
    for dept in dept_list:
        if dept.dt_name.lower() == search_name.lower():
            print("\nDepartment found (by Name):")
            dept.display_dept_info()
            return
    print("\nNo department found with the given Name.")

# Function to search department by Department No (assuming it's same as dept_id)
def search_by_dept_no(dept_list, search_no):
    for dept in dept_list:
        if dept.dt_id == search_no:
            print("\nDepartment found (by Department No):")
            dept.display_dept_info()
            return
    print("\nNo department found with the given Department No.")

# Example usage
search_id = input("\nSearch by Department ID: ")
search_by_dept_id(departments, search_id)

search_name = input("\nSearch by Department Name: ")
search_by_dept_name(departments, search_name)

search_no = input("\nSearch by Department No: ")
search_by_dept_no(departments, search_no)
