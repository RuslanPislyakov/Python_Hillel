class GroupStudentsAmountException(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.age}, {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, record_book: {self.record_book}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) == 10:
            raise GroupStudentsAmountException('Group can not consist of more than 10 students!')
        self.group.add(student)

    def delete_student(self, last_name):
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


gr = Group('PD1')
lst = list()
for i in range(12):
    lst.append(Student('Male', 30, 'Tom_' + str(i), 'Jobs' + str(i), 'AN142'))
    try:
        gr.add_student(lst[i])
    except GroupStudentsAmountException:
        print('The group is full! Only 10 students are allowed')

