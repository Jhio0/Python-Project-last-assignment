file = open("doctor.txt", mode='r')
f = print(file.read())
class Doctor:
    
    def __init__(self, Id, Name, Special, Working_time, qualification, room_number):
        self.Id = Id
        self.list1 = []


    def formatDrInfo(self, Id):
        self.Id = open("doctor.txt", mode='r')


    
    def readDoctorsFile(self, file):
        for line in file:
            strip = line.strip()
            split = strip.split()
            self.list1.append(split)
        return split




