'''
Created on 
    March 26, 2021

Course work: 
    Python Snippet Collection

@author: Elakia,Sivaraam

Source:
    
'''
# sudo apt-get install ffmpeg
# sudo apt-get install -y python-pydub

# Import necessary modules
from os import path
from pydub import AudioSegment
  
# assign files
input_file = "talk_with_alistair_dist_process_logs.mp3"
output_file = "result.wav"
  
# convert mp3 file to wav file
sound = AudioSegment.from_mp3(input_file)
sound.export(output_file, format="wav")

def startpy():

    return 


if __name__ == '__main__':
    startpy()