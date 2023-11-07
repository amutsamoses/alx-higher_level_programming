0x0B. Python - Input/Output

A file is a container that stores information, right? In computer systems, a file is a contiguous set of bytes. Data in a computer system is always stored into files. Files can take different forms depending on the user requirements like data files, text files, program executable files etc.

A computer processes these files by translating them into 0s and 1s.

Every file contains three main parts:

1. Header: This contains information about the file i.e. file name, file type, file size etc.
2. Data: This is the actual information/content stored in the file.
3. End of file: This is a special character that marks the end of the file.

Also, in a file, a new line character (‘\n’) marks the end of a line or start of a new line.
Python Open File
You can open file in Python using the built-in function open().
Syntax:

open(filename, access_mode)
Python Access Modes
The second argument to open() is the access_mode. The access_mode specifies the mode in which you want to open the file. Modes include “r” for reading, “w” for writing and “a” for appending. This argument is optional and takes the default value of “r”, i.e., the read mode if we pass no value to it.

Mode	Function
r	Open a file for reading. This is the default mode.
w	Open a file for writing. If the file already exists, overwrite its contents. Create a new file if the file does not exist.
a	Open a file for appending. Preserve the file’s contents, add new data to the end of the file.
r+	Open a file for reading and writing.
w+	Allows to write as well as read from the file.
a+	Allows appending as well as reading from the file.
