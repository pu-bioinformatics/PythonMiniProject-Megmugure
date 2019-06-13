def menu(file):
    """
    This function prints out the display menu.
    It takes file as an argument.
    The display menu contains all the options the user may input.
    """
    print("********************************************************************************")
    print("* PDB FILE ANALYZER                                                            *")
    print("********************************************************************************")
    print("* Select an option from below:                                                 *")
    print("*                                                                              *")
    print("*      1)Open a PDB file                        (O)                            *")
    print("*      2)Information                            (I)                            *")
    print("*      3)Show histogram of amino acids          (H)                            *")
    print("*      4)Display secondary structures           (S)                            *")          
    print("*      5)Export PDB File                        (X)                            *")
    print("*      6)Exit                                   (Q)                            *")
    print("*                                                                              *")
    print("*                                                   Current PDB: %s      *" % file)
    print("********************************************************************************")
    
    global option
    option = input(":")
    choice(option)     #the function choice is called inside this function after the menu has been printed. The user can then input the options on the menu.
    
    
    
def open_file(file):
    """
    This function prompts the user to input a valid path where the pdb file they wish
    to read is located.
    It takes file as an argument.
    It uses the module "os" to verify if the path specified is indeed a valid one.
    If it evaluates to true, it splits the path name and extracts the file name and then
    prints that the file has been loaded successfully.
    """
    import os
    filepath = input("Enter a Valid PATH for a PDB file: ")
    
    if os.path.isfile(filepath):
        split_filepath = filepath.split("/")
        file = split_filepath[-1]
        print("The File " + file + " has been successfully loaded")
        return file, filepath
    else:
        print("No such path existing")
        open_file(file)
        
        

def information(filepath):
    """
    This function opens the pdb file loaded.
    It takes the filepath as an argument.
    It then displays the title of the pdb file, the name of
    the file as well as a summary of the primary structure of the file.
    It displays the amino acids as they appear in all the different chains respectively.
    """
    with open(filepath, 'r') as my_file:   #opens the file
        lines = my_file.readlines()
        
        dict4 = {'CYS': 'C','ASP': 'D','SER': 'S','GLN': 'Q','LYS': 'K','ILE': 'I','PRO': 'P','THR': \
                 'T','PHE': 'F','ASN': 'N','GLY': 'G','HIS': 'H','LEU': 'L','ARG': 'R','TRP': 'W','ALA': 'A','VAL': 'V','GLU': 'E','TYR': 'Y','MET': 'M'}         #the dictionary used to convert the amino acids from 3 letter codes to one letter codes.
        title_lst = []  #an empty list where the title will be appended to
        chains = []     #an empty list where all the chains in the file will be appended to
        for line in lines:
            split_lines = line.split()   #splits the lines in the file
            if line.startswith("TITLE"):
                split_lines = split_lines[1:]
                for words in split_lines:
                    title_lst.append(words)
                    title = " ".join(title_lst)
                    title_max_80_characters = "Title: " + title

            if line.startswith("SEQRES"):
                if split_lines[2] not in chains:
                    chains.append(split_lines[2])
                    extracted_chains = " and ".join(chains)
                    extracted_chains = "CHAINS: " + extracted_chains

        for i in range(0, len(title_max_80_characters), 80):
            print(title_max_80_characters[i:i+80])            #prints the title having a maximum of 80 characters per line
                
        
        print(extracted_chains)

        for chain in chains:
            print("-Chain " + chain)

            amino_list = []
            num_string = ""
            helix = 0
            sheet = 0
            for line in lines:
                split_lines = line.split()

                if line.startswith("SEQRES"):
                    if chain == split_lines[2]:

                        num_string = "  Number of amino acids:   " + str(split_lines[3])
                        for amino in split_lines[4:]:
                            amino_list.append(dict4[amino])
                    

                if line.startswith("HELIX"):
                    if chain == split_lines[4]:
                        helix = helix + 1

                if line.startswith("SHEET"):
                    if chain == split_lines[5]:
                        sheet = sheet + 1

            print(num_string)
            print("  Number of helix:          " + str(helix))
            print("  Number of sheet:          " + str(sheet))
            

            amino_list = "".join(amino_list)
            sequence_lst = []
            for i in range(0, len(amino_list), 50):
                seq_string = "            "+amino_list[i:i+50]
                sequence_lst.append(seq_string)
            line1 = list(sequence_lst[0])
            line1[2:12] = "Sequence: "
            line1 = "".join(line1)
            sequence_lst[0] = line1
            for line in sequence_lst:
                print(line)
                

                
