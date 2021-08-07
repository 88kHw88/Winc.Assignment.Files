__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os

#maakt een folder / directory
directory = "cache"
#Parent Directory path / bestandslocatie:
parent_Dir = r"C:\Users\Ka Hou\files"
#samenvoegen van Path / locatie:
path_Cache = os.path.join(parent_Dir, directory)

def clean_cache():
    #kijkt of er een map 'cache' op de lokatie staat
    if os.path.isdir(path_Cache):        
        #maakt een lijst met bestanden uit map 'cache'                          
        filelist = [files for files in os.listdir(path_Cache)]    
        for f in filelist:
            #verwijdert alle bestanden uit map 'cache'  
            os.remove(os.path.join(path_Cache,f))                 
    else:
        #maakt een folder 'cache' in C:\Users\Ka Hou\files
        os.mkdir(path_Cache)                                      
        
clean_cache()


from zipfile import ZipFile
#lokatie van het zipbestand (str)
zip_location = r"C:\Users\Ka Hou\files\data.zip"
def cache_zip(zip_dir_cache, cache_dir_path):
    #leest het zipbestand uit op de gegeven lokatie
    with ZipFile(zip_dir_cache, "r") as zip:
        #pakt zipbestand uit in 'target location'    
        zip.extractall(cache_dir_path)          
        
cache_zip(zip_location, path_Cache)


def cached_files():
    abs_Path = os.path.abspath(r"C:\Users\Ka Hou\files\cache")  
    #maakt een lijst van alle files op de gegeven lokatie     
    filelist = [file for file in os.listdir(abs_Path)]              
    newlist = []
    for f in filelist:
        #alle bestanden worden in een lijst-format gezet in 'abs_path'
        newlist.append(os.path.join(abs_Path, f))                   
    return newlist
        
print(cached_files())


lst_Files = cached_files()
def find_password(input_Cached_Files):
    for name in input_Cached_Files:
        #opent alle files uit de gegevenlokatie                     
        text_File = open(name)        
        #leest de files en wanneer 'password' wordt gevonden:          
        if "password" in text_File.read():      
            target_File = open(name)
            #leest het programma de regels in het bestand uit
            target_Lines = target_File.readlines()
            txt_Lines = []
            for line in target_Lines:
                if "password" in line:
                    #Regel met 'password' wordt toegevoegd aan txt_Lines []. De '/n' wordt eruit gehaald met .strip
                    txt_Lines.append(line.strip())
                    txt_password = txt_Lines
            #omzetten van de regel met het 'password' en maakt er een string van.
            #D.m.v. split wordt de regel op spatie gesplitst en return de 'password'
            for password in txt_password:
                password_str = (str(password))
                password_str = password_str.split(" ")[1]
            return password_str                
        
        text_File.close()

print(find_password(lst_Files))
