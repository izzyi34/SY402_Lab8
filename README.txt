The data is store in the hash data file as "File path/name" , "Hash of the file" , "The date and time the file was obsereved"
An example is: /home/itkowsky/.mozilla/firefox/jmktb20t.default-release/AlternateServices.txt,e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855,2021-03-30 18:17:07.709978

The files and their paths are collected using os.walk. They are then hashed using sha256 and stored to hashes.csv. The first time hash.py is run it creates the csv file. Any time it is run after this it will check the new hashes against the old hashes and inform the user if any changes have been made.
