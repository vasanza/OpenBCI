import cv2 #Show images in windows
from pylsl import StreamInlet, resolve_stream #Lab Streaming Layer for transmition of data
import pandas as pd #Structure data and export it
import random
import time

imCLH=cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images/CLH.jpg')
imCRH=cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images/CRH.jpg')
imDLF=cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images/DLF.jpg')
imPLF=cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images/PLF.jpg')
imDRF=cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images/DRF.jpg')
imPRF=cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images/PRF.jpg')
imBEO=cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images_m2/Baseline.jpg')
imREST=cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images_m2/Rest.jpg')


dataBEO, dataCLH, dataCRH, dataDLF, dataPLF, dataDRF, dataPRF, dataRest = [], [], [], [], [], [], [], [] #Colect data
BEO, CLH, CRH, DLF, PLF, DRF, PRF, REST = "1", "2", "3", "4", "5", "6", "7", "8"  #Code of Type of movement
beo, clh, crh, dlf, plf, drf, prf, rest = 1, 1, 1, 1, 1, 1, 1, 1   #Numbers of repetition
ide = 0 #Identification

timeWindow=3  #seconds

#Cyton Board fs= 250Hz
sampleRate=250

#Cyton + Daisy Board fs= 125Hz
# sampleRate=125

samples=timeWindow*sampleRate

samplesperType=2 #  Number of samples per type of movement


#Functions for data collection and export of generated files


def funCLH(image):
    print("Close Left Hand")

    start_timeCLH = time.time()
    
    #Generate the name of the sample file, with the subject identification number,
    #the number of repetitions, the experiment type and the movement type code.
    name = "S"+subject+"R"+str(run)+typeofExperiment+CLH  
    
    #Open the image file for the window
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", image)
    cv2.waitKey(1)

    #streaming data from OPENBCI
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample() #collected data and timestamp
        dataCLH.append(sample)  #add the samples to the file
        if len(dataCLH) == samples:  #validation that all data from the temporary window is obtained
            #cv2.destroyWindow("Image") 
            cv2.waitKey(1)
            print("---Time CLH Function: %s seconds ---" % (time.time() - start_timeCLH))

            df = pd.DataFrame(dataCLH) #Conversion to dataframe
            df.to_csv("C:/Users/danie/Documents/BCI Data Collection/Datacollected_method_1/" + name + "_" +
                      str(clh) + '.csv') #Save File
            dataCLH.clear()  #Delete saved data
            break


def funCRH(image):
    print("Close Right Hand")

    start_timeCRH = time.time()
    
    name = "S"+subject+"R"+str(run)+typeofExperiment+CRH
    #im = cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images/CRH.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", image)
    cv2.waitKey(1)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        dataCRH.append(sample)
        if len(dataCRH) == samples:
            #cv2.destroyWindow("Image") 
            cv2.waitKey(1)
            print("---Time CRH Function: %s seconds ---" % (time.time() - start_timeCRH))

            df = pd.DataFrame(dataCRH)
            df.to_csv("C:/Users/danie/Documents/BCI Data Collection/Datacollected_method_1/" + name+"_" +
                      str(crh) + '.csv')
            dataCRH.clear()
            break


def funDLF(image):
    print("Dorsiflexion Left Foot")

    start_timeDLF = time.time()
    
    name = "S"+subject+"R"+str(run)+typeofExperiment+DLF
    #im = cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images/DLF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", image)
    cv2.waitKey(1)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        dataDLF.append(sample)
        if len(dataDLF) == samples:
            #cv2.destroyWindow("Image") 
            cv2.waitKey(1)
            print("---Time DLF Function: %s seconds ---" % (time.time() - start_timeDLF))

            df = pd.DataFrame(dataDLF)
            df.to_csv("C:/Users/danie/Documents/BCI Data Collection/Datacollected_method_1/" + name+"_" +
                      str(dlf) + '.csv')
            dataDLF.clear()
            break


def funPLF(image):
    print("Plantarflexion Left Foot")

    start_timePLF = time.time()
   
    name = "S"+subject+"R"+str(run)+typeofExperiment+PLF
    #im = cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images/PLF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", image)
    cv2.waitKey(1)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        dataPLF.append(sample)
        if len(dataPLF) == samples:
            #cv2.destroyWindow("Image") 
            cv2.waitKey(1)
            print("---Time PLF Function: %s seconds ---" % (time.time() - start_timePLF))

            df = pd.DataFrame(dataPLF)
            df.to_csv("C:/Users/danie/Documents/BCI Data Collection/Datacollected_method_1/" + name + "_" +
                      str(plf) + '.csv')
            dataPLF.clear()
            break


def funDRF(image):
    print("Dorsiflexion Right Foot")

    start_timeDRF = time.time()

    name = "S"+subject+"R"+str(run)+typeofExperiment+DRF
    #im = cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images/DRF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", image)
    cv2.waitKey(1)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        dataDRF.append(sample)
        if len(dataDRF) == samples:
            #cv2.destroyWindow("Image") 
            cv2.waitKey(1)
            print("---Time DRF Function: %s seconds ---" % (time.time() - start_timeDRF))

            df = pd.DataFrame(dataDRF)
            df.to_csv("C:/Users/danie/Documents/BCI Data Collection/Datacollected_method_1/" + name + "_" +
                      str(drf) + '.csv')
            dataDRF.clear()
            break


