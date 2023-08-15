# map()
ls = [1, 2, 3]
def square(num):
    return num * 2
data = map(square, ls)
print(data)
print(type(data))
for x in data:
    print(x)

ls = [96, 69]
print(''.join(list(map(str, ls))))

a = [[96], [69]]
print(''.join(list(map(str, a))))

# Input data: List of dictionaries
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function. Do not change this.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
   ### WRITE SOLUTION CODE HERE
   str_list = []
   for item in map(mod, employee_list):
      str_list.append(item)
   return str_list

for x in to_mod_list(employee_list):
    print(x)


def generate_usernames(mod_list):
   usernames = [ username.replace(" ", "_") for username in mod_list]
   return usernames

   raise NotImplementedError()

def map_id_to_initial(employee_list):
   map_dic = {employee['name'][0]: employee['id'] for employee in employee_list}
   return map_dic
   raise NotImplementedError()

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")

   print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

   print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers))
print(small)