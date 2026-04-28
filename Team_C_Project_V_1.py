#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This code is critical for functions that require the date and time
from datetime import datetime

# Person class. Skelaton of other 'people' classes(doctor, nurse & patient).
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

# doctor class. 
class Doctor(Person):
    def __init__(self, first_name, last_name, specialty, phone, doctor_id, password):
        super().__init__(first_name, last_name)
        self.specialty = specialty 
        self.phone = phone 
        self.doctor_id = doctor_id 
        self.password = password 

# This is the hardcoded doctor's list. It also includes the default doctor
doctors = [
    Doctor("Rafa", "Younis", "Cardiology", "6025551234", "Doc101", "pass101"),
    Doctor("Sarah", "Smith", " Pediatrics", "4805552314", "Doc102", "pass102"),
    Doctor("Micheal", "lee", "Neurology", "6236668899", "Doc103", "pass103"),
    Doctor("Emily", "Davis", "Dermatology", "5206669934", "doc104", "pass104")
]
default_doctor = Doctor("Chief", "Doctor", "General", "6027277546", "chief", "12345")
doctors.append(default_doctor)

#Nurse Class
class Nurse(Person):
    def __init__(self, first_name, last_name, password, floor_number):
        super().__init__(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.__nurse_password = password # password (pre determined)
        self.floor_number = floor_number
        self.__nurse_id = first_name + last_name + str(floor_number) #login username (auto gen'd using full name + floor num)

    def full_name(self): # For formal greetings after login
        return f"{self.first_name} {self.last_name}"

    def create_patient(self): # Prompts several info to make a new patient
        print("Ready to create Patient. Please enter following details:")
        new_id = int(len(patients) + 1)
        new_first_name = input("[1/5] Enter patient first name: ")
        new_last_name = input("[2/5] Enter patient last name: ")
        new_age = int(input("[3/5] Enter patient age: "))
        new_admit_address = (input("[4/5] Enter patient's admittance date (Full month, Day): "))
        new_admit_date = str(input("[5/5] Enter patient address: "))

        patients.append(Patient(new_first_name, new_last_name, new_id, new_age, new_admit_address, new_admit_date))
        print("Patient created")


    def view_patient(self): #views patient general info
        view_id = int(input("Please enter ID of patient for details: ")) 
        found = False

        for patient in patients:
            if patient.patient_id == view_id: # scrolls through patient list until the patient's id matches the id you're looking for
                patient.retrieve_patient_info()
                found = True
                break

        if not found:
            print(f"No patient found with ID: {view_id}")

    def view_meds(self): # Patrick, this is where I left off (1/2)
        view_id = int(input("Please enter ID of patient for details: ")) 
        found = False

        for patient in patients:
            if patient.patient_id == view_id: # scrolls through patient list until the patient's id matches the id you're looking for
                print(f"")
                found = True
                break

        if not found:
            print(f"No patient found with ID: {view_id}")

    def view_vitals(self): # Patrick, this is where I left off (2/2)
        view_id = int(input("Please enter ID of patient for details: ")) 
        found = False

        for patient in patients:
            if patient.patient_id == view_id: # scrolls through patient list until the patient's id matches the id you're looking for
                print(f"") # I don't know what I need to print yet - leaving this as I am unavailable
                found = True #Setting this to true prevents "not found" code from happening
                break

        if not found: # if ID is not found, print that fact lol
            print(f"No patient found with ID: {view_id}")


    def get_nurse_id(self):
        return self.__nurse_id

    def get_nurse_pw(self):
        return self.__nurse_password

# This is the hardcoded nurse's list
nurses = [
    Nurse("Place", "Holder", "AdjustingIndexes", 0), #Placeholder to avoid "index minus one" instances
    Nurse("Mikan", "Tsumiki", "evilteddybear", 1),
    Nurse("Lisa", "Garland", "quietplease", 2),
    Nurse("Sally", "Smithson", "daylightallergy", 1)]

# Class of all the paitients and their data
class Patient(Person):
    def __init__(self, first_name, last_name, patient_id, age, admit_date, med_costs, patient_doctor, address, lab_tests, vitals, medications, status):
        super().__init__(first_name, last_name)
        self.patient_id = patient_id
        self.age = age
        self.admit_date = admit_date
        self.med_costs = med_costs
        self.doctor = patient_doctor
        self.address = address
        self.lab_tests = lab_tests if lab_tests is not None else []
        self.vitals = vitals if vitals is not None else []
        self.medications = medications if medications is not None else []
        self.discharge_status = status

    # Get's the redacted version of the patient name to display to the patient
    def get_info_patient(self):
        print(f'{self.first_name[0]}*** {self.last_name[0]}***')

# This is the hardcoded list of the patients
patients = [
    Patient("John", "Smith", 1, 65, "March 3", 5, "Chief", "1600 Pennsylvania Ave NW", [], [], [], False),
    Patient("Patrica", "Jones", 2, 73, "February 9", 1000000000, "Chief", "300 West Anchient St", [], [], [], False),
    Patient("Someone", "Something", 3, 10, "April 7", 30, "Chief", "900 Water Way", [], [], [], False),
    Patient("Zack", "Xylophone", 4, 45, "December 31", 990, "Chief", "3409 W Apach Blvd", [], [], [], False)
]

# Doctor Module Function
# This function checks doctor id and password
# If doctor correct allow access
# If wrong show invalid message
def login ():
    doc_id = input("Enter Doctor ID:").strip()
    password = input("Enter password:").strip()
    for doctor in doctors:
        if doctor.doctor_id == doc_id and doctor.password == password:
            print("login sucessful.welcome to the HIS")
            print("\nDoctor Module")
            print("0. exit")        
            print("1. create new doctor")
            print("2. create patient")
            print("3. view all patients")
            print("4.order lab test")
            print("5.Add Patient Vitals")
            print("6.Update Patient Vitals")
            print("7.View Patient Vitals")
            print("8.Add Patient Medicine")
            print("9.Update Patient Medicine")   
            print("10.Delete Patient Medicine")
            print("11.Print Patient Information")        
            print("12.Discharge")

            choice  = input("enter your choice:")

            if choice == "0":
                exit_HIS()
            elif choice == "1":
                create_doctor()
            elif choice == "2":
                create_patient()
            elif choice == "3":
                view_all_patients()
            elif choice == "4":
                order_lab_test()
            elif choice == "5":
                vitals_manager.add_vital()
            elif choice == "6":
                vitals_manager.update_vitals()
            elif choice == "7":
                vitals_manager.view_vitals()
            elif choice == "8":
                med_manager.prescribe_med()
            elif choice == "9":
                med_manager.update_med()
            elif choice == "10":
                med_manager.delete_med()    
            elif choice == "11":
                finder = Find_print_patient(patients)
                finder.search_patient()
            elif choice == "12":
                doctorDischarge(patients).pDischarge()
            else: 
                print("invalid choice.")
        else:
            print("Invalid Login")


#create new_doctor function.
# This creates a new doctor and adds doctor to list
def create_doctor():
    first_name = input("Enter first name:")
    last_name = input("Enter last name:")
    specialty = input("Enter specialty:")
    phone = input(" Enter phone number:")
    doctor_id = input("Enter doctor id:")
    password = input("Enter password:")

    new_doctor = Doctor(first_name , last_name, specialty, phone, doctor_id, password)
    doctors.append(new_doctor)
    print("doctor created successfully.")


# create patient function. 
# This function creates a new patient and add patient to list
def create_patient():
    first_name = input(" Enter patient first name:")
    last_name = input(" Enter patient last name:")
    patient_id = input(" Enter patient id:") 
    patient_age = input("Enter patient age:")
    patient_admit_date = input("Enter patient admit date:")
    patient_med_costs = input("Enter patient med costs:")
    patient_doctor = input("Enter patient doctor:")
    patient_address = input("Enter patient address:")



    new_patient = Patient(first_name, last_name, patient_id, patient_age, patient_admit_date, patient_med_costs, patient_doctor, patient_address, [], [], [], False)
    patients.append(new_patient)
    print("patient created successfully.")

#Order lab test function.
# This function finds a patient and adds alab test
# It also upadtes the taotale medaical cost
def order_lab_test():
    patient_name = input(" Enter patient first name:")

    for patient in patients:
        if patient. first_name == patient_name:
            test_name = input("Enter lab test name:")
            cost = float(input("Enter test cost:"))

            patient.lab_tests.append((test_name, cost))
            patient.med_costs += cost

            print("Lab test ordered sucessfully.")
            return 

    print("patient not found.")

# View patients function:
# This function displays all patients details (name, age, ect,)
def view_all_patients():
    if not patients:
        print("No patient found.")
        return


    print("\===== all patients details =====")


    for patient in patients:
        print("\n---------")
        print("First Name:", patient.first_name)
        print("Last Name:", patient.last_name)
        print("Patient ID:", patient.patient_id)
        print("Age:", patient. age)
        print("Admit Date:", patient.admit_date)
        print("Medical Cost:", patient.med_costs)
        # if len(patient.lab_tests) == 0:
        #     print("No lab tests recorded for this patient.")
        # else:
        #     print("Lab tests:", patient.lab_tests)
        # if len(patient.allergies) == 0:
        #     print("No akkergies recorded for this patient.")
        # else:
        #     print("Alleriges:", patient.allergies)
        # if len(patient.allergies) == 0:
        #     print("No allergies recorded for this patient.")
        # else:
        #     print("Lab tests:", patient.lab_tests)

#Discharge patient.
# This function removes patients from the system. 
# Pass back the data for discharging the patient.

# ***Delete this***

class Discharge:
    def __init__(self, patient):
        self.patient = patient
        self.date = datetime.now()

    def p_sum(self):
        d_format = self.date.strftime("%Y-%m-%d %H:%M:%S")
        summary = (
            f"Patient Record\n"
            f"Patient Name: {self.patient.first_name} {self.patient.last_name}\n"
            f"Patient ID: {self.patient.patient_id}\n"
            f"Age: {self.patient.age}\n"
            f"Admit Date: {self.patient.admit_date}\n"
            f"Discharge Date: {d_format}\n"
            f"Attending Doctor: {self.patient.doctor}\n"
            f"Address: {self.patient.address}\n"
            f"Medical Costs: ${self.patient.med_costs}\n"
            f"Lab Tests: {', '.join(self.patient.lab_tests) if self.patient.lab_tests else 'None'}\n"
            f"Medications: {', '.join(self.patient.medications) if self.patient.medications else 'None'}\n"
        )

        return summary


# Initiate the discharge through creating the file.

class doctorDischarge:
    def __init__(self, p_list):
        self.patients = p_list

    def pDischarge(self):

        try:
            pid = int(input("Enter patient ID to discharge: "))
        except ValueError:
            print("Invalid ID.")
            return

        # Scan through patients find pid...
        patient = None
        for p in self.patients:
            if p.patient_id == pid:
                patient = p
                break

        if patient is None:
            print("\nNo patient was found.")
            return

        # Create record
        record = Discharge(patient)
        summary = record.p_sum()

        # Create the file
        date_str = datetime.now().strftime("%Y%m%d")
        filename = f"{patient.first_name.lower()}{patient.last_name.lower()}_discharged_{date_str}.txt"

        # Write to the file
        with open(filename, "w") as file:
            file.write(summary)

        # Remove patient from system
        self.patients.remove(patient)

        print("\nPatient was discharged successfully!")
        print(f"Discharge file created: {filename}")

# Nurse Module Function
def run_nurse():
    print("\nHello Nurse, please enter login details:")

    username_attempt = input("Username: ")

    logged_in_nurse = None

    for nurse in nurses:
        if username_attempt.lower() == nurse.get_nurse_id().lower():
            password_attempt = input(f"{nurse.full_name()}, please enter your password: ")

            if password_attempt == nurse.get_nurse_pw():
                logged_in_nurse = nurse
            break

    if not logged_in_nurse:
        print("Invalid Credentials.")
        print("Valid nurse usernames are:")
        for n in nurses:
            print(" -", n.get_nurse_id())
        return

    while True:
        print(f"\nWelcome {logged_in_nurse.full_name()}. What would you like to do today?")
        user_input = input(f"(0) Exit HIS  |  (1) Create Patient  |  (2) View Patient General Info | (3) View Patient Meds | (4) View Patient Vitals | (5) Add Patient Vitals | (6) Update Patient Vitals | (7) Print Patient Details")

        if user_input == "0":
            print("Thank you for visting the HIS!")
            break
        elif user_input == "1":
            logged_in_nurse.create_patient()

        elif user_input == "2":
            logged_in_nurse.view_patient()

        elif user_input == "3":
            logged_in_nurse.view_meds()

        elif user_input == "4":
            logged_in_nurse.view_vitals()

        elif user_input == "5":
            vitals_manager.add_vital()

        elif user_input == "6":
            vitals_manager.update_vitals()

        elif user_input == "7":
            finder = Find_print_patient(patients)
            finder.search_patient()

# Patient Module Function
def run_patient():
    print("Welcome to the Patient Module!")
    while True:
        selection = input("Please type in your Patient ID, or press 0 to return back to the main menu: ")

        if selection == "0":
            break

        try:
            selection = int(selection)
        except ValueError:
            print("Please try again. Only enter numbers.")
            continue

        # Search for patient
        patient_id = None
        for p in patients:
            if p.patient_id == selection:
                patient_id = p
                break

        if patient_id is None:
            print("No Patient Found. Please Try Again.")
            continue

        # Patient found
        print("I found your information!")
        patient_id.get_info_patient()

        print("1. Current Medical Expenses")
        print("2. View Medications")
        print("3. View Vitals")
        print("0. Return to Main Menu")

        try:
            choice = int(input("Please choose an option: "))
        except ValueError:
            print("Invalid Input. Please only type numbers.")
            continue

        if choice == 1:
            print(f'Total medical expenses: ${patient_id.med_costs}')
            print("Returning to main menu.")
            continue
        elif choice == 2:
            med_manager.view_med(role)
        elif choice == 3:
            vitals_manager.view_vitals(role)
        elif choice == 0:
            break
        else:
            print("Invalid choice. Try again.")

def search_patient():
    while True:
        search = input("Please Type in the Patient ID of the Patient to retrieve his or her information")
        if search == "0":
            break
        try:
            search = int(search)
        except ValueError:
            print("Error. Please type in the patient ID.")
            continue

        patient_id = None
        for p in patients:
            if p.patient_id == search:
                patient_id = p
                patient_id.retrieve_patient_info()
                break

        if patient_id is None:
            print("Patient Not Found. Try Again.")
            continue

# Medince Function
class Medication:
    # This defines what a medication is in the system, initializes all the information for the medication
    def __init__(self, name, dosage, route, frequency):
        self.__name = name
        self.__dosage = dosage
        self.__route = route
        self.__frequency = frequency

    # When the med is created, its just an object, this turns that object into something readable for the user
    def __str__(self):
        return f'{self.__name}, {self.__dosage}, {self.__route}, {self.__frequency}'

    # This is protection against any duplicate meds in case the patient is already prescribed that medication
    def duplicate_med(self, other):
        return str(self).lower() == str(other).lower()

    # All 4 of these are for the update meds so if they dont want to change one of the parts of the medication, it returns the unchanged value
    def get_name(self):
        return self.__name

    def get_dosage(self):
        return self.__dosage

    def get_route(self):
        return self.__route

    def get_frequency(self):
        return self.__frequency


class MedicationManager:
    # This creates a list of meds per patient when called, it is tied to specific patient ids
    def __init__(self):
        self.patient_meds = {}

    # A login function for the doctor so they can access the doctor only functions
    def doctor_login(self):
        doc_id = input("Enter Doctor ID: ").strip()
        password = input("Enter password: ").strip()

        # Goes through all the doctors in the doctor list and if the id and password match any doctors it logs them in
        for doctor in doctors:
            if doctor.doctor_id.lower() == doc_id.lower() and doctor.password == password:
                print("Login successful.")
                return True

        print("Invalid login.")
        return False

    # Function for the patient ids, it helps to eliminate code repition so that you can just call the function for patient id
    def get_patient_id(self):
        view_id = input("Please enter patient ID: ").strip()

        # Prevents user from leaving patient id blank
        while view_id == "":
            print("Patient ID cannot be blank.")
            view_id = input("Please enter patient ID: ").strip()

        # Prevents user from entering non-numerical value
        try:
            view_id = int(view_id)
        except ValueError:
            print("Patient ID must be a number.")
            return None

        # Goes through patients in patient list to see if said patient id exists 
        for patient in patients:
            if patient.patient_id == view_id:
                print(f"Patient {view_id} found.")
                return view_id

        print(f"No patient found with ID: {view_id}")
        return None

    # The prescribe med function allows doctors to ,well, prescribe meds to each patient
    def prescribe_med(self):
        # Checks to see if user is logged in as a doctor
        if not self.doctor_login():
            return

        view_id = self.get_patient_id()
        if view_id is None:
            return

        med_name = input("Enter medication name: ").strip()

        # Prevents user from leaving med name blank
        while med_name == "":
            print("Med name cannot be blank.")
            med_name = input('Please enter med name: ').strip()

        dosage = input("Enter dosage: ").strip()

        # Prevents user from leaving dosage blank
        while dosage == "":
            print("Dosage cannot be blank.")
            dosage = input('Please enter dosage: ').strip()

        route = input("Enter route (PO, IV, Injection): ").strip().lower()

        # This while loop prevents the user from inputting something random for the route
        while route not in ['po', 'iv', 'injection']:
            print(f'Invalid route. Please only enter PO, IV, or Injection for route.')
            route = input("Enter route (PO, IV, Injection): ").strip().lower()

        # Turns the route into a clean display format before storing it
        if route == "po":
            route = "PO"
        elif route == "iv":
            route = "IV"
        else:
            route = "Injection"

        frequency = input("Enter frequency: ").strip()

        # Prevents user from leaving frequency blank
        while frequency == "":
            print("Frequency cannot be blank.")
            frequency = input('Please enter frequency: ').strip()

        new_med = Medication(med_name, dosage, route, frequency)

        # This checks to see if the patient already has meds or not, and if not creates an empty med list for the patient
        if view_id not in self.patient_meds:
            self.patient_meds[view_id] = []

        # This checks to see no duplicate meds are being prescribed to the patient
        for med in self.patient_meds[view_id]:
            if med.duplicate_med(new_med):
                print(f'Same medication is already listed for this patient.')
                return 

        self.patient_meds[view_id].append(new_med)
        print(f"Patient {view_id}'s medication list has been updated.")

    # This allows the doctors, nurses, and patients view the patient's medication
    def view_med(self):        
        view_id = self.get_patient_id()
        if view_id is None:
            return

        # Checks to see if the patient's meds they are looking for actually exist or not
        if view_id not in self.patient_meds or len(self.patient_meds[view_id]) == 0:
            print(f'No medication found for this patient.')
            return

        print('\nMedications:')

        # Prints each med for the patient 
        for med in self.patient_meds[view_id]:
            print(med)

    # This function allows doctors to update a patient's meds if there was a misinput, change of medication, and so on
    def update_med(self):
        # Checks to see if user is logged in as a doctor
        if not self.doctor_login():
            return

        view_id = self.get_patient_id()
        if view_id is None:
            return

        # Checks to see if patient actually has meds or not
        if view_id not in self.patient_meds or len(self.patient_meds[view_id]) == 0:
            print(f'No medication found for this patient.')
            return

        print('\nMedications:')

        # Creates a list of the patients meds tied to a specific number that allows the doctor to easily change the meds
        for number in range(len(self.patient_meds[view_id])):
            print(f"{number}: {self.patient_meds[view_id][number]}")

        # Makes sure the program doesnt crash if the user doesnt choose a valid option when prompted to choose from different options
        try:
            index = int(input(f'Please enter the number of the medication to update: '))
        except ValueError:
            print("Invalid choice.")
            return

        # Does the same thing as above but handles errors where the user input a valid number, but its not in the list provided
        if index < 0 or index >= len(self.patient_meds[view_id]):
            print("Invalid choice.")
            return

        print("\nEnter new medication details:")
        old_med = self.patient_meds[view_id][index]

        new_med_name = input("Enter new medication name, or press Enter to keep current: ").strip()

        # Allows the user to leave this field blank if it doesnt need to be changed
        if new_med_name == "":
            new_med_name = old_med.get_name()

        new_dosage = input("Enter new dosage, or press Enter to keep current: ").strip()

        # Allows the user to leave this field blank if it doesnt need to be changed
        if new_dosage == "":
            new_dosage = old_med.get_dosage()

        new_route = input("Enter new route (PO, IV, Injection), or press Enter to keep current: ").strip().lower()

        # Allows the user to leave this field blank if it doesnt need to be changed
        if new_route == "":
            new_route = old_med.get_route()
        else:
            while new_route not in ['po', 'iv', 'injection']:
                print('Invalid route. Please only enter PO, IV, or Injection.')
                new_route = input("Enter route (PO, IV, Injection): ").strip().lower()

            # Turns the route into a clean display format before storing it
            if new_route == "po":
                new_route = "PO"
            elif new_route == "iv":
                new_route = "IV"
            else:
                new_route = "Injection"

        new_frequency = input("Enter new frequency, or press Enter to keep current: ").strip()

        # Allows the user to leave this field blank if it doesnt need to be changed
        if new_frequency == "":
            new_frequency = old_med.get_frequency()

        new_med = Medication(new_med_name, new_dosage, new_route, new_frequency)

        # Goes through each med in the patient's list and checks if the patient already has that medication
        for i in range(len(self.patient_meds[view_id])):
            if i != index and self.patient_meds[view_id][i].duplicate_med(new_med):
                print("This medication is already listed for this patient.")
                return

        self.patient_meds[view_id][index] = new_med
        print("Medication updated.")

    # Function for deleting meds
    def delete_med(self):
        # Checks to see if user is logged in as a doctor
        if not self.doctor_login():
            return

        view_id = self.get_patient_id()
        if view_id is None:
            return

        # Makes sure the patient has medication to delete
        if view_id not in self.patient_meds or len(self.patient_meds[view_id]) == 0:
            print(f'No medication found for this patient.')
            return

        print(f'\nMedications:')

        # Provides a list of medication for the user to choose from and delete the medication
        for number in range(len(self.patient_meds[view_id])):
            print(f' {number}: {self.patient_meds[view_id][number]}')

        # Handles non-numeric inputs
        try:
            index = int(input(f'Please enter the number of the medication you wish to delete: '))
        except ValueError:
            print(f'Invalid choice.')
            return

        # Handles numeric inputs not in the range of whats provided
        if index < 0 or index >= len(self.patient_meds[view_id]):
            print(f'Invalid choice.')
            return

        deleted_med = self.patient_meds[view_id].pop(index)
        print(f'Deleted: {deleted_med}')

        # If the patient has no more medication left in their list after the doctor delete the medication, the list gets deleted 
        # so theres no empty lists
        if len(self.patient_meds[view_id]) == 0:
            del self.patient_meds[view_id]

med_manager = MedicationManager()

# Vitals Function
class Vital:
    # Initializes a single vital, records the name, value, and time when it was entered
    def __init__(self, vital_name, value):
        self.__vital_name = vital_name
        self.__value = value
        self.timestamp = datetime.now()

    # Updates vital value and adds a new timestamp
    def update_value(self, new_value):
        self.__value = new_value
        self.timestamp = datetime.now()

    # Returns vital name, value, and when it was entered
    def display(self):
        formatted_time = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.__vital_name}: {self.__value} | Entered {formatted_time}"

