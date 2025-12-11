"""
Common File Modes :
| Mode     | Meaning       | Description                                                   |
| -------- | ------------- | ------------------------------------------------------------- |
| **"r"**  | Read          | Opens file for reading (default). Error if file doesn’t exist |
| **"w"**  | Write         | Creates new file or overwrites existing                       |
| **"a"**  | Append        | Adds data to end of file. Creates if not exists               |
| **"x"**  | Create        | Creates new file but **errors if exists**                     |
| **"r+"** | Read + Write  | File must exist                                               |
| **"w+"** | Write + Read  | Creates/overwrites                                            |
| **"a+"** | Append + Read | Creates if not exists                                         |
| **"b"**  | Binary Mode   | Used with other modes for binary files (e.g., "rb", "wb")     |
"""

"""Opening Binary File"""
# f = open("sample.jpg","rb")
# data = f.read()
# f.close()
# print(type(data))  # <class 'bytes'>
# print(len(data))   # Size in bytes


"""Write operations"""
# f = open("sample.txt","w")
# f.write("Hello Line 1\n")
# f.write("Hello Line 2\n")
# f.write("Hello Line 3\n")
# f.write("Hello Line 4\n")
# f.close()

# f= open("sample.txt","a")
# f.write("Appended Line 5\n")
# f.write("Appended Line 6\n")
# f.close()

"""Read operations"""
f = open("sample.txt","r")

# content = f.read()   # reads entire file
# print(content)

# line = f.readline()  # reads one line at a time
# print(line)
# line = f.readline()  # reads one line at a time
# print(line)

# lines = f.readlines()  # reads all lines into a list
# print(lines)

f.close()

"""Using with statement (context manager) - automatically closes file"""

with open("sample.txt","r") as f:
    content = f.read()
    print(content)
# File is automatically closed outside the with block

"""iterating through file line by line"""
with open("sample.txt","r") as f:
    for line in f:
        print(line.strip())  # strip() removes extra newlines
        #OR
        # print(line,end='')  # end='' avoids double newlines