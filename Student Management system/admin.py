import csv


class Admin:

    student_details = ["Reference Number","Index Number","Student Name","Program","Level"]


    list_of_admins = ["Holison","Kirk","Simon","George"]
    admin_ids  = ["0000","1234","1111","2222"]

    student_DB = []


    def __init__(self, name_of_admin, identity):
        self.name_of_admin = name_of_admin
        self.identity = identity

    def add_student(self,Student_name,Reference,index_number,program,level):

        # append all the values receive to the student Database array
        data = [Reference,index_number,Student_name,program,level]
        for i in range(len(data)):
            self.student_DB.append(data[i])
    

        # open the csv file and append the details of the student
        with open("student_Database.csv","a",newline="") as SDB:
            writer = csv.writer(SDB,delimiter="\t")
            writer.writerows([self.student_DB])
            return
        
    def remove_student(self,reference_number):

        student_found = False
        updated_data = []
        with open("student_Database.csv", "r",newline="") as SDB:
            reader = csv.reader(SDB,delimiter="\t")
            counter = 0
            for line in reader:
                if len(line) > 0:
                    if reference_number != line[0]:
                        updated_data.append(line)
                        counter += 1
                    else:
                        student_found = True

        if student_found is True:
            with open("student_Database.csv", "w",newline="") as SDB:
                writer = csv.writer(SDB,delimiter="\t")
                writer.writerows(updated_data)
            print("Student with reference: ", reference_number, "removed successfully!")
        else:
            print("Student does not exist!")

    def print_student_DB(self): 

        with open("student_Database.csv","r",newline="") as SDB:
            reader = csv.reader(SDB,delimiter="\t")

            # print the students fields respectively
            for i in self.student_details:
                print(i, end="\t")
            print("\n--------------------------------------------------------------------------------------------")

            # print each item in each row of the student Database 
            for line in reader:
                 for column in line:
                    print(column,end="\t\t")
            print("\n")
                          

    def search_student(self,reference_number):

        with open("student_Database.csv","r",newline="") as SDB:
            reader = csv.reader(SDB,delimiter="\t")

            for line in reader:
                if len(line)>0:
                    if reference_number == line[0]:
                        print(f"Name: {line[2]}")
                        print(f"Index Number: {line[1]}")
                        print(f"Program: {line[3]}")
                        print(f"Level: {line[4]}")
                        break
            else:
                print("Student does not exist!")
                return

    def total_no_students(self):
        counter = 0

        with open("student_Database.csv","r",newline="") as SDB:
            reader = csv.reader(SDB,delimiter="\t")

            # iterate throught all the rows in the database to estimate the total number of students
            for line in reader:
                counter +=1
            print(f"The Total number of students is: {counter}")



class student():

    course200 = {"COE 272":"Dr. Henry Nunoo",
                "COE 252":"Dr. Mrs. Teresah Adjeidoo",
                "MATH 252":"Dr. Rydal Eggan",
                "COE 288":"Dr. Ing. Ransford Genesis",
                "TE 272":"Dr. Obour Agyekum"}

    def __init__(self,reference,index):
        self.reference  = reference
        self.index = index

    
    def validate_student(self,reference,index):

        with open("student_Database.csv","r",newline="") as SDB:
            reader = csv.reader(SDB,delimiter="\t")
            for line in reader:
                if len(line)>0:
                    if reference == line[0] and index == line[1]:
                        return True
                else:
                    return False

    def CL(self):

        print("Course","\t ","\t Lecturer")
        print("____________________________")
        for course in self.course200:
            print(course,"\t ",self.course200[course])
            print("\n")
