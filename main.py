
from patient import Patient
from test import Test
import jinja2
import pdfkit
import os
from datetime import datetime


def main():

    #Instantiate patient
    patient = Patient()
    print(patient.name, patient.dob, patient.age)

    #recording sample 1
    #37582574614763719392452175374874658923641
    #omission of 9, addition of 1, sub of 2 for 8, addition of 1

    #recording sample 2
    #632917461525374845217739214763256464759
    #addition of 1, omission of 9, sub of 7 for 6, sub 3 for 4, omission of 8

    #recording sample 3
    #25943411527835749879573714561469372672463632917462537484521179392147632574627598
    #addition of double 1, omission of 2 and 5, sub 7 for 1, sub 3 for 2

    #Answer Keys
    answer_key_1 = "3759825746147637939245217537487465292364"
    answer_key_2 = "6329174652537484521779392147632574637598"
    answer_key_3 = "25943452783574987957371456146293726724636329174652537484521779392147632574637598"

    #Total Errors
    total_errors = {
        "add_err": 0,
        "omi_err": 0,
        "sub_and_trans_err": 0
    }

    #Confirmation to begin test
    continue_to_1 = input("Continue to Test 1? (y/n): ")
    if continue_to_1 == "n":
        return
    
    #Instantiating first test, live transcription begins
    test_1 = Test(answer_key_1, 1)
    test_1.add_errors(total_errors)
    print(test_1.print_results())

    continue_to_2 = input("Continue to Test 2? (y/n): ")
    if continue_to_2 == "n":
        return

    #Instantiating second test, live transcription begins
    test_2 = Test(answer_key_2, 2)
    test_2.add_errors(total_errors)
    print(test_2.print_results())

    continue_to_3 = input("Continue to Test 3? (y/n): ")
    if continue_to_3 == "n":
        return
    
    #Instantiating third test, live transcription begins
    test_3 = Test(answer_key_3, 3)
    test_3.add_errors(total_errors)
    print(test_3.print_results())

    print(f"Total Errors: {total_errors}")

    #Test Result Calculations
    total_vertical_time = round(test_1.duration + test_2.duration)
    total_horizontal_time = test_3.rounded_duration
    adjusted_horizontal_time = round(test_3.duration * (80/(80 - total_errors["omi_err"] + total_errors["add_err"])))
    total_errors_num = sum(total_errors.values())
    DEM_ratio = round(adjusted_horizontal_time/total_vertical_time, 2)

    #Confirmation to create pdf
    make_pdf = input("Make PDF? (y/n): ")
    if make_pdf == "n":
        return
    
    print("Creating PDF...")
    
    #context for pdf.html
    context = {
        "patient_name": patient.name,
        "date_of_birth": patient.dob,
        "age": patient.age,
        "answer_key_1": answer_key_1,
        "marker_results_1": test_1.marker_results['marked_numbers'],
        "rounded_duration_1": test_1.rounded_duration,

        "answer_key_2": answer_key_2,
        "marker_results_2": test_2.marker_results['marked_numbers'],
        "rounded_duration_2": test_2.rounded_duration,

        "answer_key_3": answer_key_3,
        "marker_results_3": test_3.marker_results['marked_numbers'],
        "rounded_duration_3": test_3.rounded_duration,

        "sub_and_trans_err": total_errors["sub_and_trans_err"],
        "omi_err": total_errors["omi_err"],
        "add_err": total_errors["add_err"],

        "total_vertical_time": total_vertical_time,
        "total_horizontal_time": total_horizontal_time,
        "adjusted_horizontal_time": adjusted_horizontal_time,
        "total_errors_num": total_errors_num,

        "DEM_ratio": DEM_ratio
    }

    #html to pdf set-up
    template_loader = jinja2.FileSystemLoader("./")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("pdf.html")
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")

    #custom filenames and directory path
    current_date = datetime.now().strftime("%Y-%m-%d")
    output_filename = f"{patient.name}_{current_date}.pdf"
    output_directory = f"patient_pdf"

    output_path = os.path.join(output_directory, output_filename)

    #making pdf and storing it in the output path
    pdfkit.from_string(output_text, output_path, configuration=config)

    print("Finished!")


if __name__ == "__main__":
    main()