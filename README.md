## imei/meid agt.

### description.

This is a process about generate the imei/meid automatic.

Available in python2/python3 versions.

### How to use it.

if you want to generate the imei,you must provide some parameters as below:

mode : 0->imei 1->meid.
first number : the first number you want to generate.
number : how many numbers you want to generate.

after that, the program will generate it and save as csv file.

and you can provide parameter in two ways,in command line or input in the command windows.

for example:

```
python imei_meid_agt_py3.py -m 0 -f 12345678901234 -n 100
python imei_meid_agt_py3.py -mode 0 -from 12345678901234 -number 100
```

if you do not provide the parameters with command line,when you run the process,you can enter the parameter in the command.

for example:

```
$ python imei_meid_agt_py3.py
Please enter what type you want to generate(0/IMEI 1/MEID):IMEI


==================================
==================================
=====IMEI generate process...=====
==================================

Please enter the first_number(14 bits):
12345678901234
Please enter how much you want to generate:
100


Already generate 100 imei number, Please check C:\Users\Vecio\Desktop/imei.csv
```

### note.
* you know, the python2 and the python3 is different.Therefore,
	please run the imei_meid_agt_py2.py with python2.
	please run the imei_meid_agt_py3.py with python3.

* i already test the program in ubuntu 16.04 and windows 10 with python3.I have not tried other platforms. 

### Others.
If you have other questions, Please contact me ~
I would be happy to discuss them together ~