"""
Phone Number Validator

Write a function called validate_phone that checks if a string is a valid phone number
according to the following rules:

1. The phone number must be in the format: XXX-XXX-XXXX (3 digits, hyphen, 3 digits, hyphen, 4 digits)
2. All characters except hyphens must be digits
3. The first digit cannot be 0 or 1 (US area codes don't start with these)
4. The first three digits (area code) cannot be 911
5. The middle three digits cannot be all the same digit (e.g., 555)

Your function should return True if all conditions are met, and False otherwise.


"""

def validate_phone(phone_number):
    parts = phone_number.split("-") #split into parts first
    try:
        part1 = parts[0]
        part2 = parts[1]
        part3 = parts[2]

        # check part lengths
        if len(part1) != 3:
            return False
        if len(part2) != 3:
            return False
        if len(part3) != 4:
            return  False

        # check all char except hyphens are digits
        if not part1.isdigit():
            return False
        if not part2.isdigit():
            return False
        if not part3.isdigit():
            return False

        #  check first digit not 0 or 1
        if part1[0] == "1":
            return False
        if part1[0] == "0":
            return False

        # check first three digits not 911
        if part1 == "911":
            return False

        # check middle digits not same
        if part2[0] == part2[1] == part3[2]:
            return False

        return True

    except IndexError:
        return False


print(validate_phone("212-4567890"))  # False (wrong format)
print(validate_phone("123-456-7890"))  # False (area code starts with 1)
print(validate_phone("911-456-7890"))  # False (area code is 911)
print(validate_phone("212-555-3456"))  # False (middle section has all same digits)
print(validate_phone("212-456-7890"))  # True


# MORE ELEGANT
def validate_phone2(phone_number):
    parts = phone_number.split("-") #split into parts first
    try:
        part1 = parts[0]
        part2 = parts[1]
        part3 = parts[2]

        if len(part1) != 3 or len(part2) != 3 or len(part3) != 4:
            return  False
        if not part1.isdigit() or not part2.isdigit() or not part3.isdigit():
            return False
        if part1[0] == "1" or part1[0] == "0":
            return False
        if part1 == "911":
            return False
        if part2[0] == part2[1] == part3[2]:
            return False
        return True

    except IndexError:
        return False


print(validate_phone2("212-4567890"))  # False (wrong format)
print(validate_phone2("123-456-7890"))  # False (area code starts with 1)
print(validate_phone2("911-456-7890"))  # False (area code is 911)
print(validate_phone2("212-555-3456"))  # False (middle section has all same digits)
print(validate_phone2("212-456-7890"))  # True