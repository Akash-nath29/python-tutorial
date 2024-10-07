# Writing into a text file
# Step 1: Open the file
# Step 2: Write something
# Step 3: Close the file

f = open("test.txt", "a")
f.write("\nLots of loveeee <3")
f.close()


with open("test.txt", "r") as f:
    print(f.read())

# Modes

# ‘r’	Open text file for reading. Raises an I/O error if the file does not exist.
# ‘r+’	Open the file for reading and writing. Raises an I/O error if the file does not exist.
# ‘w’	Open the file for writing. Truncates the file if it already exists. Creates a new file if it does not exist.
# ‘w+’	Open the file for reading and writing. Truncates the file if it already exists. Creates a new file if it does not exist.
# ‘a’	Open the file for writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
# ‘a+’	Open the file for reading and writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
# ‘rb’	Open the file for reading in binary format. Raises an I/O error if the file does not exist.
# ‘rb+’	Open the file for reading and writing in binary format. Raises an I/O error if the file does not exist.
# ‘wb’	Open the file for writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
# ‘wb+’	Open the file for reading and writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
# ‘ab’	Open the file for appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.
# ‘ab+’	Open the file for reading and appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.