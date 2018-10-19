class OurClass():

    def __init__(self, name, location, size=0, members = None):
        self.name = name
        self.location = location
        self.size = size
        if members:
            self.members = members
        else:
            self.members = []
        self.at_capacity = self.check_if_at_capacity()

    def add_class_members(self, new_member):
        self.members.append(new_member)
        self.size += 1
        if check_if_at_capacity():
            print('Capacity Reached!!')

    def check_if_at_capacity(self):
        if self.size >= 31:
            self.at_capacity = True
        else:
            self.at_capacity = False
        return self.at_capacity

    def get_num_questions_asked(self):
        total_qs = 0
        for member in self.members:
            total_qs += len(member.questions_asked)
        return total_qs

    def get_num_lines_code(self):
        total_lines = 0
        for member in self.members:
            total_lines += member.num_lines_coded
        return total_lines


###

class Member():

    def __init__(self, name, hair_color, birthdate):
        self.name = name
        self.hair_color = hair_color
        self.birthdate = birthdate
        self.questions_asked = []
        self.lines_of_code = ""
        self.num_lines_coded = 0
        self.codelevel = self.get_coding_level()

    def add_question_asked(self, question):
        self.questions_asked.append(question)

    def add_coded_line(self, code):
        self.lines_of_code.append(code)
        self.num_lines_coded += 1
        self.codelevel = self.get_coding_level()

    def get_coding_level(self):
        if self.num_lines_coded <= 100:
            self.codelevel = "beginner"
        elif self.num_lines_coded <= 1000:
            self.codelevel = "novice"
        elif self.num_lines_coded <= 10000:
            self.codelevel = "intermediate"
        else:
            self.codelevel = "master"
        return self.codelevel
