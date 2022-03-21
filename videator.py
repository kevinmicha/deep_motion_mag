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
    
    out = cv2.VideoWriter('videos/'+name+'_original.avi',cv2.VideoWriter_fourcc(*'DIVX'), 40.0, size)
    
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
    
    out = cv2.VideoWriter('videos/'+name+'_mag.avi', cv2.VideoWriter_fourcc(*'DIVX'), 40.0, size)
    
    for img in img_array:
        out.write(img)
    out.release()

################# main script
def main():

    path_original = 'data/vids/juguete-turbio/'
    path_output = 'data/output/juguete-turbio/'
    
    videator('juguete-turbio', path_original, path_output)

    path_original = 'data/vids/juguete-turbio/gs/'
    path_output = 'data/output/juguete-turbio/gs/'

    videator('juguete-turbio_gs', path_original, path_output)

    path_original = 'data/vids/juguete-turbio/sat/'
    path_output = 'data/output/juguete-turbio/sat/'
    
    videator('juguete-turbio_sat', path_original, path_output)

if __name__ == "__main__":
    main()
