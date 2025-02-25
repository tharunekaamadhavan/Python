class company:
    Cmp_name=""
    def cmp(self):
         print(self.Cmp_name)
class employee_personal:
     Emp_id=""
     Address=""
     Mobile_num=""
     def emp_personal(self):
          print(self.Emp_id)
          print(self.Address)
          print(self.Mobile_num)
class Employee(company,employee_personal):
    Name=""
    def emp(self):
        print(self.Name)
class department(company,employee_personal):
    Dpt=""
    def dept(self):
         print(self.Dpt)
S1=Employee()
S2=department()
S1.Cmp_name="tesla"
S1.Name="Tharunekaa"
S1.Emp_id="253908"
S1.Mobile_num="8238238348"
S2.Dpt="AID"
S1.Address="Chennai"
S1.emp()
S1.cmp()
S2.dept()
S1.emp_personal()
