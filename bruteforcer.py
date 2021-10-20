import sys
import requests
from requests.models import requote_uri

version = "1.0.0"


def run(arguments):

    try:
        # add http protocol if not included  in parameter
        req = None
        url = str(arguments["-u"])
        w = str(arguments["-w"])
        if(url.split(":")[0] not in ("https", "http")):
            url = "https://" + url
        req = requests.get(url)
        print("{}  - {}".format(url, req.status_code))
        with open(w, "r") as file:
            while(True):
                line = file.readline().strip()
                if(line == ""):
                    break
                req = requests.get(f"{url}{line}",
                                   allow_redirects=False)
                print(f"{url}{line} - {req.status_code}")
    except IndexError:
        print("The host is down")


def program():
    arguments = {}
    for i in range(1, len(sys.argv)):
        if(sys.argv[i] in ("-v", "--version", "-h", "--help")):
            # just in case a -v or -h escape from the __main__
            print("Great you found a bug")
            break
        elif(sys.argv[i] in ("-u", "-w", "-p", "-t")):
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
              "-w             : wordlist\n" +
              "-p             : include port number\n" +
              "-v , --version : include port number\n" +
              "\nreport bugs and other suggetions on github page\n")
    elif(sys.argv[1] in ("-v", "--version")):
        print("Version : {}".format(version))
    else:
        program()
