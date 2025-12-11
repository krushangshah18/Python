#Strings are immutable,

s = "Hello World"

print(s[0])  #H  
print(s[-1]) #d

print(s[0:5])     # Hello
print(s[6:11])    # World
print(s[:5])      # Hello (start default = 0)
print(s[6:])      # World (end default = end)
print(s[::2])     # HloWrd (step = 2)
print(s[::-1])    # dlroW olleH (reverse string)

"""Common String Methods"""
"""
| Method          | Description           | Example                         |
| --------------- | --------------------- | ------------------------------- |
| `upper()`       | Converts to uppercase | `"hello".upper()` → `"HELLO"`   |
| `lower()`       | Converts to lowercase | `"Hi".lower()` → `"hi"`         |
| `title()`       | First letter capital  | `"hello world".title()`         |
| `strip()`       | Removes whitespace    | `"  text  ".strip()`            |
| `replace(a, b)` | Replace substring     | `"hi hi".replace("hi","hello")` |
| `find()`        | Find index            | `"apple".find("p")` → 1         |
| `count()`       | Count occurrences     | `"banana".count("a")` → 3       |
| `split()`       | Convert to list       | `"a,b,c".split(",")`            |
| `join()`        | Join list to string   | `" ".join(["Hello","World"])`   |
| `startswith()`  | Check prefix          | `"Python".startswith("Py")`     |
| `endswith()`    | Check suffix          | `"file.txt".endswith(".txt")`   |
"""

#Replace :
text = "i am an Just Intern"
new_txt = text.replace("Just","AI/ML")
print(new_txt) 

print("aaaab".replace("a", "x"))

#Split :
data = "apple,banana,cherry"
fruits = data.split(",")
print(fruits)

sentence = "Python is fun"
print(sentence.split())

#Join :
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)

anotherWord = ["DRC","is","best"]
afterJoin = " | ".join(anotherWord)
print(afterJoin)

#String Concatenation and Repetition
print("Hi" + " " + "There")   # Hi There
print("Ha" * 3)                # HaHaHa
