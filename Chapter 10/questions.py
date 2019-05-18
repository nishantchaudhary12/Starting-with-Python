class Questions:
    def __init__(self, ques, options, correct):
        self.__ques = ques
        self.__options = options
        self.__ans1 = options[0]
        self.__ans2 = options[1]
        self.__ans3 = options[2]
        self.__ans4 = options[3]
        self.__correct = correct
        self.__item = list()
        self._answer = 0

    def set_ques(self, ques):
        self.__ques = ques

    def set_ans1(self, options):
        self._ans1 = options[0]

    def set_ans2(self, options):
        self._ans2 = options[1]

    def set_ans3(self, options):
        self._ans3 = options[2]

    def set_ans4(self, options):
        self._ans4 = options[3]

    def set_correct(self, correct):
        self._correct = correct

    def get_ques(self):
        return self.__ques

    def get_ans1(self):
        return self.__ans1

    def get_ans2(self):
        return self.__ans2

    def get_ans3(self):
        return self.__ans3

    def get_ans4(self):
        return self.__ans4

    def get_correct(self):
        return self.__correct

    def correct_answer(self, ans):
        if self.__options[ans-1] == self.__correct:
            return True
