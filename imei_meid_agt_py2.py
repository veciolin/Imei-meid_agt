#!/usr/bin/python2
#
# Date : 2018/12/17
# Author : Vecio.lin
#


import sys, getopt, csv , os

usage = '''
imei.py usage:
    imei.py <options> (option-args)
    Options arguments:
        -h/--help                           this help screen.
        -m/--mode                           mode:0->imei 1->meid
        -f/--from                           the first number.
        -n/--number                         how many numbers you wanna generate.
        '''

def prase_command(argv):
    mode = ''
    first_number = ''
    number = ''
    try:
        opts, args = getopt.getopt(argv,"hm:f:n:",["help=","mode=","from=","number="])
    except getopt.GetoptError:
        print (usage)
        sys.exit()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print (usage)
            sys.exit()
        elif opt in ("-f", "--from"):
            first_number = arg
        elif opt in ("-n", "--number"):
            number = arg
        elif opt in ("-m", "--mode"):
            mode = arg
    return (mode,first_number,number)

def imeichecksum(digit_str):
  sum1 = 0
  sum2=0
  total=0
  temp = 0
  checksum = 0

  for i in range(len(digit_str)):
    if i%2==0:
        sum1 = sum1 + ord(digit_str[i]) - ord('0')
    else:
        temp = (ord(digit_str[i]) - ord('0')) * 2
        if temp < 10:
            sum2 = sum2 + temp
        else:
            sum2 = sum2 + 1 +temp -10

  total = sum1 + sum2

  if total%10 == 0 :
    checksum = 0
  else :
    checksum = 10 - total%10

  digit_str = digit_str + str(checksum)

  return digit_str

def generate_imei(first,num):
    # Get the first number
    print("")
    print("==================================")
    print("==================================")
    print("=====IMEI generate process...=====")
    print("==================================")
    print("")
    count=0
    while ((not first.isdigit()) or len(first)!=14) :
        if count :
            print("What you enter is illegal,Please retry.")
        count = count+1
        print("Please enter the first_number(14 bits):")
        first = raw_input()

    count=0
    while not num.isdigit():
        if count :
            print("What you enter is illegal,Please retry.")
        count = count + 1
        print("Please enter how much you want to generate:")
        num = raw_input()

    csvFileName = os.getcwd() + "/imei.csv"
    try:
        os.remove(csvFileName)
    except:
        #print("Unexpected error:", sys.exc_info()[0])
        pass

    for i in range(int(num)):
        temp = str(int(first) + i)
        complete_imei = imeichecksum(temp)
        complete_imei = complete_imei + '\t'
        with open(csvFileName,"a+",newline="") as datacsv:
            csvwriter = csv.writer(datacsv,dialect = ("excel"))
            csvwriter.writerow([complete_imei])

    print("")
    print("")
    print("Already generate",num,"imei number,","Please check",csvFileName)


def generate_meid(first,num):
    print("")
    print("==================================")
    print("==================================")
    print("=====MEID generate process...=====")
    print("==================================")
    print("")

    try:
       int(first,16)
    except:
       first = ''
    count=0
    while ((not first.isalnum()) or len(first)!=14) :
        if count :
            print("What you enter is illegal,Please retry.")
        count = count+1
        print("Please enter the first_number(14 bits):")
        first = raw_input()
        try:
            int(first,16)
        except:
            first = ''

    count=0
    while not num.isdigit():
        if count :
            print("What you enter is illegal,Please retry.")
        count = count + 1
        print("Please enter how much you want to generate:")
        num = raw_input()

    csvFileName = os.getcwd() + "/meid.csv"
    try:
        os.remove(csvFileName)
    except:
        #print("Unexpected error:", sys.exc_info()[0])
        pass
    for i in range(int(num)):
        temp = str(hex(int(first,16) + i))
        complete_meid = temp[2:].zfill(14) + '\t'
        complete_meid = complete_meid.upper()
        with open(csvFileName,"a+",newline="") as datacsv:
            csvwriter = csv.writer(datacsv,dialect = ("excel"))
            csvwriter.writerow([complete_meid])

    print("")
    print("")
    print("Already generate",num,"meid number,","Please check",csvFileName)


if __name__ == "__main__":
    first_number = ''
    number = ''
    mode = ''
    (mode,first_number,number) = prase_command(sys.argv[1:])

    if mode == '':
        mode = input("Please enter what type you want to generate(0/IMEI 1/MEID):");
    print("")

    if mode == "0" or mode == "IMEI" :
        generate_imei(first_number,number)
    elif mode == "1" or mode == "MEID" :
        generate_meid(first_number,number)
    else :
        print("What you enter is illegal!!!!!!")
        print("Fuck you,Re-run it.")
