import sys
import requests

version = "1.0.0"


def run(arguments):
    print(arguments)


def program():
    arguments = {}
    for i in range(1, len(sys.argv)):
        if(sys.argv[i] in ("-v", "--version", "-h", "--help")):
            # just in case a -v or -h escape from the __main__
            print("Great you found a bug")
            break
        elif(sys.argv[i] in ("-u", "-d", "-p", "-t")):
            # above loop prevent from entering useless commands
            try:
                arguments[sys.argv[i]] = sys.argv[i+1]
            except IndexError:
                print("check your syntax once again ( IndexError )")
    run(arguments)


if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print("HEy bro, Y0u must use those commands in --help or -h :)")
    elif(sys.argv[1] in ("-h", "--help")):
        print("usage: bruteforcer [option] ... [-h help | <filename> ]\n\n" +
              "Options and arguments are as follows\n\n" +
              "-h , --help    : display help and exists\n" +
              "-u             : insert destination address\n" +
              "-p             : include port number\n" +
              "-v , --version : include port number\n" +
              "\nreport bugs and other suggetions on github page\n")
    elif(sys.argv[1] in ("-v", "--version")):
        print("Version : {}".format(version))
    else:
        program()
