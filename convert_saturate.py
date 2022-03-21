import cv2
import os
from PIL import ImageEnhance
from PIL import Image


def frame_saturate(frame):
    '''
    Saturate current frame
    '''

    converter = ImageEnhance.Color(frame)
    Im_sat = converter.enhance(2.0)   

    return Im_sat

################# main script
def main():

    # path to folder with frames to convert
    path = 'data/vids/juguete-turbio/'

    # path to folder with grayscale frames
    output_path = 'data/vids/juguete-turbio/sat/'

    # Check whether the specified path exists or not
    isExist = os.path.exists(output_path)

    if not isExist:
        # Create a new directory because it does not exist 
        os.makedirs(output_path)
    
    print("Saturated frames will be stored in "+output_path)

    count = 0

    namelist = sorted(os.listdir(path))

    for filename in namelist:
        if filename.endswith(".png"):
            count += 1

            frame = Image.open(path+filename)

            if frame is not None:

                sat_frame = frame_saturate(frame)

                name = output_path + '%d.png' % (count)

                sat_frame.save(name)

if __name__ == "__main__":
    main()
