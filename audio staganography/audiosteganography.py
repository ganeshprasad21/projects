# this project assumes you feed it the audio file with name sample.wav 16 bit pcm audio ... for best possible results
# packages
# numpy for better datastructures wave for wav processing and wavf for writing wave file
import wave
import numpy as np
import scipy.io.wavfile as wavf



def encode(messageinascii,lengthofmessage):
    nameoffile = input("""enter the name of wav audiofile
    *****************************************************
    with extension
    **********************************************************
    make sure its 
    >mono channel file (stereo channel audios in future build)
    ->16 bit depth 
     -->pcm coded
	--->wav file

    for better results(sample.wav is provided)
    """)
    #open wav file as wav_object
    file = wave.open(nameoffile) #wave_file obj is created
    # data header is 44 byte but this takes data directly so we read all data by giving that index
    data = file.readframes(-1)
    #data in numpy array int16 format
    data_in_int = list(np.frombuffer(data,np.int16)) #it will be in binary string format like b'\xfc\xff\x04\x00\xff\xff\x03\x00\xfc\xff\x04\x00\xff\xff\xff\xff\x04\x00\x04\x00\x04\x00\xf4\xff\xc3\xff\xc7\xff\xd0\xff\xd0\xff\xca\xff\xeb\xff\xa3\xff\xff\xfeM\xfe\xd4\xfd^\xfd\xf4\xfc\xba\xfc\xa3\xfc\xbc\xfc\xcb\xfc\x11\xfdi\xfd'so we convert it to int16 np array and store
    for i in range(1,lengthofmessage+1): #1st bit is reserved for length of message
        if data_in_int[i] %2 != 0:
            data_in_int[i] = data_in_int[i] - 1 #make all values from index 1 even so that the encoding can be done
    data_in_int[0] = lengthofmessage#we have to now adde the size in first sample that is to be encode now we set the zero index to desired number that is how many more iterations to decode or how many bits are encoded
    #encoding process
    for i in range(1,lengthofmessage+1):
        if messageinascii[i-1] % 2 != 0:
            data_in_int[i] = data_in_int[i]+1 #data_in_in is unaltered but contains data in requuired format

#[0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1]
#data <1 or any that dosent matter it shows length>,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,123123
#[16, 0, 2, 2, 4, 4, 6, 6, 8, 0, 2, 2, 4, 4, 6, 6, 8, 123123] data_in int
#[16, 0, 3, 3, 5, 5, 6, 6, 8, 0, 3, 3, 5, 5, 6, 6, 9, 123123] data in int after enc

    # saving encoded file
    # total frames
    number_of_frames = file.getnframes()
    # frames per sec
    samples_per_second = file.getframerate()
    #generate encoded aud
    samples = np.array(data_in_int,np.int16) #make it 16 bit encoded music with this step
    fs = samples_per_second #44.1kh
    out_f = 'out1.wav' #name that is chosen as convention

    wavf.write(out_f, fs, samples) #file
    print("""
    
    
    
    
    encoded ****************************************************
    
    
    
    
    
    """)
    starter()











def datamodifier(message):
    answer = ""
    answerfinal = ""
    for i in range(len(message)):
        binary = format(ord(message[i]),'08b') #give eout ascii values
        answer = answer + binary #8 bit ascii
    answer.rstrip()
    for i in range(len(answer)):
        answerfinal = answerfinal + answer[i] + "," #adding commas so that seperation becomes easier
    answerfinal = answerfinal[:-1] #comma is there so we take till the value
     # mod 9 bit being odd indicates the array is complete (((for decoding only 9th bit is used to indicate mark to consider to decode till previous triplet)
    returnvalue =  (list(map(int,answerfinal.split(","))))
    length = len(returnvalue)
    return(returnvalue,length)









def decode(inputtedfilenamehere):
    file = wave.open(inputtedfilenamehere)     #wave object called file
    decoding_data = file.readframes(1)              #reading 1st frame which contain data
    totalnumberofbits = list(np.frombuffer(decoding_data, np.int16))[0]     #taling the value out from list containing only that
    asciidata = file.readframes(totalnumberofbits)#read the encoded message
    asciidatainint = list(np.frombuffer(asciidata, np.int16)); #make it a list
    decodedmessageinbinary = ""#message that is to be decoded in ones and zero
    for i in asciidatainint:
        if i % 2 == 1:
            decodedmessageinbinary = decodedmessageinbinary + "1"
        else:
            decodedmessageinbinary = decodedmessageinbinary + "0"#o for even 1 for odd
    ldecodedmessageinbinary = len(decodedmessageinbinary.rstrip()) // 8 #length to find nor of loops to decode
    answertoret = ""#final
    counter = 0
    for i in range(ldecodedmessageinbinary):
        answertoret = answertoret + chr(int(decodedmessageinbinary[counter:counter + 8], 2))#conversion
        counter = counter + 8
    filetowrite = open("secretmessagefromaud.txt", 'w')#write to a file
    filetowrite.write((answertoret))#print
    print("""






***********************decoding success







""")
    print("""
    
    
    """+
          answertoret+"""
          
          
    """)
    starter()


def starter():
    selector = input(""" 
    ****************************
    1 to encode
    2 to decode
     ***************************
	""")
    if int(selector) == 1:
        message = input("""
        ***********************************************
        enter message
        ************************************************
        """)
        message = message.rstrip()
        (messageinascii, lengthofmessage) = datamodifier(message)
        encode(messageinascii,lengthofmessage)
    elif int(selector) == 2:
        inputtedfilenamehere = input("""
        ********************************
	enter filename usually out1.wav
	*****************************

        """)
        decode(inputtedfilenamehere)
    else:
        starter()



if __name__ == '__main__':
    starter()
