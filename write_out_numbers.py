"""
Create a function that transforms any positive number to a string representing the number in words.
The function should work for all numbers between 0 and 999999.

Should have hyphens between numbers between 100 e.g. twenty-nine
"""

def number2words(n):
    ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
    teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    if any(not x.isdigit() for x in str(n)):
        return ''

    if n <= 10:
        return ones[n]
    if 11 <= n <= 19:
        return teens[n]
    elif n < 100:
        if n % 10 == 0:
            return tens[n]
        else:
            return tens[(n // 10) * 10] + '-' + ones[(n % 10)]
    elif n < 1000:
        if n % 100 == 0:
            return ones[(n // 100)] + ' hundred'
        else:
            return ones[(n // 100)] + ' hundred ' + number2words(n % 100)
    else:
        if n % 1000 == 0:
            return number2words(n // 1000) + ' thousand'
        else:
            return number2words(n // 1000) + ' thousand ' + number2words(n % 1000)

    return ''

print(number2words(22))
print(number2words(456))
print(number2words(10376))