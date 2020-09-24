import find_func_in_a_file
import os
project = os.walk(input("enter dir"))
file_names = []
for dirpath,dirname,files in project:
    if len(files)!=0:
        for file_name in files:
                if file_name.endswith(".c") or file_name.endswith(".h"):
                    full_pth = dirpath + r"/" + file_name
                    file_names.append(full_pth)
functions_file = input("enter the file that contains functions seperated by lines: ")
function_list = list() #a list that contains all the functions
with open(functions_file) as functionFile:
    functions_collection = functionFile.readlines()
    for function in functions_collection:
        function_list.append(function.rstrip())
    print(*function_list)
answer_file =input("enter answer file name") 
answer_File = open(answer_file,"a")


#to find in each file
with open(answer_file,"a") as answer_File:
    for file_to_search in file_names:
        find_func_in_a_file.find_function(file_to_search,function_list,answer_File)
###script by ganesh prasad r

