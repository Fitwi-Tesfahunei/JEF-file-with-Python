# JEF-file-with-Python
This code demonstrates how to generate a JEF file which can be read by a digital embroidery machine.
Please follow the comments on the .py file. 
An important thing to follow is that in JEF, we only read in bytes from -127 to 127, and we cannot have floating numbers.
With that in mind, when you are trying to create curves, make sure that you only use the integer parts of the floating number results.
