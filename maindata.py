class Doctor: #doctor class
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

        print(line)


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



class Patient:
    #init function which starts by reading the patients.txt file
    def __init__(self):
        self.readPatientsFile()
    
    #formats lists made by the enterPatientInfo method and takes it as a parameter, the list is formatted into string with each piece of info being separated by an underscore and returns a string
    def formatPatientInfo(self, patientlist):
        formattedpatient = (f"{patientlist[0]}_{patientlist[1]}_{patientlist[2]}_{patientlist[3]}_{patientlist[4]}")
        return formattedpatient

    #contains input statements that gathers the information on the patient, then is added to a list, then, it returns the list
    def enterPatientInfo(self):
        id = int(input("Enter Patient ID:\n\n"))
        name = input("Enter Patient name:\n\n")
        disease = input("Enter Patient disease:\n\n")
        gender = input("Enter Patient gender:\n\n")
        age = int(input("Enter Patient age:\n\n"))
        patientlist = [id, name, disease, gender, age]
        return patientlist

    #method that opens the patients.txt file in reading and writing mode
    def readPatientsFile(self):
        self.file = open("files/patients.txt", "r+")

    #method that searches the patient by the inputted ID number
    def searchPatientById(self):
        patient_id = int(input("Enter the patient Id:\n"))
        return patient_id

    #method that uses the searchPatientbyID method and displays the information of that Patient
    def displayPatientInfo(self):
        id = self.searchPatientById()
        if id in self.info:
            for self.pid in self.info:
                print(self.info[self.pid])
        else:
            print("Can't find the Patient with the same ID on the system")

    #method that uses the searchPatientbyID method and edits the information of that patient 
    def editPatientInfo(self):
        id =self.searchPatientById()
    
    #method that displays each line of the patients.txt file by splitting the string into a list and formatting each index on the list into a tabular format using a formatted string and prints the list
    def displayPatientsList(self):
        for line in self.file:
            self.info = line.split("_")
            print(f"{self.info[0].upper():5}{self.info[1]:18}\t{self.info[2]:10}\t{self.info[3]:10}\t{self.info[4]}")

    #method that takes the formatted patient information and appends it in the patients.txt file
    def writeListOfPatientsToFile(self, addpatient):
        self.file.read()
        self.file.write(f"\n{addpatient}")
        self.file.close()

    #method that asks for the patient information, formats the information, and appends the information into the patients.txt file usinf the enterPatientInfo, formatPatientInfo, and writeLitsofPatienstToFile methods
    def addPatientToFile(self):
        patientinfo_list = self.enterPatientInfo()  
        addpatient = self.formatPatientInfo(patientinfo_list)
        self.writeListOfPatientsToFile(addpatient)

class Laboratory: #laboratory class
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


#Facility class
class Facility:
    #init function that starts by reading the facilities.txt file
    def __init__(self):
        self.readFacilitiesFile()

    #method that opens the facilities.txt file in reading and writing mode
    def readFacilitiesFile(self):
        self.file = open("facilities.txt", "r+")

    #method that asks for the facility name the user wants to add and uses the writeListOffacilitiesToFile method to append to the facilities.txt file    
    def addFacility(self):
        addfacility = input("Enter Facility Name:\n")
        self.writeListOffacilitiesToFile(addfacility)

    #displays each line of the facilities.txt file
    def displayFacilities(self):
        for line in self.file:
            print(line)

    #method that takes the addfacility input statement as a parameter, and appends to the facilities.txt in a new line
    def writeListOffacilitiesToFile(self, addfacility):
        self.file.read()
        self.file.write(f"\n{addfacility}")
        self.file.close()
        
#Menu that asks for the users input for their desired selection, classes are initiated and the corresponding methods are applied depending on the users input
def DisplayMenu():
    menu = int(input("Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop:\n1 -\tDoctors\n2 -\tFacilities\n3 -\tLaboratories\n4 -\tPatients\n\n"))
    while menu in range(1,5):
        if menu == 1:
            doctor = Doctor()
            doctor.formatDrInfo()
            doctor.readDoctorsfile()
            while True:
                m = doctor.enterDrInfo()
                if m == 1:
                    doctor.displayDoctorInfo()
                elif m == 2:
                    doctor.searchDoctorById()
                elif m == 3:
                    doctor.searchDoctorByName()
                elif m == 4:
                    doctor.addDrToFile()
                elif m == 5:
                    doctor.editDoctorInfo()
                elif m == 6:
                    break
        elif menu == 2:
            facility = Facility()
            facility_menu = int(input("Facilities Menu:\n1 - Display Facilities List\n2 - Add Facility\n3 - Back to Main Menu\n"))
            while facility_menu in range(1,4):
                if facility_menu == 1:
                    facility.displayFacilities()
                elif facility_menu == 2:
                    facility.addFacility()
                else:
                    break
                facility_menu = int(input("Facilities Menu:\n1 - Display Facilities List\n2 - Add Facility\n3 - Back to Main Menu\n"))
            else:
                print("Invalid Input")
        elif menu == 3:
            laboratory = Laboratory()
            laboratory.addLabToFile()
            laboratory.writeListOfLabsToFile()
            while True:
                m = laboratory.readLaboratoriesFile()
                if m == 1:
                    laboratory.displayLabsList()
                elif m == 2:
                    laboratory.enterLaboratoryInfo()
                    laboratory.formatLabInfo()
                elif m == 3:
                    break
        elif menu == 4:
            patient = Patient()
            patient_menu = int(input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n\n"))
            while patient_menu in range(1,5):
                if patient_menu == 1:
                    patient.displayPatientsList()
                elif patient_menu == 2:
                    patient.displayPatientInfo()
                elif patient_menu == 3:
                    patient.addPatientToFile()
                elif patient_menu == 4:
                    patient.editPatientInfo()
                else:
                    break
                patient_menu = int(input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n\n"))
            else:
                print("Invalid Input")
        else:
            break
        menu = int(input("Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop:\n1 -\tDoctors\n2 -\tFacilities\n3 -\tLaboratories\n4 -\tPatients\n\n"))

DisplayMenu()