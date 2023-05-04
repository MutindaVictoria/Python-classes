class Student:
    name="Emily"
    age=21
    school="AkiraChix"
    nationality="Kenyan"
    first_name="Emily"
    last_name="Waeni"
    country="Kenya"

class Student:
    school="AkiraChix"
    def __init__(self,name,age,nationality,school,fullname):
        self.name =name
        self.age =age
        self.school =school
        self.nationality=nationality
        self.first_name=first_name
        self.last_name=last_name


    def greet_student(self):
        return f"Hello {self.name},welcome to {self.school },proudly {self.nationality}"

    def show_full_name(self):
        return f"Hello {self.first_name}{self.last_name} welcome to {self.school},proudly{self.nationality}"

    def years_of_birth(self):
        return f"{2023-self.age}"

    def show_initials(self.name):
        return f"{self.first_name[0].Upper()},{self.last_name[0].Upper()}"


# Update the Student Class to include these attributes - first_name, last_name, age, country
     # Add these methods to the Student class
             #- show_full_name
            # - year_of_birth
             #- show_initials

6


