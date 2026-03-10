"""
Have the function StringExpression(str) read the str parameter being passed which will contain the written out version of the numbers 0-9 and the words "minus" or "plus" and convert the expression into an actual final number written out as well.
For example: if str is "foursixminustwotwoplusonezero" then this converts to "46 - 22 + 10" which evaluates to 34 and your program should return the final string threefour.
If your final answer is negative it should include the word "negative."

Examples:
Input: "onezeropluseight"
Output: oneeight

Input: "oneminusoneone"
Output: negativeonezero
"""

def StringExpression(strParam):
  # create number dictionary and store operators to map
  num_map = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
  }
  ops = ["plus", "minus"]

  i = 0
  parts = []
  while i < len(strParam):
    for op in ops:
      if strParam[i:i+len(op)] == op:
        parts.append("+" if op == "plus" else "-")
        i += len(op)
        break
    else:
      # parse number
      for word, digit in num_map.items():
        if strParam[i:i+len(word)] == word:
          if parts and parts[-1].isdigit():
            parts[-1] += digit  # append digit to previous number
          else:
            parts.append(digit)
          i += len(word)
          break

  # evaluate expression
  expr = "".join(parts)
  result = eval(expr)

  # convert result back to words
  rev_map = {v: k for k, v in num_map.items()}
  negative = result < 0
  result_str = str(abs(result))
  final = "".join(rev_map[d] for d in result_str)
  if negative:
    final = "negative" + final
  return final

# keep this function call here
# print(StringExpression(input()))

# Testing:
str1 = "onezeropluseight" # "oneeight"
str2 = "oneminusoneone" # "negativeonezero"
str3 = "foursixminustwotwoplusonezero" # "threefour"

print(StringExpression(str1))
print(StringExpression(str2))
print(StringExpression(str3))