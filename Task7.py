class MedicalRecord:
    def __init__(self, record_id, details):
        self.record_id = record_id
        self.details = details

class Patient:
    def __init__(self, patient_id, name, record_id, record_details):
        self.patient_id = patient_id
        self.name = name
        self.medical_record = MedicalRecord(record_id, record_details)

    def get_record(self):
        return f"Record {self.medical_record.record_id}: {self.medical_record.details}"

class Doctor:
    def __init__(self,doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.patients= [] #Aggreaiton

    def add_patient(self, patient):
        self.patients.append(patient) 


    def list_patients(self):
            return [p.name for p in self.patients]
        
class Department:
    def __init__(self, name):
        self.name = name 
        self.doctors = [] #Composition

    def add_doctor(self, doctor):
        self.doctors.append (doctor)
    
    def list_doctors (self):
        return [d.name for d in self.doctors]
    
class Hospital:
    def __init__(self, name):
        self.name = name
        self.department = [] #Composition

    def add_department(self, department):
        self.department.append(department)

    def list_departments(self):
        return [d.name for d in self.department]
    
#Create a hostpital
hospital = Hospital("City Hospital")

#Crearte depatments
dept1 = Department("Cardiology")
dept2 = Department("Neurology")

#Add departments to hospital
hospital.add_department(dept1)
hospital.add_department(dept2)

#Create doctors 
doc1 = Doctor(101, "Dr. Ali", "Cardiology")
doc2 = Doctor(102, "Dr. Sam", "Neurology")

#Add doctors to departments
dept1.add_doctor(doc1)
dept2.add_doctor(doc2)

#Create patients
patient1 = Patient(1, "billy", 1001, "Heart condition")
patient2 = Patient(2, "Emma", 1002, "Migraine")

#Assign patients to doctors 
doc1.add_patient(patient1)
doc2.add_patient(patient2)

#Print hospital structure
print("Departments in hospital:", hospital.list_departments())
print("Doctors in Cardiology:", dept1.list_doctors())
print("Doctors in Neurology:", dept2.list_doctors())
print("Patients of Dr. Ali:", doc1.list_patients())
print("Medical record of Emma:", patient2.get_record())


    

