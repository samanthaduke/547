def interface():
    print("Blood Test Analysis")
    keep_running = True
    while keep_running:
        print("Options")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
            keep_running = False
    return  

interface()


def accept_input(test_name)
    entry = input("Enter the {}test result: ".format(test_name))
    return int(entry)



def check_HDL(HDL_value):
    if HDL >= 60
        answer = "Normal"
    elif 60 > HDL >= 40
        answer = "Borderline Low"
    else HDL < 40
        answer = "Low"
    return answer
    
def print_result(test_name, test_value, test_class):
    out_string = "The test value of {} for {} is {}".format(test_value, test_name, test_class)
    print(out_string)
    return

def HDL_driver():
    HDL_value = accept_input("HDL")
    classificaton = check_HDL(HDL_value)
    print_result("HDL", HDL_value, classificaton)
    return


interface()