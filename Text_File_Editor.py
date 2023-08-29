print("\nWelcome to our Text File Editor\n")
a = True

while a:
    print("1. Read Text File\n2. Display Text\n3. Update Text\n4. Clean Text\n5. Save Text\n6. Exit")
    choice = input("\nPlease select an option : ")
    while choice not in ["1", "2", "3", "4", "5", "6"]:
        print("\n1. Read Text File\n2. Display Text\n3. Update Text\n4. Clean Text\n5. Save Text\n6. Exit")
        choice = input("\nPlease select an option : ")
    if choice == "1" : 
        itilizate = input("\nMete on chemen pou fiche w la oubyen non l: ")
        try:
            file = open(f"{itilizate}.txt", "r")
        except FileNotFoundError:
            print("\nDezole nou pa rive jwenn fichye w la : \n")
        else:
            kontni = file.read()
    elif choice == "2" :
        try:
            if kontni is not None:
                print("Kontni fichye a : \n")
                print(kontni)
        except:
            print("\nPa gen fichye ki enpòte deja\n")
    elif choice == "3" :
        try:
            ajoute_tèks = input("\nMete tèks wap ajoute nan fen an : ")
            kontni += "\n" + ajoute_tèks
            print("\nTèks la ajoute nan fichye a avèk siksè")
        except:
            print("\nPa gen fichye ki enpòte deja\n")
    elif choice == "4" :
        try:
            efase = input("\nPeze 1 pou w efase tout espas ki gen nan tèks la epi 2 pou w retire yon karaktè byen espesifik : ")
            while efase not in ['1', '2']:
                print("Sa w antre a pa nan lis la")
                efase = input("\nPeze 1 pou w efase tout espas ki gen devan ak dèyè nan tèks la epi 2 pou w retire yon karaktè byen espesifik : ")
            if efase == "1":
                kontni = kontni.strip()
            elif efase == "2":
                efase = input("Ki karaktè wap retire, lap soti nan tout tèks la nèt : ")
                new = "".join([char for char in kontni if char != efase])
                kontni = new 
            print("Text cleaned successfully.")
        except:
            print("\nPa gen fichye ki enpòte deja")
    elif choice == "5" :
        try:
            save = input("Peze 1 pou w sove on kopi epi 2 si wap modifye orijinal la : ")
            while save not in ['1', '2']:
                print("Sa w antre a pa nan lis la")
                save = input("Peze 1 pou w sove on kopi epi 2 si wap modifye orijinal la : ")
            if save == "1":
                print("Non fichye a")
                new = input("Mete non fichye a :")
                try:
                    newf = open(f"{new}.txt", "w")
                    newf.write(kontni)
                    newf.close()
                    print(f"File {new} saved successfully")
                except:
                    print("Gen yon erè nou anrejistre l pou ou sou non Backup.txt")
                    new_file = open("backup.txt", "w")
                    new_file.write(kontni)
                    print("File 'backup.txt' saved successfully")
            else:
                    menm_file = open(f"{itilizate}.txt", "w")
                    menm_file.write(kontni)
                    menm_file.close()
                    print(f"File {new} saved successfully")
        except:
            print("\nPa gen fichye ki enpòte deja\n")
    elif choice == "6" :
        print("Exiting the Text File Editor. Goodbye!")
        a = False