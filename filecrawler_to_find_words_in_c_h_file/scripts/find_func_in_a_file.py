def find_function(file_to_search,function_list,answerFile):
	for function in function_list:
		line_num = 1
		with open(file_to_search) as fileToSearch:
			for line in fileToSearch:
				if function in line.rstrip(): #read line by line
					answerFile.write("\n"+"in the file :::  "+ "\n" +file_to_search +"<<<>>>"+"\n\n"+"    found function-name :::      "+function+"   ::: at    line ::: "+ str(line_num)+ "\n")
				line_num += 1
