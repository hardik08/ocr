# Load the necessary packages
import cv2
import imutils
import pytesseract
import re


# Prepare the image
def prepare_image():

    # Get the image
    image = cv2.imread("images\\nj\\nj1.jpg")

    # Prepare the image
    ratio = image.shape[0] / 500.0
    orig = image.copy()
    image = imutils.resize(image, height=500)

    # convert the image to grayscale, blur it and find edges in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    topHat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
    blackHat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

    add = cv2.add(gray, topHat)
    # substract = cv2.subtract(add, blackHat)

    return add


# Definition to extract text from image
def text_extractor():
    # Parse the text from the image to text

    add = prepare_image()
    text = pytesseract.image_to_string(add)

    # Convert the text string into a list by splitting them at new line break
    text_array = text.split('\n')

    # Remove all the null/blank elements from the list
    text_array = [x for x in text_array if x.strip()]

    # Printing the list
    print(text_array)

    # Getting the state from the list
    # First element will always be a State
    state = text_array[0]

    # Print the state
    # print("State: ", state)

    # Separating the parsing based on the state name
    # For New York
    if 'YORK' in state:
        # Give the state name to avoid any noise in the state names
        state_name = "New York"
        print("State: ", state_name)

        # Print the address
        address = text_array[5] + " " + text_array[6]
        print("Address: ", address)

        # Print the name
        name = text_array[4] + " " + text_array[3]
        name = ''.join(e for e in name if e.isalpha() or e.isspace())
        print("Name: ", name)

        # Print the license id/number
        license_number = text_array[2]
        license_number = re.sub('[^0-9]', '', license_number)
        print("License Number: ", license_number)

        # Print the date of birth
        dob = text_array[8]
        dob_list = dob.split(" ")
        print("Date of Birth: ", dob_list[-1])

        # Print the expiry date and issuance date
        expiry_dt = text_array[9]
        dt_list = expiry_dt.split(" ")
        print("Expiry Date: ", dt_list[-1])

    # For New Jersey
    if 'JERSEY' in state:
        # Give the state name to avoid any noise in the state names
        state_name = "New Jersey"
        print("State: ", state_name)

        # Print the address
        address = text_array[6] + " " + text_array[7]
        print("Address: ", address)

        # Print the name
        name = text_array[5] + " " + text_array[4]
        name = ''.join(e for e in name if e.isalpha() or e.isspace())
        print("Name: ", name)

        # Print the license id/number
        license_number = text_array[1]
        license_number = re.sub('[^0-9]', '', license_number)
        print("License Number: ", license_number)

        # Print the date of birth
        dob = text_array[2]
        dob_list = dob.split(" ")
        dob = dob_list[-2]
        print("Date of Birth: ", dob_list[-2])

        # Print the expiry date and issuance date
        dt = text_array[3]
        dt_list = dt.split(" ")
        expiry_dt = dt_list[-1]
        issue_dt = dt_list[-3]
        print("Issue Date: ", dt_list[-3])
        print("Expiry Date: ", dt_list[-1])

    # For California
    if 'Cali' in state:
        # Give the state name to avoid any noise in the state names
        state_name = "California"
        print("State: ", state_name)

        # Print the address
        address = text_array[5] + " " + text_array[6]
        print("Address: ", address)

        # Print the name
        name = text_array[4] + " " + text_array[3]
        name = ''.join(e for e in name if e.isalpha() or e.isspace())
        print("Name: ", name)

        # Print the license id/number
        license_number = text_array[1]
        license_number = re.sub('[^0-9]', '', license_number)
        print("License Number: ", license_number)

        # Print the date of birth
        dob = text_array[7]
        print("Date of Birth: ", dob)

        # Print the expiry date and issuance date
        expiry_dt = text_array[2]
        print("Expiry Date: ", expiry_dt)

    # For Arizona
    if 'izo' in state:
        # Give the state name to avoid any noise in the state names
        state_name = "Arizona"
        print("State: ", state_name)

        # Print the address
        address = text_array[5] + " " + text_array[6]
        print("Address: ", address)

        # Print the name
        name = text_array[4] + " " + text_array[3]
        name = ''.join(e for e in name if e.isalpha() or e.isspace())
        print("Name: ", name)

        # Print the license id/number
        license_number = text_array[1]
        license_number = re.sub('[^0-9]', '', license_number)
        print("License Number: ", license_number)

        # Print the date of birth
        dob = text_array[2]
        print("Date of Birth: ", dob)

        # Print the expiry date and issuance date
        expiry_dt = text_array[7]
        print("Expiry Date: ", expiry_dt)

    # For Massachusetts
    if 'MASS' in state:
        # Give the state name to avoid any noise in the state names
        state_name = "Massachusetts"
        print("State: ", state_name)

        # Print the address
        address = text_array[9] + " " + text_array[11]
        print("Address: ", address)

        # Print the name
        name = text_array[7] + " " + text_array[8]
        name = ''.join(e for e in name if e.isalpha() or e.isspace())
        print("Name: ", name)

        # Print the license id/number
        license_number = text_array[3]
        license_number = re.sub('[^0-9]', '', license_number)
        print("License Number: ", license_number)

        # Print the date of birth
        dob = text_array[4]
        print("Date of Birth: ", dob)

        # Print the expiry date and issuance date
        expiry_dt = text_array[4]
        print("Expiry Date: ", expiry_dt)

    return text_array, state, state_name, address, name, license_number, dob, expiry_dt


text_array, state, state_name, address, name, license_number, dob, expiry_dt = text_extractor()

print(text_array)
print("Unrefined state: ", state)
print("State: ", state_name)
print("Address: ", address)
print("Name: ", name)
print("License Number: ", license_number)
print("Date of Birth: ", dob)
print("Expiry Date: ", expiry_dt)
