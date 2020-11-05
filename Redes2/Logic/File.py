import os, sys, time, hashlib
Y = "y/n"
file_list = []
root_dir = "C:/Users/Karol/Desktop/aaa/"
print(" Start Scan....")

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        file_path = subdir + os.sep + file

        if (file_path.endswith(".exe") or file_path.endswith(".dll")):
            file_list.append(file_path)

print(" we found some files could be viruses")
print("start scan files....")


def counts():
    for x in range(5):
        print(x + 1)
        time.sleep(1)





def scan():
    infected_list = []
    for f in file_list:
        virus_def = open("C:/Users/Karol/Desktop/aaa/viruses.txt", "r")
        file_not_read = False
        print("\n scaning... : {}".format(f))
        hasher = hashlib.md5()
        try:
            with open(f, "rb") as file:
                try:
                    print("entro")
                    buf = file.read()
                    file_not_read = True
                    hasher.update(buf)
                    file_hashed = hasher.hexdigest()
                    print("file md5 Done:{}".format(file_hashed))
                    for line in virus_def:
                        if file_hashed == line.strip():
                            print("Malware Detected --> file name: {}".format(f))
                            infected_list.append(f)
                        else:
                            pass
                except Exception as e:
                    print(" could not read the file Error: {}".format(e))
        except:
            pass
    print("Infected files found : {}".format(infected_list))
    deleteOrnot = str(input("would you like to delete the infected files y=yes n=no (y/n)"))
    if deleteOrnot.upper() == Y:
        for infected in infected_list:
            os.remove(infected)
            print("file removed : {}".format(infected))
    else:
        print(" See You ...")
        os.system("PAUSE")


def hash():
    ejemplo_dir = 'C:/Users/Karol/Desktop/aaa/'
    contenido = os.listdir(ejemplo_dir)
    imagenes = []
    for fichero in contenido:
        if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.txt'):
            imagenes.append(fichero)
    print(imagenes)

    md5_hash = hashlib.md5()
    for x in imagenes:
        a_file = open("C:/Users/Karol/Desktop/aaa/"+x, "rb")
        content = a_file.read()
        md5_hash.update(content)
        digest = md5_hash.hexdigest()
        print(digest)

hash()

