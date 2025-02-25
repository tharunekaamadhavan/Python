class company:
    def display(self, name, loc):
        print("Company name: ",name,"\nCompany location: ",loc)
class employee(company):
    def display_info(self, ename,eage):
        print("Employee name: ",ename,"\nEmployee age: ",eage)
c=employee()
c.display("Tesla", "Berlin, Germany")
c.display_info("Tom", 26)
