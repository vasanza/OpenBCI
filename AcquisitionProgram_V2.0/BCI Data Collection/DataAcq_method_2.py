import cv2
import pandas as pd
import random
import time
import argparse
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds

###############################################################
###                        To execute in CMD                ###  
###     Linux --board-id 0 --serial-port /dev/ttyUSB#       ###
###     Windows --board-id 0 --serial-port COM#             ###
###############################################################
#cyton id 0
#cyton+daisy id 2


imCLH=cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images_m2/Left.jpg')
imCRH=cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images_m2/Right.jpg')
imBEO=cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images_m2/Baseline.jpg')
imREST=cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images_m2/Rest.jpg')
imBACKGROUND=cv2.imread('C:/Users/danie/Documents/BCI Data Collection/images_m2/Background.jpg')



dataBEO, dataCLH, dataCRH, dataRest = [], [], [], [] #Colect data
BEO, CLH, CRH, REST = "1", "2", "3", "4"  #Code of Type of movement
beo, clh, crh, rest = 0, 0, 0, 0   #Numbers of repetition
ide = 0 #Identification


timeWindow=3  #seconds

#Cyton + Daisy Board fs= 250Hz
sampleRate=250

#Cyton + Daisy Board fs= 125Hz
# sampleRate=125

samples=timeWindow*sampleRate

samplesperType=2 #  Number of samples per type of movement




def loadParam():
    BoardShim.enable_dev_board_logger()
    parser = argparse.ArgumentParser()
    parser.add_argument('--serial-port', type=str,  required=False, default='')
    parser.add_argument('--board-id', type=int, required=True)
    args = parser.parse_args()
    params = BrainFlowInputParams()
    params.serial_port = args.serial_port
    board = BoardShim(args.board_id, params)
    return board


def funCLH(boardInfo,image):
    print("Close Left Hand")

    start_timeCLH = time.time()

    name = "S"+subject+"R"+str(run)+typeofExperiment+CLH
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", image)
  
    cv2.waitKey(3000)
   
    data_clh = boardInfo.get_current_board_data(samples)
    print("---Time CLH Function: %s seconds ---" % (time.time() - start_timeCLH))
   
    df = pd.DataFrame(np.transpose(data_clh))

    df.to_csv("C:/Users/danie/Documents/BCI Data Collection/Datacollected_method_2/" + name + "_" +
              str(clh) + '.csv')


def funCRH(boardInfo,image):
    print("Close Right Hand")
    start_timeCRH = time.time()

    name = "S" + subject + "R" + str(run) + typeofExperiment + CRH
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", image)

    cv2.waitKey(3000)
   
    data_crh = boardInfo.get_current_board_data(samples)
    print("---Time CRH Function: %s seconds ---" % (time.time() - start_timeCRH))

    df = pd.DataFrame(np.transpose(data_crh))

    df.to_csv("C:/Users/danie/Documents/BCI Data Collection/Datacollected_method_2/" + name + "_" +
              str(crh) + '.csv')


def funBEO(boardInfo,image):
    print("Baseline Eyes Open")

    start_timeBEO = time.time()
    name = "S" + subject + "R" + str(run) + typeofExperiment + BEO
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", image)

    cv2.waitKey(3000)

    data_beo = boardInfo.get_current_board_data(samples)
    print("---Time BEO Function: %s seconds ---" % (time.time() - start_timeBEO))

    df = pd.DataFrame(np.transpose(data_beo))

    df.to_csv("C:/Users/danie/Documents/BCI Data Collection/Datacollected_method_2/" + name + "_" +
              str(beo) + '.csv')


def funRest(boardInfo,image):
    print("Rest")

    start_timeREST = time.time()

    name = "S"+subject+"R"+str(run)+typeofExperiment+REST+"_"+ide
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", image)

    cv2.waitKey(3000)

    data_rest = boardInfo.get_current_board_data(samples)
    print("---Time Rest Function: %s seconds ---" % (time.time() - start_timeREST))
    
    df = pd.DataFrame(np.transpose(data_rest))

    df.to_csv("C:/Users/danie/Documents/BCI Data Collection/Datacollected_method_2/" + name + "_" +
              str(des) + '.csv')


movement = {'1': funCLH, '2': funCRH}


subject =  input('ENTER SUBJECT ID: ')

# Type of experiments   M (Motion) / I (Imaginative Motion) / O(Observative)
typeofExperiment = input('Enter the type of experiment to perform(M/I): ')   
run = int(input('Enter the repetition number: '))

time.sleep(20)

board_info = loadParam()
board_info.prepare_session()
print(board_info.get_sampling_rate(0))
board_info.start_stream()

totalSamples = 0

while __name__ == '__main__':
   
    funBEO(board_info,imBEO)
    beo += 1
    des = 1
    ide = BEO
    funRest(board_info,imREST)

    start_timeSAMPLING = time.time()

    while totalSamples != samplesperType * 2:
       
        codeMovement = str(random.randint(1, 2))

        if codeMovement == '1' and clh != samplesperType:
            clh += 1
            movement[codeMovement](board_info,imCLH)
            des = clh
            ide = CLH
            funRest(board_info,imREST)

        elif codeMovement == '2' and crh != samplesperType:
            crh += 1
            movement[codeMovement](board_info,imCRH)
            des = crh
            ide = CRH
            funRest(board_info,imREST)

        totalSamples = clh + crh

    print("---Time Aqc Code: %s seconds ---" % (time.time() - start_timeSAMPLING))

    totalSamples, clh, crh = 0, 0, 0

    repeat = input("Do you wish to continue? (Y/N) :")

    if repeat == 'N' or repeat == 'n':
        board_info.stop_stream()

        break
    else:
        run += 1
