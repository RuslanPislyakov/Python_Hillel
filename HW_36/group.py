class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        # self.group.discard(last_name)
        stud_to_del = self.find_student(last_name)
        self.group.discard(stud_to_del)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for stud in self.group:
            all_students += f'{stud.last_name} {stud.first_name}\n'
        return f'Number:{self.number}\n{all_students} '