dict1 = {'ASP': 'D','SER': 'S','GLN': 'Q','LYS': 'K','ILE': 'I','PRO': 'P','THR': 'T','PHE': 'F','ASN': 'N','GLY': 'G','HIS': 'H','LEU':\
         'L','ARG': 'R','TRP': 'W','ALA': 'A','VAL': 'V','GLU': 'E','TYR': 'Y','MET': 'M'}                  #the dictionary used to convert the amino acids from 3 letter codes to one letter codes.

def ascend_alphabetic(filepath):
    """
    This function opens the pdb file and orders the amino acids in an alphabetic order,
    in the ascending order, from a to z.
    It takes the filepath as an argument.
    It prints the output to the console.
    """
    with open (filepath, "r") as file:
        lines = file.readlines()
        amino_acids = []
        
        for line in lines:
            split_lines = line.split()
            
            if line.startswith("SEQRES"):
                for amino in split_lines[4:]:
                    amino_acids.append(amino)
                    
                    dict2 = dict((i, 0) for i in dict1.keys())
                    for amino in amino_acids:
                        dict2[amino] = dict2[amino] + 1
                        sorted_amino = sorted(dict2)
                        
        for i in sorted_amino:
            print("%s (%3d): %s" %(i, dict2[i], '*'*dict2[i])) 
            


def descend_alphabetic(filepath):
    """
    This function opens the pdb file and orders the amino acids in an alphabetic order,
    in the descending order, from z to a.
    It takes the filepath as an argument.
    It prints the output to the console.
    """
    with open (filepath, "r") as file:
        lines = file.readlines()
        amino_acids = []
        
        for line in lines:
            split_lines = line.split()
            
            if line.startswith("SEQRES"):
                for amino in split_lines[4:]:
                    amino_acids.append(amino)
                    
                    dict2 = dict((i, 0) for i in dict1.keys())
                    for amino in amino_acids:
                        dict2[amino] = dict2[amino] + 1
                        sorted_amino = sorted(dict2, reverse = True)
                        

        
        for i in sorted_amino:
            print("%s (%3d): %s" %(i, dict2[i], '*'*dict2[i]))
            
            
def ascend_nums(filepath):
    """
    This function opens the pdb file and orders the amino acids according to their 
    numbers in the file, in an ascending order, from the lowest to the highest number.
    It takes the filepath as an argument.
    It prints the output to the console.
    """
    with open (filepath, "r") as file:
        lines = file.readlines()
        amino_acids = []
        
        for line in lines:
            split_lines = line.split()
            
            if line.startswith("SEQRES"):
                for amino in split_lines[4:]:
                    amino_acids.append(amino)
                    
                    dict2 = dict((i, 0) for i in dict1.keys())
                    for amino in amino_acids:
                        dict2[amino] = dict2[amino] + 1
                        sorted_amino = dict(sorted(dict2.items(), key = lambda t: t[1]))
                        
        for i in sorted_amino:
            print("%s (%3d): %s" %(i, dict2[i], '*'*dict2[i]))
            
                

def descend_nums(filepath):
    """
    This function opens the pdb file and orders the amino acids according to their 
    numbers in the file, in a descending order, from the highest to the lowest number.
    It takes the filepath as an argument.
    It prints the output to the console.
    """
    with open (filepath, "r") as file:
        lines = file.readlines()
        amino_acids = []
        
        for line in lines:
            split_lines = line.split()
            
            if line.startswith("SEQRES"):
                for amino in split_lines[4:]:
                    amino_acids.append(amino)
                    
                    dict2 = dict((i, 0) for i in dict1.keys())
                    for amino in amino_acids:
                        dict2[amino] = dict2[amino] + 1
                        sorted_amino = dict(sorted(dict2.items(), key = lambda t: t[1], reverse = True))
                       
        for i in sorted_amino:
            print("%s (%3d): %s" %(i, dict2[i], '*'*dict2[i]))
            
            
def hist():
    """
    This function prints the menu containing the options the user has for ordering the
    amino acids in the file.
    """
    
    print("Choose an option to order by: ")
    print("   number of amino acids - ascending   (an)")
    print("   number of amino acids - descending  (dn)")
    print("   alphabetically - ascending          (aa)")
    print("   alphabetically - descending         (da)")
    
    global selection
    selection = input(":")
    

        
def hist_option(filepath):
    """
    This function contains all the options the user can make for oredering the amino acids.
    It takes the filepath as an argument.
    It calls the function that displays the menu first.
    The functions defined individually, for ordering, are called within this function. This depends on the option entered by the user.
    """
    hist()
    if selection.lower() not in ("an", "dn", "aa", "da"):
        print("Invalid option")
        hist_option(filepath)
        
    else:
        if selection == "an":
            ascend_nums(filepath)
        if selection == "dn":
            descend_nums(filepath)
        if selection == "da":
            descend_alphabetic(filepath)
        if selection == "aa":
            ascend_alphabetic(filepath)                    
                                       
            
            
def secondary(filepath,file):
    """
    This function opens the pdb file and then displays it's secondary structure.
    It has specific symbols for 3 criteria of structures namely; helix, sheet and
    the rest of the amino acids that are not part of the 2 structures.
    It also enables the location of each structure to be identified and printed
    at the location where it starts.
    """
    split_file = file.split(".")
    file_id = split_file[0]
    print("Secondary Structure of the PDB id %s:" %file_id)
    with open(filepath, 'r') as file:  
        lines = file.readlines()
        
        dict4 = {'CYS': 'C','ASP': 'D','SER': 'S','GLN': 'Q','LYS': 'K','ILE': 'I','PRO': 'P','THR': 'T','PHE': 'F','ASN': 'N','GLY': 'G',\
                 'HIS': 'H','LEU': 'L','ARG': 'R','TRP': 'W','ALA': 'A','VAL': 'V','GLU': 'E','TYR': 'Y','MET': 'M'}

        chains = []
        for line in lines:
            split_lines = line.split()
            if line.startswith("SEQRES"):
                if split_lines[2] not in chains:
                    chains.append(split_lines[2])

        for chain in chains:      #this iterates over all the chains found in the pdb file opened. Subsequently, it does the following to all the chains available.
            print("Chain " + chain + ":" + "\n" + "(1)")

            amino_lst = []
            empty_amino_lst = []
            empty_dashes_lst = []   
            for line in lines:
                split_lines = line.split()

                if line.startswith("SEQRES"):
                    if chain == split_lines[2]:
                        for amino in split_lines[4:]:
                            amino_lst.append(dict4[amino]) #appends the 1 letter codes of all the amino acids in the amino_lst
                            empty_amino_lst.append(" ")    #appends empty spaces to the empty list
                            empty_dashes_lst.append("-")   #appends dashes to the empty list
                            
                            
                            

                if line.startswith("HELIX"):
                    if chain == split_lines[4]:
                        
                        helix_name = split_lines[2]
                        empty_amino_lst[int(split_lines[5]) - 1 : int(split_lines[5]) - 1 + len(helix_name)] = helix_name  #sets the labels for each helix
                        
                        x = int(split_lines[8]) - int(split_lines[5]) + 1
                        y = x * "/"    #multiplies each helix symbol "/" by the number of times it appears
                        empty_dashes_lst[int(split_lines[5]) - 1 : int(split_lines[8])] = y
                        
                        
                        
                                 
                        
                if line.startswith("SHEET"):
                    if chain == split_lines[5]:
                        
                        sheet_name = split_lines[1] + split_lines[2]
                        empty_amino_lst[int(split_lines[6]) - 1 : int(split_lines[6]) - 1 + len(sheet_name)] = sheet_name  #sets the labels for each sheet
                        
                        x = int(split_lines[9]) - int(split_lines[6]) + 1
                        n = x * "|"   #multiplies each sheet symbol "|" by the number of times it appears
                        empty_dashes_lst[int(split_lines[6]) - 1 : int(split_lines[9])] = n
                        

            amino_lst = "".join(amino_lst)
            
            empty_dashes_lst = "".join(empty_dashes_lst)
            
            empty_amino_lst = "".join(empty_amino_lst)

            for i in range(0, len(amino_lst), 80):                          #enables the contents of all the lists to be printed 80 lines max, one list after another and followed by a new line character.
                print(amino_lst[i:i+80], "\n" + empty_dashes_lst[i:i+80] + "\n" + empty_amino_lst[i:i+80])
                
                
                
