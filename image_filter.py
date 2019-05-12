import cv2
import numpy as np

class Cartoonizer:
    """Cartoonizer effect
        A class that applies a cartoon effect to an image.
        The class uses a bilateral filter and adaptive thresholding to create
        a cartoon effect.
    """
    def __init__(self):
        pass

    def render(self, img_rgb):
        img_rgb = cv2.imread(img_rgb)
        img_rgb = cv2.resize(img_rgb, (1366,768))
        numDownSamples = 2       # number of downscaling steps
        numBilateralFilters = 50  # number of bilateral filtering steps
        # downsample image using Gaussian pyramid
        img_color = img_rgb
        for _ in range(numDownSamples):
            img_color = cv2.pyrDown(img_color)
        

        # repeatedly apply small bilateral filter instead of applying
        # one large filter
        for _ in range(numBilateralFilters):
            img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
      

        # upsample image to original size
        for _ in range(numDownSamples):
            img_color = cv2.pyrUp(img_color)
     
        # convert to grayscale and apply median blur
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        img_blur = cv2.medianBlur(img_gray, 7)
      
        # detect and enhance edges
        img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                         cv2.ADAPTIVE_THRESH_MEAN_C,
                                         cv2.THRESH_BINARY, 9, 2)
       
        # convert back to color so that it can be bit-ANDed with color image
        (x,y,z) = img_color.shape
        img_edge = cv2.resize(img_edge,(y,x)) 
        img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
      
        
        return cv2.bitwise_and(img_color, img_edge)
class Paint:
    def __init__(self):
        pass

    def render(self, img_rgb):
        img_rgb = cv2.imread(img_rgb)
        img_rgb = cv2.resize(img_rgb, (1366,768))
        numDownSamples = 2       # number of downscaling steps
        numBilateralFilters = 50  # number of bilateral filtering steps

        # downsample image using Gaussian pyramid
        img_color = img_rgb
        for _ in range(numDownSamples):
            img_color = cv2.pyrDown(img_color)
        

        # repeatedly apply small bilateral filter instead of applying
        # one large filter
      
        # upsample image to original size
        for _ in range(numDownSamples):
            img_color = cv2.pyrUp(img_color)
     

        # convert to grayscale and apply median blur
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
       
        (x,y,z) = img_color.shape
        img_gray = cv2.resize(img_gray,(y,x)) 
        img_gray = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)
        return cv2.bitwise_and(img_color, img_gray)
class Gray:
   def render(self, img_rgb):
        img_rgb = cv2.imread(img_rgb)
        # convert color to grayscale
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        img_gray = cv2.resize(img_gray,(1366,768)) 
        
        return img_gray
class Blur:
   def render(self, img_rgb):
        img_rgb = cv2.imread(img_rgb)
        # convert to Blur
        # img_gray = cv2.GaussianBlur(img_rgb, (9, 9), 5) 
        img_blur = cv2.medianBlur(img_rgb, 5)
        img_blur = cv2.resize(img_blur,(1366,768)) 
   
  
        return img_blur
class Sepia:
   def render(self, img_rgb):
        img_rgb = cv2.imread(img_rgb)
        # convert to Blur
        # img_gray = cv2.GaussianBlur(img_rgb, (9, 9), 5) 
        img_sepia = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2YCrCb)
        img_sepia = cv2.resize(img_sepia,(1366,768)) 
   
  
        return img_sepia
class Blend:
   def render(self, img_rgb):
        img_rgb = cv2.imread(img_rgb)
        # convert to Blur
        # img_gray = cv2.GaussianBlur(img_rgb, (9, 9), 5) 
        img_blend = cv2.cvtColor(img_rgb,cv2.CV_64F) 
        img_blend = cv2.resize(img_blend,(1366,768)) 
   
  
        return img_blend
file_name = input("Enter Image Name ")
i=int(input("Enter your choice:\n1.Paint\n2.Cartoon\n3.Gray\n4.Sepia\n5.Blur\n6.Blend\n"))
if(i==1):
	tmp_canvas = Paint()
elif(i==2):
	tmp_canvas = Cartoonizer()
elif(i==3):
    tmp_canvas = Gray()
elif(i==4):
    tmp_canvas = Sepia()
elif(i==5):
    tmp_canvas = Blur()
elif(i==6):
    tmp_canvas = Blend()
else:
    print("Please enter Correct Choice!!!")
#file_name = input('enter image name')

res = tmp_canvas.render(file_name)
cv2.imwrite("Cartoon version.jpg", res)
cv2.imshow("Cartoon version", res)
cv2.waitKey(0)
cv2.destroyAllWindows()