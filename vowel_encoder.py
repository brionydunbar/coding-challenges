"""
Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:
a -> 1
e -> 2
i -> 3
o -> 4
u -> 5

For example, encode("hello") would return "h2ll4".
There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.
"""

def encode(st):
    for char in st:
        st = st.replace("a", "1")
        st = st.replace("e", "2")
        st = st.replace("i", "3")
        st = st.replace("o", "4")
        st = st.replace("u", "5")
    return st

def decode(st):
    for char in st:
        st = st.replace("1", "a")
        st = st.replace("2", "e")
        st = st.replace("3", "i")
        st = st.replace("4", "o")
        st = st.replace("5", "u")
    return st


print(encode("hello"))
print(decode("h3 th2r2"))