class VitalsManager:
    # Creates a dict to store all of the patient specific vitals
    def __init__(self):
        self.patient_vitals = {}

     # A login function for the doctor so they can access the doctor only functions
    def doctor_login(self):
        doc_id = input("Enter Doctor ID: ").strip()
        password = input("Enter password: ").strip()

        # Goes through all the doctors in the doctor list and if the id and password match any doctors it logs them in
        for doctor in doctors:
            if doctor.doctor_id.lower() == doc_id.lower() and doctor.password == password:
                print("Login successful.")
                return True

        print("Invalid login.")
        return False

    # A login function for the nurse so they can access the nurse only functions
    def nurse_login(self):
        nurse_id = input("Enter Nurse ID: ").strip()
        password = input("Enter password: ").strip()

        # Goes through all the nurses in the nurse list and if the id and password match any nurses it logs them in
        for nurse in nurses:
            if nurse.get_nurse_id().lower() == nurse_id.lower() and nurse.get_nurse_pw() == password:
                print("Login successful.")
                return True

        print("Invalid login.")
        return False

    # Function for nurse and doctors to login
    def staff_login(self):
        role = input("Enter role (doctor/nurse): ").strip().lower()

        # Runs the doctor/nurse login depending on user input
        if role == "doctor":
            return self.doctor_login()
        elif role == "nurse":
            return self.nurse_login()
        else:
            print("Invalid role.")
            return False

    # Function for the patient ids, it helps to eliminate code repition so that you can just call the function for patient id
    def get_patient_id(self):
        view_id = input("Please enter patient ID: ").strip()

        # Prevents user from leaving patient id blank
        while view_id == "":
            print("Patient ID cannot be blank.")
            view_id = input("Please enter patient ID: ").strip()

        # Prevents user from entering non-numerical value
        try:
            view_id = int(view_id)
        except ValueError:
            print("Patient ID must be a number.")
            return None

        # Goes through patients in patient list to see if said patient id exists 
        for patient in patients:
            if patient.patient_id == view_id:
                print(f"Patient {view_id} found.")
                return view_id

        print(f"No patient found with ID: {view_id}")
        return None

    # This is for adding vitals to a patient 
    def add_vital(self):
       # Checks to see if user is logged in as a doctor or nurse
        if not self.staff_login():
            return

        view_id = self.get_patient_id()
        if view_id is None:
            return

        # Creates an empty vital list for patient if they dont already have one
        if view_id not in self.patient_vitals:
                self.patient_vitals[view_id] = []

        # Clears old vitals so the patient only has one set of current vitals
        self.patient_vitals[view_id] = []

        vital_names = ['height', 'weight', 'bp', 'pulse', 'temperature']

        # Goes through all the vitals in this list^^ and asks the user to enter a value
        for vital in vital_names:
            value = input(f'Please enter {vital}: ').strip()

            # Prevents user from leaving vital value blank
            while value == "":
                print("Value cannot be blank.")
                value = input(f'Please enter {vital}: ').strip()

            new_vital = Vital(vital, value)
            self.patient_vitals[view_id].append(new_vital)

        print('Vitals added.')

    # View vitals function to allow people to view patients vitals
    def view_vitals(self):    
        view_id = self.get_patient_id()
        if view_id is None:
            return

        else:
            print(f"\nVitals for patient {view_id}:")

        if view_id not in self.patient_vitals or len(self.patient_vitals[view_id]) == 0:
            print("No vitals found for this patient.")
            return

        # Goes through each vital in the patients list and uses the display function to show it to the user
        for vital in self.patient_vitals[view_id]:
            print(vital.display())

    # Function for updating vitals if there is a typo, or new information, etc
    def update_vitals(self):
        # Checks to see if user is logged in as a doctor or nurse
        if not self.staff_login():
            return

        view_id = self.get_patient_id()
        if view_id is None:
            return

        if view_id not in self.patient_vitals or len(self.patient_vitals[view_id]) == 0:
            print("No vitals found for this patient.")
            return

        print(f'\nCurrent Vitals for patient {view_id}')

        # Prints the patients vitals attached to a different number to make it easy to choose with vital to update
        for number in range(len(self.patient_vitals[view_id])):
            print(f'{number}: {self.patient_vitals[view_id][number].display()}')

        # This handles input errors if the user enter a nonnumerical value
        try:
            index = int(input('Enter the number of the vital you wish to update: '))
        except ValueError:
            print('Invalid choice')
            return

        # This handles if the user enters a number outside of what's displayed
        if index < 0 or index >= len(self.patient_vitals[view_id]):
            print('Invalid choice')
            return

        new_value = input('Please enter new value: ').strip()

        # Prevents user from leaving vital value blank
        while new_value == "":
            print("Value cannot be blank.")
            new_value = input(f'Please enter new value: ').strip()

        self.patient_vitals[view_id][index].update_value(new_value)

        print('Vital updated successfully.')

