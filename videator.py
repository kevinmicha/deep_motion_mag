import cv2
import numpy as np
import os

def videator(name, path_original, path_output):
 
    img_array = []

    namelist = sorted(os.listdir(path_original))

    for filename in namelist:
        if filename.endswith(".png"):
            img = cv2.imread(path_original+filename)
            if img is not None:
                height, width, layers = img.shape
                size = (width,height)
                img_array.append(img)
    
    out = cv2.VideoWriter('videos/'+name+'_original.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 40.0, size)
    
    for img in img_array:
        out.write(img)
    out.release()

    img_array = []

    namelist = sorted(os.listdir(path_output))

    for filename in namelist:
        if filename.endswith(".png"):
            img = cv2.imread(path_output+filename)
            if img is not None:
                height, width, layers = img.shape
                size = (width,height)
                img_array.append(img)
    
    out = cv2.VideoWriter('videos/'+name+'_mag.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 40.0, size)
    
    for img in img_array:
        out.write(img)
    out.release()

################# main script
def main():

    video = 'juguete-turbio'
    #video = 'guitar'

    path_original = 'data/vids/'+video+'/'
    path_output = 'data/output/'+video+'/'
    
    videator(video, path_original, path_output)

    path_original = 'data/vids/'+video+'/gs/'
    path_output = 'data/output/'+video+'/gs/'

    videator(video+'_gs', path_original, path_output)

    path_original = 'data/vids/'+video+'/sat/'
    path_output = 'data/output/'+video+'/sat/'
    
    videator(video+'_sat', path_original, path_output)

    path_original = 'data/vids/'+video+'/alpha_50/'
    path_output = 'data/output/'+video+'/alpha_50/'
    
    #videator(video+'_alpha_50', path_original, path_output)

    #path_original = 'data/vids/'+video+'/alpha_75/'
    #path_output = 'data/output/'+video+'/alpha_75/'
    
    videator(video+'_alpha_75', path_original, path_output)

    path_original = 'data/vids/'+video+'/alpha_100/'
    path_output = 'data/output/'+video+'/alpha_100/'
    
    videator(video+'_alpha_100', path_original, path_output)

    path_original = 'data/vids/'+video+'/alpha_400/'
    path_output = 'data/output/'+video+'/alpha_400/'
    
    videator(video+'_alpha_400', path_original, path_output)

if __name__ == "__main__":
    main()
