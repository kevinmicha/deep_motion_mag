
import cv2
import os

# determine what OpenCV version we are using
try:
    import cv2.cv as cv

    USE_CV2 = True
except ImportError:
    # OpenCV 3.x does not have cv2.cv submodule
    USE_CV2 = False

def frame_to_grayscale(frame):
    '''
    Convert current frame color to grayscale
    '''

    # convert to gray image
    grayIm = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)


    return grayIm

################# main script
def main():

    # path to folder with frames to convert

    #video = 'guitar'
    video = 'juguete-turbio'

    path = 'data/vids/'+video+'/'

    # path to folder with grayscale frames
    output_path = 'data/vids/'+video+'/gs/'

    # Check whether the specified path exists or not
    isExist = os.path.exists(output_path)

    if not isExist:
        # Create a new directory because it does not exist 
        os.makedirs(output_path)
    
    print("Grayscale frames will be stored in "+output_path)

    count = 0

    namelist = sorted(os.listdir(path))

    for filename in namelist:
        if filename.endswith(".png"):
            count += 1
            frame = cv2.imread(path+filename)

            if frame is not None:

                gs_frame = frame_to_grayscale(frame)

                name = output_path + '%04d.png' % (count)

                cv2.imwrite(name,gs_frame)

if __name__ == "__main__":
    main()
