from Doctor import Doctor

class Admin:
    """A class that deals with the Admin operations"""

    def __init__(self, username, password, address=''):
        self.__username = username
        self.__password = password
        self.__address = address

    def login(self):
        """Handles admin login"""
        print("-----Admin Login-----")
        username = input('Enter username: ')
        password = input('Enter password: ')

        if username == self.__username and password == self.__password:
            print("Login successful!")
            return True
        else:
            print("Invalid credentials. Try again.")
            return False

    def view(self, items):
        """Displays a list of items"""
        for index, item in enumerate(items):
            print(f'{index+1:3} | {item}')

    def doctor_management(self, doctors):
        """Handles doctor registration, viewing, updating, and deletion"""
        print("-----Doctor Management-----")
        print("1 - Register\n2 - View\n3 - Update\n4 - Delete")
        choice = input("Choose an option: ")

        if choice == '1':  # Register
            first_name = input("Enter Doctor's First Name: ")
            surname = input("Enter Doctor's Surname: ")
            specialty = input("Enter Specialty: ")
            doctors.append(Doctor(first_name, surname, specialty))
            print("Doctor registered successfully!")

        elif choice == '2':  # View
            print("-----List of Doctors-----")
            self.view(doctors)

        elif choice == '3':  # Update
            self.view(doctors)
            index = int(input("Enter Doctor ID to Update: ")) - 1
            if 0 <= index < len(doctors):
                field = input("Update (1: First Name, 2: Surname, 3: Specialty): ")
                if field == '1':
                    doctors[index].set_first_name(input("Enter new First Name: "))
                elif field == '2':
                    doctors[index].set_surname(input("Enter new Surname: "))
                elif field == '3':
                    doctors[index].set_speciality(input("Enter new Specialty: "))
                print("Doctor details updated!")
            else:
                print("Invalid ID.")

        elif choice == '4':  # Delete
            self.view(doctors)
            index = int(input("Enter Doctor ID to Delete: ")) - 1
            if 0 <= index < len(doctors):
                del doctors[index]
                print("Doctor deleted!")
            else:
                print("Invalid ID.")

    def view_patients(self, patients):
        """Displays all patients"""
        print("-----List of Patients-----")
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """Assigns a doctor to a patient"""
        self.view_patients(patients)
        patient_index = int(input("Select Patient ID: ")) - 1

        self.view(doctors)
        doctor_index = int(input("Select Doctor ID: ")) - 1

        if 0 <= patient_index < len(patients) and 0 <= doctor_index < len(doctors):
            patients[patient_index].link(doctors[doctor_index].full_name())
            print("Doctor assigned to patient successfully!")
        else:
            print("Invalid selection.")

    def discharge_patient(self, patients, discharged_patients):
        """Discharges a patient"""
        self.view_patients(patients)
        index = int(input("Enter Patient ID to Discharge: ")) - 1
        if 0 <= index < len(patients):
            discharged_patients.append(patients.pop(index))
            print("Patient discharged!")
        else:
            print("Invalid ID.")

    def view_discharged_patients(self, discharged_patients):
        """Displays discharged patients"""
        print("-----Discharged Patients-----")
        self.view(discharged_patients)