vitals_manager = VitalsManager()

# Print Patient Function
# This class will help to print the patient's information
class Print:
    def __init__(self, patient):
        self.patient = patient
        self.date = datetime.now()

    # This function will print the information in the .txt file
    def print_patient(self):
        date = self.date.strftime("%Y-%m-%d %H:%M:%S")
        patient_info = (
            f"Patient Record\n"
            f"Patient Name: {self.patient.first_name} {self.patient.last_name}\n"
            f"Patient ID: {self.patient.patient_id}\n"
            f"Age: {self.patient.age}\n"
            f"Admit Date: {self.patient.admit_date}\n"
            f"Attending Doctor: {self.patient.doctor}\n"
            f"Address: {self.patient.address}\n"
            f"Medical Costs: ${self.patient.med_costs}\n"
            f"Lab Tests: {', '.join(str(v) for v in self.patient.lab_tests) if self.patient.lab_tests else 'None'}\n"
            f"Vitals: {', '.join(str(v) for v in self.patient.vitals) if self.patient.vitals else 'None'}\n"       
            f"Medications: {', '.join(str (v) for v in self.patient.medications) if self.patient.medications else 'None'}\n"
        )

        return patient_info


# This class is to help find the patient
class Find_print_patient:
    def __init__(self, patient_list):
        self.patients = patient_list

    # This is the function to actually search for the patient
    def search_patient(self):

        try:
            patient_id = int(input("Enter patient ID: "))
        except ValueError:
            print("Invalid ID.")
            return

        # Scan through the patients find the right patient
        patient = None
        for p in self.patients:
            if p.patient_id == patient_id:
                patient = p
                break

        if patient is None:
            print("\nNo patient was found.")
            return

        # Create a record that has the patient info
        record = Print(patient)
        summary = record.print_patient()

        # Create the file
        date_str = datetime.now().strftime("%Y%m%d")
        filename = f"{patient.first_name.lower()}{patient.last_name.lower()}_{date_str}.txt"

        # Write the file
        with open(filename, "w") as file:
            file.write(summary)

        print("\nPatient information was successfully printed!")
        print(f"Patient information file: {filename}")


