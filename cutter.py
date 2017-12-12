import os
import subprocess

# specify path to folder with videos
folder = '/home/sk/Videos/'

# specify path to folder with output images
label_folder = '/home/sk/Videos/lab1/'

for files in os.listdir(folder):
    if files.endswith('.MOV'):
        command = 'ffmpeg -i %s %s' %(folder + files, label_folder + files) + '-%05d.jpg'
        subprocess.call(command, shell=True)

