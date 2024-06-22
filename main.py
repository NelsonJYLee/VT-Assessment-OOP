
from patient import Patient
from test import Test


def main():
    name = input("Patient Name (Firstname Lastname): ")
    dob = input("Date of Birth (mm/dd/yyyy): ")
    age = input("Age: ")
    patient = Patient(name, dob, age)
    print(patient.patient_name, patient.date_of_birth, patient.age)

    answer_key_1 = "3759825746147637939245217537487465292364"

    continue_to_1 = input("Continue to Test 1? (y/n): ")
    if continue_to_1 == "n":
        return
     
    test_1 = Test(answer_key_1, 1)
    test_1.add_errors
    test_1.print_results



    



if __name__ == "__main__":
    main()