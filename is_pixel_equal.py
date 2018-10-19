import time
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
image1=Image.open("d:\\captcha1.png")
image2=Image.open("d:\\captcha2.png")
def is_pixel_equal(image1, image2, x, y):
    pixel1 = image1.load()[x, y]
    pixel2 = image2.load()[x, y]
    threshold = 60
    if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
            pixel1[2] - pixel2[2]) < threshold:
        return True
    else:
        return False
def get_gap():
    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            b=is_pixel_equal(image1,image2,i,j)
            if b==False:
                it=(i,j)
                yield it
item_list=get_gap()
for i in item_list:
    print(i)
        

