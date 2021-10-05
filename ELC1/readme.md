# Extended Learning Challenge 1

## PROBLEM

CHMOD is a command in the UNIX computer system. It is the command used for
giving users permissions to access and change files and directories. There are 3 classes of users.
They are the owner, the group and others. The permissions given are: read(r), write(w) and
execute(x).
The argument of the CHMOD command is a 3-character octal number (ex. 526). When each
digit of that number is converted to binary, the binary digits are paired to represent read, write
and execute in that order. 526 would convert to 101 010 110.
The first binary conversion gives the user permissions. The second gives the group permissions.
The third gives the others permissions. So here, the owner has read and execute permissions and
that is represented by r-x. The group has only write permission given by -w-. The others class
has read and write permissions as shown by rw-.

Putting all of the above together CHMOD 526 = 101 010 110 = r-x -w- rw-

## GOAL

### INPUT

There will be 5 lines of input. Lines 1 and 2 will each contain 3 octal digits. Lines 3 and 4 will each contain three 3-digit binary numbers. Line 5 will contain three 3-character stings.

### OUTPUT

for each line of input print the other two equivalent forms of the CHMOD result.
Print a space between each grouping as shown below.
SAMPLE INPUT SAMPLE OUTPUT

| # | Input | Output |
| :--- | :---: | :---: |
| 1 | 5, 2, 6 | 101 010 110 and r-x -w- rw- |
| 2 | 7, 3, 0 | 111 011 000 and rwx -wx --- |
| 3 | 100, 001, 101 | 4 1 5 and r-- --x r-x |
| 4 | 010, 011, 100 | 2 3 4 and -w- -wx r-- |
| 5 | r-x, rw-, rwx | 5 6 7 and 101 110 111 |
