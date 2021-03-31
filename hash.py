#Ezrah Itkowsky and Jose Aguirre

import os
import hashlib
from datetime import datetime
import csv

ignore = ["/usr", "/boot", "/bin", "/etc", "/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run"]

BUFF = 65536

def first_time():
    csvFile = open("hashes.csv", "w")
    for root, dirs, files in os.walk("/", topdown=True):
        if root in ignore:
            dirs[:] = []
            files[:] = []
        for name in files:
            filename = (os.path.join(root, name))
            hashed = hashlib.sha256()
            try:
                f = open(filename, "rb")
            except:
                continue
            fb = f.read(BUFF)
            while len(fb) > 0:
                hashed.update(fb)
                fb = f.read(BUFF)
            DT = str(datetime.now())
            csvFile.write(filename + "," + str(hashed.hexdigest()) + "," + DT + "\n")
        for name in dirs:
            filename = (os.path.join(root, name))
            hashed = hashlib.sha256()
            try:
                f = open(filename, "rb")
            except:
                continue
            fb = f.read(BUFF)
            while len(fb) > 0:
                hashed.update(fb)
                fb = f.read(BUFF)
            DT = str(datetime.now())
            csvFile.write(filename + "," + str(hashed.hexdigest()) + "," + DT + "\n")

def compare():
    oldFile =  open("hashes.csv", "rt")
    oldHashes = []
    reader = csv.reader(oldFile, delimiter=",")
    for row in reader:
        for item in row:
            oldHashes.append(item)
    changes = []
    csvFile = open("hashes.csv", "w")
    for root, dirs, files in os.walk("/", topdown=True):    
        if root in ignore:
            dirs[:] = []
            files[:] = []
        for name in files:
            filename = (os.path.join(root, name))
            hashed = hashlib.sha256()
            try:
                f = open(filename, "rb")
            except:
                continue
            fb = f.read(BUFF)
            while len(fb) > 0:
                hashed.update(fb)
                fb = f.read(BUFF)
            DT = str(datetime.now())
            result = False
            if str(hashed.hexdigest()) in oldHashes:
                result = True
            if result == False:
                changes.append(filename + "," + str(hashed.hexdigest()) + "," + DT + "\n")
            csvFile.write(filename + "," + str(hashed.hexdigest()) + "," + DT + "\n")
        for name in dirs:
            filename = (os.path.join(root, name))
            hashed = hashlib.sha256()
            try:
                f = open(filename, "rb")
            except:
                continue
            fb = f.read(BUFF)
            while len(fb) > 0:
                hashed.update(fb)
                fb = f.read(BUFF)
            DT = str(datetime.now())
            result = False
            if str(hashed.hexdigest()) in oldHashes:
                result = True
            if result == False:
                changes.append(filename + "," + str(hashed.hexdigest()) + "," + DT + "\n")
            csvFile.write(filename + "," + str(hashed.hexdigest()) + "," + DT + "\n")
    print("\n")
    print("The folling changes were found:")
    for i in changes:
        print(i)


def main():
    if os.path.isfile("hashes.csv"):
        print("Comparing files to hashes.csv")
        compare()
    else:
        print("Creating the hashes.csv file")
        first_time()


if __name__=="__main__":
    main()
