#########################################################################
#########               Class #1: Doctor                        #########
#########################################################################
class Doctor:
    def __init__(self):
        self.x = open("doctor.txt", mode='r')
        self.y = self.x.readlines()
        self.list1 = []
        self.nest_list = []
        self.name = []
        self.title_list = [["id","name","specilist","timing","qualification","Room Number"]]
        self.new_doctor = []


    def formatDrInfo(self):
        for line in self.y:
            if line[-1] == '\n':
                self.list1.append(line[:-1])

        return line


    def readDoctorsfile(self):
        mystring = ' '.join(map(str,self.list1))
        z = mystring.replace('_', ' ')
        a = z.split()
        self.list1 = a 
        self.nest_list = [self.list1[i:i+6] for i in range(0, len(self.list1), 6)]


    def searchDoctorById(self):
        self.id = self.list1[::6]
        b = (input("Enter the doctor Id:\n "))
        self.id_list = []
        if b in self.id:
            if b == '21':
                self.id_list.append(self.nest_list[1])
            elif b == '32':
                self.id_list.append(self.nest_list[2])
            elif b == '17':
                self.id_list.append(self.nest_list[3])
            elif b == '33':
                self.id_list.append(self.nest_list[4])
            elif b == '123':
                self.id_list.append(self.nest_list[5])
            elif b == '66':
                self.id_list.append(self.nest_list[6])
            
            self.var = self.displayDoctorsList()
        else:
            print("Can't find the doctor with the same ID on the system\n")
                
        print("Back to the prevoius Menu\n")

        

    def displayDoctorsList(self):
        for line in self.title_list:
            print("{:<3} {:<20} {:<15} {:<20} {:<20} {:<20}\n".format(line[0], line[1],line[2],line[3],line[4],line[5]))
        for line in self.id_list:
            print("{:<3} {:<20} {:<15} {:<20} {:<20} {:<20}\n".format(line[0], line[1],line[2],line[3],line[4],line[5]))

    def searchDoctorByName(self):
        self.name = []
        for each in self.nest_list:
            self.name.append(each[1])
        c = str(input("Enter the doctor name:\n "))
        self.id_list.clear()
        if c in self.name:
            if c == 'Dr.Gody':
                self.id_list.append(self.nest_list[1])
            elif c == 'Dr.Vikram':
                self.id_list.append(self.nest_list[2])
            elif c == 'Dr.Amy':
                self.id_list.append(self.nest_list[3])
            elif c == 'Dr.David':
                self.id_list.append(self.nest_list[4])
            elif c == 'Dr.Ross':
                self.id_list.append(self.nest_list[5])
            elif c == 'Dr.Mike':
                self.id_list.append(self.nest_list[6])
            
            self.var = self.displayDoctorsList()
        else:
            print("Can't find the doctor with the same name on the system\n")
            
        
        print("Back to the prevoius Menu\n")

    def displayDoctorInfo(self):
        for line in self.nest_list:
            print("{:<3} {:<20} {:<15} {:<20} {:<20} {:<20}\n".format(line[0], line[1],line[2],line[3],line[4],line[5]))

        print("Back to the prevoius Menu\n")
                


    def editDoctorInfo(self):
        edit = str(input("Please enter the id of the doctor that you want to edit their information:\n"))
        def change_doctor():
            id_input = str(input("Enter new Name: \n"))
            self.nest_list[x].clear()
            self.nest_list[x].insert(0, edit)
            self.nest_list[x].insert(1, id_input)
            special_input = str(input("Enter new Specilist in: \n"))
            self.nest_list[x].insert(2, special_input)
            timing_input = str(input("Enter new Timing:\n"))
            self.nest_list[x].insert(3, timing_input)
            qualify_input = str(input("Enter new Qualification: \n"))
            self.nest_list[x].insert(4, qualify_input)
            room_input = str(input("Enter new Room: \n"))
            self.nest_list[x].insert(5, room_input)
        if edit == '21':
            x = 1
            change_doctor()
        elif edit == '32':
            x = 2
            change_doctor()
        elif edit == '17':
            x = 3
            change_doctor()
        elif edit == '33':
            x = 4
            change_doctor()
        elif edit == '123':
            x = 5
            change_doctor()
        elif edit == '66':
            x = 6
            change_doctor()
        
        print("Back to the prevoius Menu\n")


    def addDrToFile(self):
        id_1 = (input("Enter the doctor's ID:\n"))
        self.new_doctor.append(id_1)
        doct_1 = (input("Enter the doctor's name:\n"))
        self.new_doctor.append(doct_1)
        special_1 = (input("Enter the doctor's specility:\n"))
        self.new_doctor.append(special_1)
        timing_1 = (input("Enter the doctor's timing (e.g., 7am-10pm):\n"))
        self.new_doctor.append(timing_1)
        qualify_1 =  (input("Enter the doctor's qualification:\n"))
        self.new_doctor.append(qualify_1)
        room_1 =  (input("Enter the doctor's room number:\n"))
        self.new_doctor.append(room_1)
        self.nest_list.append(self.new_doctor)

        print("Back to the prevoius Menu\n")

    
    def enterDrInfo(self):
        z = int(input("Doctor's Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n"))
        return z