# Discharge Function
class Discharge:
    def __init__(self, patient):
        self.patient = patient
        self.date = datetime.now()

    def p_sum(self):
        d_format = self.date.strftime("%Y-%m-%d %H:%M:%S")
        summary = (
            f"Patient Record\n"
            f"Patient Name: {self.patient.first_name} {self.patient.last_name}\n"
            f"Patient ID: {self.patient.patient_id}\n"
            f"Age: {self.patient.age}\n"
            f"Admit Date: {self.patient.admit_date}\n"
            f"Discharge Date: {d_format}\n"
            f"Attending Doctor: {self.patient.doctor}\n"
            f"Address: {self.patient.address}\n"
            f"Medical Costs: ${self.patient.med_costs}\n"
            f"Lab Tests: {', '.join(self.patient.lab_tests) if self.patient.lab_tests else 'None'}\n"
            f"Vitals: {', '.join(self.patient.vitals) if self.patient.vitals else 'None'}\n"        
            f"Medications: {', '.join(self.patient.medications) if self.patient.medications else 'None'}\n"
        )

        return summary


# Initiate the discharge through creating the file.

class doctorDischarge:
    def __init__(self, p_list):
        self.patients = p_list

    def pDischarge(self):

        try:
            pid = int(input("Enter patient ID to discharge: "))
        except ValueError:
            print("Invalid ID.")
            return

        # Scan through patients find pid...
        patient = None
        for p in self.patients:
            if p.patient_id == pid:
                patient = p
                break

        if patient is None:
            print("\nNo patient was found.")
            return

        # Create record
        record = Discharge(patient)
        summary = record.p_sum()

        # Create the file
        date_str = datetime.now().strftime("%Y%m%d")
        filename = f"{patient.first_name.lower()}{patient.last_name.lower()}_discharged_{date_str}.txt"

        # Write to the file
        with open(filename, "w") as file:
            file.write(summary)

        # Remove patient from system
        self.patients.remove(patient)

        print("\nPatient was discharged successfully!")
        print(f"Discharge file created: {filename}")


