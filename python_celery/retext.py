import re


def generate_data():
    """
    Generate 4 types of data alphabet, alphanumeric, float, integer using regex
    """
    # Generate alphabetic data
    alphabetic_data = re.sub(r'[^a-zA-Z]', '', input("Enter alphabetic data: "))
    print(alphabetic_data)
    # Generate alphanumeric data
    alphanumeric_data = re.sub(r'[^a-zA-Z0-9]', '', input("Enter alphanumeric data: "))
    print(alphanumeric_data)
    # Generate float data
    float_data = re.sub(r'[^0-9.]', '', input("Enter float data: "))
    print(float_data)
    # Generate integer data
    integer_data = re.sub(r'[^0-9]', '', input("Enter integer data: "))
    print(integer_data)
    return alphabetic_data, alphanumeric_data, float_data, integer_data
