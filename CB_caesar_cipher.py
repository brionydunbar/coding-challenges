"""
Have the function CaesarCipher(str,num) take the str parameter and perform a Caesar Cipher shift on it using the num parameter as the shifting number.
A Caesar Cipher works by shifting each letter in the string N places in the alphabet (in this case N will be num).
Punctuation, spaces, and capitalization should remain intact.
For example if the string is "Caesar Cipher" and num is 2 the output should be "Ecguct Ekrjgt".

Examples:
Input: "Hello" & num = 4
Output: Lipps

Input: "abc" & num = 0
Output: abc

"""

def CaesarCipher(strParam,num):
  text = strParam
  result = ""
  num = num % 26 # normalise shift to within alphabet
  # check if char is alpha
  for char in text:
    if char.isalpha():
      if char.isupper():
        result += chr((ord(char) - ord("A") + num) % 26 + ord("A"))
      else:
        result += chr((ord(char) - ord("a") + num) % 26 + ord("a"))
    else:
      result += char
  return result


# keep this function call here
# print(CaesarCipher(input()))


# Testing:
str1 = "Hello"
num1 = 4 # "Lipps"

str2 = "abc"
num2 = 0 # "abc"

str3 = "world!"
num3 = 1 # "xpsme!"

str4 = "no change"
num4 = 0 # "no change"

str5 = "some change"
num5 = 1 # "tpnf dibohf"

str6 = "byte-dash"
num6 = 0 # "byte-dash"

str7 = "coderBYTE"
num7 = 2 # "eqfgtDAVG"

print(CaesarCipher(str1, num1))
print(CaesarCipher(str2, num2))
print(CaesarCipher(str3, num3))
print(CaesarCipher(str4, num4))
print(CaesarCipher(str5, num5))
print(CaesarCipher(str6, num6))
print(CaesarCipher(str7, num7))