# Import the entire "gspread" library
# So I can access any function, class or method within it
import gspread
# Import the "Credentials" class which is part of the "service_account"
# function from the "google.oauth2" library
from google.oauth2.service_account import Credentials

# Set the scope
# The scope lists the API's that the program should acces in order to run
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Create another constant variable named "CREDS"
# Call the "from_service_account_file" method of the "Credentials" class
# and pass it "creds.json"
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

# sales = SHEET.worksheet("sales")

# data = sales.get_all_values()

# print(data)


def get_sales_data():
    """ 
    Get sales figures input from the user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10, 20, 30, 40, 50, 60\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")


get_sales_data()