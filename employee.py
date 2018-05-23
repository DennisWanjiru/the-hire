class Employee(object):
    ''' Employee Class '''
    count = 1

    def __init__(self, name, email, category, password):
        self.id = Employee.count
        self.name = name
        self.email = email
        self.category = category
        self.password = password
        self.benefits = []
        self.assign_benefits()
        Employee.count += 1

    def assign_benefits(self):
        if self.category == "first":
            self.benefits = ["Office", "Accomodation"]
        else:
            self.benefits = ["Office"]
