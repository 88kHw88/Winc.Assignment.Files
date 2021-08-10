__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
from zipfile import ZipFile


#maakt een nieuwe folder 
directory = "cache"
#samenvoegen van current working directory en folder:
path_Cache = os.path.join(os.getcwd(), directory) #(C:\Users\Ka Hou\files\cache)
#lokatie van het zipbestand
zip_Directory = "data.zip"
path_Zip_Directory = os.path.join(os.getcwd(), zip_Directory)

def clean_cache():
    #kijkt of er een map 'cache' op de lokatie staat
    if os.path.isdir(path_Cache):
        for files in os.listdir(path_Cache):
            #verwijdert alle bestanden in de folder
            os.remove(os.path.join(path_Cache,files))
    else:
        #anders een nieuwe map 'cache' maken
        os.mkdir(path_Cache)
            
                                 
def cache_zip(zip_dir_cache, cache_dir_path):
    #leest het zipbestand uit op de gegeven lokatie
    with ZipFile(zip_dir_cache, "r") as zip:
        #pakt zipbestand uit in 'target location'    
        zip.extractall(cache_dir_path)          


def cached_files():
    #lokatie folder 'cache'
    filelist = os.listdir(path_Cache)
    newlist = []
    #alles bestanden in opgegevens lokatie krijgen een absolute path en 
    #worden aan een lijst toegevoegd
    for f in filelist:
        txt_path = os.path.join(path_Cache, f)
        abs_txt_path = os.path.abspath(txt_path)
        newlist.append(abs_txt_path)   
    return newlist


def find_password(input_Cached_Files):
    for name in input_Cached_Files:
        #opent alle files uit de gegeven lokatie                     
        with open(name) as file:       
        #leest de regels van de file en wanneer 'password' wordt gevonden:          
            for line in file:
                if "password" in line:
                    #wordt hieronder de regel waarin 'password' wordt gevonden in een lijst gezet.
                    #de '/n' wordt verwijderd en hou je alleen de 'password' over.
                    lst_String = []
                    lst_String.append(line.strip())
                    for password in lst_String:
                        password_str = password.split(" ")[1]
                        return password_str
            

if __name__ == '__main__':
    clean_cache()
    cache_zip(path_Zip_Directory, path_Cache)
    lst_Files = cached_files()
    print(cached_files())
    print(find_password(lst_Files))