def exitDischarge():
        dDischarge = doctorDischarge(patients)

        while True:
            print("\nDischarge & Exit Module")
            print("1. Discharge Patient")
            print("0. Return to Main Menu")

            choice = input("Enter choice: ")

            if choice == "1":
                dDischarge.pDischarge()

            elif choice == "0":
                main_module()
                return


            else:
                print("Invalid choice.")

# This function allows the user to exit the program
def exit_HIS():
    print("Thank you for visiting the HIS!")

# Main Module
def main_module():
    while True:
        print("Hi! Welcome to the Health Information System! At any time, press 0 to exit the Health Information System")
        selection = input("Please choose a selection: (0) Exit HIS | (1) Doctor | (2) Nurse | (3) Patient | (4) Discharge & Exit: ")

        if selection == "0":
            exit_HIS()

        try:
            selection = int(selection)
        except ValueError:
            print("Error. Make sure to only enter numbers.")
            continue

        if selection == 1:
            login()
        elif selection == 2:
            run_nurse()
        elif selection == 3:
            run_patient()
        elif selection == 4:
            print("Only doctors can discharge patients.")
            print("0. Exit HIS")  
            print("1. Continue to Doctor Login")
            print("2. Return to Main Menu")            
            option = input("Please make a selection:")

            try:
                option = int(option)
            except ValueError:
                print("Error. Make sure to only enter numbers.")
                continue

            if option == 0:
                exit_HIS()
                return

            if option == 1:
                login()

            elif option == 2:
                continue

        else:
            print("Please type in a number between 0 and 4.")
            continue



main_module()


# In[ ]:




