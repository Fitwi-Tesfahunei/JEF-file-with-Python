# JEF-file-with-Python
This code demonstrates how to generate a JEF file which can be read by a digital embroidery machine.
Please follow the comments on the .py file. 
An important thing to follow is that in JEF, we only read in bytes from -127 to 127, and we cannot have floating numbers.
With that in mind, when you are trying to create curves, make sure that you only use the integer parts of the floating number results.
The code generates the following pattern.
![Screenshot 2022-03-12 205717](https://user-images.githubusercontent.com/69972019/158945316-5868508a-3741-4d2d-9111-ed0db3dcd038.jpg)
![5868568156077930047_121](https://user-images.githubusercontent.com/69972019/158945356-4d61ca69-8c66-4e95-87b3-e43afccc0729.jpg)
