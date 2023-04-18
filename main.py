import requests
import time

url = "https://ago.mo.gov/file-a-complaint/transgender-center-concerns"

skip = input("Customize form request? Y/N ")
if skip.upper() == "Y":
    f_name = input("Enter the first name for the form: ")
    l_name = input("Enter the last name for the form: ")
    address = input("Enter the address for the form: ")
    city = input("Enter the city for the form: ")
    zip = input("Enter the zip code for the form: ")
    email = input("Enter the email for the form: ")
    content = input("Enter the content for the \"report\": ")
else:
    f_name = "deez"
    l_name = "nuts"
    address = "ur moms house"
    city = "cumville"
    zip = "66669"
    email = "kiss@my.ass"
    content = "GAY SEX!!!"

count = 1
d = ""

while True:
    ## idk what hellish format this is lol but its what the actual form sends? 
    d = """
-----------------------------13683697902475703916498539963
Content-Disposition: form-data; name="TextFieldController_4"

""" + f_name + """
-----------------------------13683697902475703916498539963
Content-Disposition: form-data; name="TextFieldController_5"

""" + l_name + """
-----------------------------13683697902475703916498539963
Content-Disposition: form-data; name="TextFieldController_1"

""" + address + """
-----------------------------13683697902475703916498539963
Content-Disposition: form-data; name="TextFieldController_2"

""" + city + """
-----------------------------13683697902475703916498539963
Content-Disposition: form-data; name="DropdownListFieldController"

MO
-----------------------------13683697902475703916498539963
Content-Disposition: form-data; name="TextFieldController_6"

""" + zip + """
-----------------------------13683697902475703916498539963
Content-Disposition: form-data; name="TextFieldController_0"

""" + email + """
-----------------------------13683697902475703916498539963
Content-Disposition: form-data; name="TextFieldController_3"


-----------------------------13683697902475703916498539963
Content-Disposition: form-data; name="ParagraphTextFieldController"

""" + content + """
-----------------------------13683697902475703916498539963--

"""
    try:
        res = requests.post(url, d, timeout=2)
        if res.status_code == 200:
            print(f"Successfully sent request {count}")
        else:
            print(f"Status code {res.status_code} :(")
    except Exception as err:
        print(err)
    finally: 
        count += 1
        time.sleep(1)