#########################################################################
#########           Class #3: Laboratory                        #########
#########################################################################  
class Laboratory:
    def __init__(self):
        self.x = open("laboratories.txt", mode='r')
        self.y = self.x.readlines()
        self.list1 = []
        self.nest_list = []
        self.new_facility = []


    def addLabToFile(self):
        for line in self.y:
            if line[-1] == '\n':
                self.list1.append(line[:-1])

        return line
    

    def writeListOfLabsToFile(self):
        mystring = ' '.join(map(str,self.list1))
        z = mystring.replace('_', ' ')
        a = z.split()
        self.list1 = a 
        self.nest_list = [self.list1[i:i+2] for i in range(0, len(self.list1), 2)]


    def displayLabsList(self):
        for line in self.nest_list:
            print("{:<20} {:<20}\n".format(line[0], line[1]))

    
    def enterLaboratoryInfo(self):
        facility = (input("Enter Laboratory facility:\n"))
        self.new_facility.append(facility)
        cost = (input("Enter Laboratory cost:\n"))
        self.new_facility.append(cost)

    
    def formatLabInfo(self):
        self.nest_list.append(self.new_facility)

        
    def readLaboratoriesFile(self):
        z = int(input("Laboratories Menu\n1 - Display Laboratories list\n2 - Add Laboratory\n3 - Back to the Main Menu\n"))
        return z


#########################################################################
#########           Class #5: Management                        #########
#########################################################################
def DisplayMenu():
    text = "\nWelcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop: \n1 - 	Doctors\n2 - 	Facilities\n3 - 	Laboratories\n4 - 	Patients\n"
    print(text)
while True:
    DisplayMenu()
    order = int(input()) 
    ## create a Doctor object and display menu
    if order == 1:
        carl = Doctor()
        carl.formatDrInfo()
        carl.readDoctorsfile()
        while True:
            m = carl.enterDrInfo()
            if m == 1:
                carl.displayDoctorInfo()
            elif m == 2:
                carl.searchDoctorById()
            elif m == 3:
                carl.searchDoctorByName()
            elif m == 4:
                carl.addDrToFile()
            elif m == 5:
                carl.editDoctorInfo()
            elif m == 6:
                break
          
    ## call run_facility() function to create a Facility object and run Facility menu
    elif order == 2:
        print("\n***  Doctor Menu  ****\n")
        DisplayMenu()
        
    ## call run_labaratory() function to create a Laboratory object and display Labaratory menu
    elif order == 3:
        alex = Laboratory()
        alex.addLabToFile()
        alex.writeListOfLabsToFile()
        while True:
            m = alex.readLaboratoriesFile()
            if m == 1:
                alex.displayLabsList()
            elif m == 2:
                alex.enterLaboratoryInfo()
                alex.formatLabInfo()
            elif m == 3:
                break
        
    ## create a object of Patients class and display menu
    elif order == 4:
        print("\n*** Patients ***\n")
        
    ## program exit
    else:
        print("\n***   Program Ended !.  ***\n")
        








    













# alex = Laboratory()
# alex.addLabToFile()
# alex.writeListOfLabsToFile()
# while True:
#     m = alex.readLaboratoriesFile()
#     if m == 1:
#         alex.displayLabsList()
#     elif m == 2:
#         alex.enterLaboratoryInfo()
#         alex.formatLabInfo()
#     elif m == 3:
#         break

# carl = Doctor()
# carl.formatDrInfo()
# carl.readDoctorsfile()
# while True:
#     m = carl.enterDrInfo()
#     if m == 1:
#         carl.displayDoctorInfo()
#     elif m == 2:
#         carl.searchDoctorById()
#     elif m == 3:
#         carl.searchDoctorByName()
#     elif m == 4:
#         carl.addDrToFile()
#     elif m == 5:
#         carl.editDoctorInfo()
