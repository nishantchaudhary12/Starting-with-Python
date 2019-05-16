class Employee:
    def __init__(self, name, ID, department, job_title):
        self.__name = name
        self.__ID = ID
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_ID(self, ID):
        self.__ID = ID

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__ID

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title
