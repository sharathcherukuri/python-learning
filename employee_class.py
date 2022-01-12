class employee:
    ##class variable###
    company = "TCS"
    ##intialization###
    ##instance variables##
    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id
    ##printing employee details####
    def print_emp_details(self):
        print("Employee ID:{0}, Employee Name: {1}, Company:{2}".
              format(self.emp_id,self.name,self.company))
        return self.emp_id,self.name,self.company
##object of employee class
e1 = employee("gowtham",123)
print(e1.print_emp_details())
        
