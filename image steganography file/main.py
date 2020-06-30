from PIL import Image  # import image class from Pillow lib








def main():
    modes = int(input("""  
    image steganography python pillow
    *******************************************************************************************************
    enter 1 )for encoding 8bit rgb png image with extension ("saved.png" is provided else put an image in the folder)
    enter 2 )for decoding encoded image (usually encoded.png but if you have renamed use that name")
    enter 3 )to exit
    enter anything else to get back to this menu
    *******************************************************************************************************
     """))
    if (modes == 1):  # enter encoding function
        data = input("""
        *******************************************************************
        Enter the secret message
        ******************************************************************
        """)
        imagelocation = input("""
        ******************************************************************
        enter full location of image or just saved.png to use default image
        *******************************************************************
        
        
        
        """)
        encode(imagelocation,data)
    if(modes == 2):  # enter decoding function
            imagelocation = input("enter location")
            decoding(imagelocation)
    if(modes == 3):
            return;
    else:
            print("""
            
            ****************************************************************************************
            *****************************************************************************************
            ************************************************************************* choose again
            """)
            main()










def encode(imagelocation,data):
    count = 0 #for setting reqired number of bits as oeven so that if we write we can decode
    countascii = 0 #for encodding
    image = Image.open(imagelocation) #open image specified by image location
    copy_image = image.copy() # copying image obj to another image object so that the new image contain same info
    copy_image_loaded = copy_image.load() #converting image object to pixelaccess object to change pixel values
    (columns, rows) = image.size  # image size attribute gives out the size
    listofascii = datamodifier(data) # call data modifier function and get list of bits as answer
    for row in range(rows):
        for column in range(columns):
            if(count<=len(listofascii)):#makes sure only bits before length of message is turned even so that decoding gets faster
                if(copy_image_loaded[(column, row)][0] % 2 is 1): #values only required is made even
                    copy_image_loaded[(column, row)]=tuple([sum(x) for x in zip((-1,0,0),copy_image_loaded[(column,row)])]) #make [0] component even if its %2 val is 1 zip zips 1 list val into tople sum sums it up
                if (copy_image_loaded[(column, row)][1] % 2 is 1):
                    copy_image_loaded[(column, row)] = tuple([sum(x) for x in zip((0, -1, 0), copy_image_loaded[(column, row)])])
                if (copy_image_loaded[(column, row)][2] % 2 is 1):
                    copy_image_loaded[(column, row)] = tuple([sum(x) for x in zip((0, 0, -1), copy_image_loaded[(column, row)])])
                count = count+3


    for row in range(rows):
        for column in range(columns):
            if countascii < len(listofascii):
                copy_image_loaded[(column,row)] = tuple([sum(x) for x in zip(listofascii[(countascii+0):(countascii+3)],copy_image_loaded[(column,row)])]) #encoding
                countascii = countascii + 3
            else:
                break
    copy_image.save("encoded.png")
    print("""********************************************encoding done with accuracy*********************************************""")
    main()








def decoding(imagelocation="encoded.png"):
    answer = [] #list of all binary values till odd mod 9 bit
    decodingim = Image.open(imagelocation)
    decodingimdata = decodingim.getdata()
    decodingimiter = iter(decodingimdata) #making getdata obj an iterable so that next works
    answer = answer + [x for x in next(decodingimiter)] #answer list is filled with 3 bits per step
    answer = answer + [x for x in next(decodingimiter)]
    answer = answer + [x for x in next(decodingimiter)] #till 9 bits till here
    while (answer[-1] % 2 is 0): #if no odd is got keep on adding 9 bits
        answer = answer + [x for x in next(decodingimiter)]
        answer = answer + [x for x in next(decodingimiter)]
        answer = answer + [x for x in next(decodingimiter)]
    answer = [x%2 for x in answer[:-9]] #take out extraq bits and create a list
    answers = list(map ( str , answer))
    answertoret = "" #final answer to ret
    countval = len(answer)//9 #number of loops to convert
    count = 0
    for i in range(countval):
        answerstrin = "".join((answers[count:count+9][:-1]))
        count = count + 9
        answertoret = answertoret + chr(int(answerstrin,2)) # int in base2 to char

    with open("secretmessage.txt",'w') as filehandle:
        filehandle.write(answertoret)
    print("*****************************get message in secretmessage.txt in the folder where this program is**********")



    print(answertoret)
    print("*********************************************** decoding successful******")
    main()















def datamodifier(data):
    answer = ""
    answerfinal = ""
    for i in range(len(data)):
        binary = format(ord(data[i]),'08b') #give eout ascii values
        answer = answer + binary + '0' #8 bit ascii plus a 0 to make 3(rgb,rgb,rg'b') pixel complete and 9th bit even
    answer.rstrip()
    for i in range(len(answer)):
        answerfinal = answerfinal + answer[i] + "," #adding commas so that seperation becomes easier

    answerfinal = answerfinal + "1,1,1,1,1,1,1,1,1" # mod 9 bit being odd indicates the array is complete (((for decoding only 9th bit is used to indicate mark to consider to decode till previous triplet)
    return (tuple(map(int,answerfinal.split(",")))) #list of bits plus 111111111 is returned as list [1,1,0....1,1,1,1,1,1]




if __name__ == '__main__':
    main()
