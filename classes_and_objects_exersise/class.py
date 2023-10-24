class Class:
    __students_count = 22

    def __init__(self, class_name):
        self.class_name = class_name
        self.name_list = []
        self.grade_list = []

    def add_student(self, name: str, grade: float):
        if len(self.name_list) < Class.__students_count:
            self.name_list.append(name)
            self.grade_list.append(grade)

    def get_average_grade(self):
        return round(sum(self.grade_list) / len(self.grade_list), 2)

    def __repr__(self):
        return f"The students in {self.class_name}: {', '.join(self.name_list)}. Average grade: {sum(self.grade_list) / len(self.grade_list):.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("George", 6.00)
a_class.add_student("Kura mi", 6.00)
print(a_class.get_average_grade())
print(a_class)
