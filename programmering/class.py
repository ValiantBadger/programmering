
class Elev:
    def __init__(self, f_name : str, l_name : str, clas : int, sex :str, grade : list):
        self.f_name = f_name
        self.l_name = l_name
        self.clas = clas
        self.sex = sex
        self.grade = grade
    def __str__(self):
        return f"{self.f_name}"

        


    def info(self):
        print(self.f_name, self.l_name, "class", self.clas, self.sex,"grades are", self.grade)

    def calc_grade(self):

        suma = sum(self.grade)
        suma /= len(self.grade)
        print (suma)

    def add_grade(self):
        x = int(input ("ADD grade wat: "))
        self.grade.append(x)

class Klassroom:
    def __init__(self, name : str, student : list):
        self.name = name
        self.student = student

    def students(self):
        self.student.append(person1)
        self.student.append(person2)
        self.student.append(person3)
        self.student.append(person4)
        self.student.append(person5)
        self.student.append(person6)
        print (self.student)

    def info1 (self):
         print(self.name, self.student)




person1 = Elev("Alvin", "Granlund", 10,"his", [6,6,6,6,6,6])
person2 = Elev("Alka", "Trast", 11,"it's", [1,1,1,5,1,1])
person3 = Elev("Frina", "Albertsson", 10,"her", [4,3,5,2,6,7])
person4 = Elev("Abraham", "Trast", 8,"kitten", [3,5,2,5,4,3])
person5 = Elev("Uberna", "Yntax", 9, "alt", [5,5,5,5,5,1])
person6 = Elev("Orewer", "Poler", 11, "dc_mod", [3,5,1,5,4,3])
klass1 = Klassroom("S1", [])
klass1.students()
person1.info()
person1.calc_grade()
person1.add_grade()
person1.info()
klass1.info()




