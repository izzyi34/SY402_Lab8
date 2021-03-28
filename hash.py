import os
import hashlib
from datetime import datetime

ignore = ["/usr", "/boot", "/bin", "/etc", "/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run"]


def first_time():
    csvFile = open("hashes.csv", "w")
    for root, dirs, files in os.walk("/", topdown=True):
        #dirs[:] = [d for d in dirs if d not in ignore]
        if root in ignore:
            dirs[:] = []
            files[:] = []
        for name in files:
            #print(os.path.join(root, name))
            f = (os.path.join(root, name))
            hashed = hashlib.sha256(f.encode())
            DT = str(datetime.now())
            csvFile.write(f + "," + hashed.hexdigest() + "," + DT + "\n")
        for name in dirs:
            #print(os.path.join(root, name))
            f = (os.path.join(root, name))
            hashed = hashlib.sha256(f.encode())
            DT = str(datetime.now())
            csvFile.write(f + "," + hashed.hexdigest() + "," + DT + "\n")

def compare():
    with open("hashes.csv") as csvFile:
        oldHash = csvFile.readlines()
    changes = []
    csvFile = open("hashes.csv", "w")
    for root, dirs, files in os.walk("/", topdown=True):
        #dirs[:] = [d for d in dirs if d not in ignore]
        if root in ignore:
            dirs[:] = []
            files[:] = []
        for name in files:
            #print(os.path.join(root, name))
            f = (os.path.join(root, name))
            hashed = hashlib.sha256(f.encode())
            DT = str(datetime.now())
            newHash = (f + "," + hashed.hexdigest + "," + DT + "\n")
        for name in dirs:
            #print(os.path.join(root, name))
            f = (os.path.join(root, name))
            hashed = hashlib.sha256(f.encode())
            DT = str(datetime.now())
            hashed = hashed.hexdigest()
            newHash = (f + "," + hashed.hexdigest + "," + DT + "\n")
    print("\n")
    print("The folling changes were found:")
    for i in changes:
        print(i)


def main():
    if os.path.isfile("hashes.csv"):
        print("Comparing files to files to hashes.csv")
        compare()
    else:
        print("Creating the hashes.csv file")
        first_time()


if __name__=="__main__":
    main()
