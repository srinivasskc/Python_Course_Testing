print("This is module conversion program")

training = "This is a conversion program"

def yards_to_feet():
    '''
    This is Yards to Feet Conversion
    '''
    yards = float(input("Enter Yards: "))
    feet = yards * 3
    print(f"{yards} Yards is equal to {feet} Feet")


def miles_to_kms():
    '''
    This is Miles to Kms Conversion
    '''
    miles = float(input("Enter Miles: "))
    kms = miles * 1.60934
    print(f"{miles} Miles is equal to {kms} Kms")

def kms_to_miles():
    """
    This is Kms to Miles Conversion
    """
    kms = float(input("Enter Kms: "))
    miles = kms / 1.60934
    print(f"{kms} Kms is equal to {miles} Miles")
    