def export(filepath):
    """
    This function writes all the contents of the loaded file to the file in the path specified by the user.
    It takes the filepath as an argument.
    """
    export_path = input("Enter path for export and new file name: ")
    import os
    export_dir = export_path.split("/")    #splitting the path to get the directory name
    export_dir = "/".join(export_dir[:-1])

    if os.path.isdir(export_dir):         #checks that the export directory is an actual directory and if it evaluates to true, it goes ahead to write to the new file specified by the user.
        with open(export_path, "w") as my_exp_file:
            myfile = open(filepath, "r")
            for line in myfile:
                my_exp_file.write(line)
            myfile.close()
        print("Export Successful")    #informs the user that the export was successful.
    else:
        print("Path doesn't exist")
        export(filepath)      #recursively calls itself if the path specified by the user does not exist.
        
        
def exit():
    """
    This function enables the user to exit the program.
    The user has 2 options, to confirm exit or to go back to the main menu.
    """
    option = input("Do you want to exit (E) or do you want to go back to the main menu (M): ")
    if option.upper() == "M": 
        menu(file)
    elif option.upper() == "E":
        print("Exiting Program")   #prints "Exiting Program" and quits the program all together.
    else:
        exit()
        
        
        

def choice(option):
    """
    This function outlines all the options the user has.
    Under it are lso the appropriate function call followed by a call to the menu function.
    """

    global file, filepath
    import os
    option = option.upper()
    
    
    if option in ("O", "I", "H", "S", "X", "Q"):
        
        if file == "  None  " and option in ["O", "Q"]:
            if option == 'O':
                file , filepath = open_file(file)
                menu(file)
            if option == "Q":
                exit()
                
        else:
            if file == "  None  ":
                print("No file loaded")
                menu(file)
            
            else:
                if option == "O":
                    change = input("Do you want to replace the loaded file Y/N: ")
                    change = change.upper()
                    if change == "Y":
                        file , filepath = open_file(file)
                        menu(file)
                    elif change == "N":
                        menu(file)
                if option == "I":
                    print("PDB File: " + file)
                    information(filepath)
                    menu(file)
                if option == "H":
                    hist_option(filepath)
                    menu(file)
                if option == "S":

                    secondary(filepath,file)
                    menu(file)
                if option == "X":
                    export(filepath)
                    menu(file)
                if option == "Q":
                    exit()

    else:
        print("Invalid option")
        menu(file)
            
file = "  None  "
menu(file)
        

                 
    
            
            