def funPRF(image):
    print("Plantarflexion Right Foot")

    start_timePRF = time.time()

    name = "S"+subject+"R"+str(run)+typeofExperiment+PRF
    #im = cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images/PRF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", image)
    cv2.waitKey(1)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        dataPRF.append(sample)
        if len(dataPRF) == samples:
            #cv2.destroyWindow("Image") 
            cv2.waitKey(1)
            print("---Time PRF Function: %s seconds ---" % (time.time() - start_timePRF))

            df = pd.DataFrame(dataPRF)
            df.to_csv("C:/Users/danie/Documents/BCI Data Collection/Datacollected_method_1/" + name + "_" +
                      str(prf) + '.csv')
            dataPRF.clear()
           
            break


def funBEO(image):
    print("Baseline Eyes Open")

    start_timeBEO = time.time()

    name = "S"+subject+"R"+str(run)+typeofExperiment+BEO
    #im = cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images/Baseline.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", image)
    cv2.waitKey(1)

    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        dataBEO.append(sample)
        if len(dataBEO) == samples:
            #cv2.destroyWindow("Image") 
            cv2.waitKey(1)
            print("---Time BEO Function: %s seconds ---" % (time.time() - start_timeBEO))

            df = pd.DataFrame(dataBEO)
            df.to_csv("C:/Users/danie/Documents/BCI Data Collection/Datacollected_method_1/" + name + "_" +
                      str(beo) + '.csv')
            dataBEO.clear()

            break


def funRest(image):
    print("Rest")

    start_timeREST = time.time()

    name = "S"+subject+"R"+str(run)+typeofExperiment+REST+"_"+ide
    #img = cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images/Rest.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Image', image)
    cv2.waitKey(1)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        dataRest.append(sample)
        if len(dataRest) == samples:
            #cv2.destroyWindow("Image") 
            cv2.waitKey(1)
            print("---Time Rest Function: %s seconds ---" % (time.time() - start_timeREST))

            df = pd.DataFrame(dataRest)
            df.to_csv("C:/Users/danie/Documents/BCI Data Collection/Datacollected_method_1/" + name + "_" +
                      str(rest) + '.csv')
            dataRest.clear()

            break


movement = {'1': funCLH, '2': funCRH, '3': funDLF, '4': funPLF, '5': funDRF, '6': funPRF}

subject = input('ENTER SUBJECT ID: ')

# Type of experiments  M (Motion) / I (Imaginative Motion) / O(Observative)
typeofExperiment = input('Enter the type of experiment to perform(M/I): ')   
run = int(input('Enter the repetition number: '))

print("Looking for an EEG stream")
streams = resolve_stream('type', 'EEG')
# inlet = StreamInlet(streams[0])

totalSamples = 0

while __name__ == '__main__':

    funBEO(imBEO)
    rest = beo
    beo += 1
    ide = BEO
    funRest(imREST)
    
    start_timeSAMPLING = time.time()

    while totalSamples != samplesperType * 6:
        codeMovement = str(random.randint(1, 6)) #Generate a random code number for type of movement
      
         #Validation of code number for type of movement and excess samples
        if codeMovement == '1' and clh != samplesperType+1: 
            movement[codeMovement](imCLH) #Call function to execute
            rest = clh #repetition number after movement
            clh += 1
            ide = CLH
            funRest(imREST) #rest after action

        elif codeMovement == '2' and crh != samplesperType+1:
            movement[codeMovement](imCRH)
            rest = crh
            crh += 1
            ide = CRH
            funRest(imREST)

        elif codeMovement == '3' and dlf != samplesperType+1:
            movement[codeMovement](imDLF)
            rest = dlf
            dlf += 1
            ide = DLF
            funRest(imREST)

        elif codeMovement == '4' and plf != samplesperType+1:
            movement[codeMovement](imPLF)
            rest = plf
            plf += 1
            ide = PLF
            funRest(imREST)

        elif codeMovement == '5' and drf != samplesperType+1:
            movement[codeMovement](imDRF)
            rest = drf
            drf += 1
            ide = DRF
            funRest(imREST)

        elif codeMovement == '6' and prf != samplesperType+1:
            movement[codeMovement](imPRF)
            rest = prf
            prf += 1
            ide = PRF
            funRest(imREST)
        
        totalSamples = clh + crh + dlf + plf + drf + prf - 6
    
    print("---Time Aqc Code: %s seconds ---" % (time.time() - start_timeSAMPLING))
    totalSamples, clh, crh, dlf, plf, drf, prf = 1, 1, 1, 1, 1, 1, 1  #Restart Values
    repeat = input("Do you wish to continue? (Y/N) :")
    if repeat == 'N' or repeat == 'n':
        break
    else:
        run += 1

