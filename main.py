import os
from sys import maxunicode
from typing import Mapping
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


#Takes given text and returns its subsequent audio file
def textToSpeech(text, filename):
    mytext=str(text)
    language="en"
    myobj=gTTS(text=mytext,lang=language,slow=False,)
    myobj.save(filename)



#returns audio objext
def mergeaudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio=AudioSegment.from_mp3('railwaymod.mp3')
    #1 "attention passengers"
    start=0
    finish=2850
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_audio.mp3",format="mp3")
    #2 train_no
    #3 origin_city
    #4 destination_city
    #5 train_name
    #6 "will arrive shortly on"
    start=9000
    audioProcessed=audio[start:]
    audioProcessed.export("6_audio.mp3",format="mp3")
    #7 platform_no



def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    for index,item in df.iterrows():
        #2 train_no
        textToSpeech(item['train_no'],"2_audio.mp3")
        #3 origin_city
        textToSpeech(item['from'],"3_audio.mp3")
        #4 destination_city
        textToSpeech(item['to'],"4_audio.mp3")
        #5 train_name
        textToSpeech(item['train_name'],"5_audio.mp3")
        #7 platform_no
        textToSpeech(item['platform'],"7_audio.mp3")
        
        audios=[f"{i}_audio.mp3" for i in range(1,8)]

        announcement=mergeaudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format="mp3")

if __name__=="__main__":
    print("Generating skeleton...")
    generateSkeleton() 
    print("Now generating announcments...")
    generateAnnouncement("announce.xlsx")



