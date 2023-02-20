import numpy as np


IMAGE_PATH = "./Resources/Lenna.jpg"
CZI_IMGAE_PATH = "./Resources/Osteosarcoma_01.czi"

# ------------ Pillow ------------

# from PIL import Image

# img = Image.open(IMAGE_PATH)        # does not return numpy array
# print(type(img))                    # type PngImageFile
# img.show()                          # opens image in new window
# np_image = np.asarray(img)          # converts our imagae to a numpy array
# print(type(np_image))               # type numpy array

# ------------ Matplotlib : for plotting usually ------------

# import matplotlib.pyplot as plt
# import matplotlib.image as mpimage

# img = mpimage.imread(IMAGE_PATH)    # returns numpy array
# print(img.shape)                    # returns dimesntion of image
# plt.imshow(img)

# ------------ Scikit Image : Used for image processing ------------

# from skimage import io, img_as_float, img_as_ubyte
# import matplotlib.pyplot as plt

# img = io.imread(IMAGE_PATH)         # return a numpy array
# print(type(img))
# plt.imshow(img)

# img_float = img_as_float(img)       # returns image as numpy array values b/w 0 and 1
# print(img_float)

# img_float_2 = io.imread(IMAGE_PATH).astype(float)   # returns image as numpy array values b/w 0 and 255
# print(img)

# ------------ Open CV: Genrally used for Computer vision and NN ------------

# import cv2
# import matplotlib.pyplot as plt

# img_grey = cv2.imread(IMAGE_PATH, 0)        # returns grey image as numpy array
# img_color = cv2.imread(IMAGE_PATH, 1)       # returns color image as numpy array

# print(type(img_grey))

# cv2.imshow("Grey Image", img_grey)
# cv2.imshow("Color Image", img_color)
    
# plt.imshow(img_color)                       # this will show image with inverted color because cv2 handles as BGR not RGB
# img_bgr2rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)    # convert BGR to RGB
# plt.imshow(img_bgr2rgb)
# cv2.waitKey(0)                              # wait untill key is pressed
# cv2.destroyAllWindows()                     # destroy all created windows

# ------------ Prosperity format: CZI file: for czi file format ------------

# import czifile
# img = czifile.imread(CZI_IMGAE_PATH)
# print(img.shape)

# ------------ All the images inside a folder ------------

# Folder_Path = "./Resources/*"
# import glob
# import cv2

# for file in glob.glob(Folder_Path):
#     print(file)