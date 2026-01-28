# import cv2 as cv
# import numpy as np
# import urllib.request

# def read_img_url(url):
#     req = urllib.request.urlopen(url)
#     img_rw = np.asarray( bytearray(req.read()), dtype=np.uint8)
#     img = cv.imdecode(img_rw, cv.IMREAD_COLOR)
#     return img 

# def add_noise(img):
#     mean = 0
#     sigma = 50
#     noisy = np.random.normal(mean, sigma, img.shape)
#     new_img = np.clip( img + noisy, 0, 255 ).astype(np.uint8)
#     return new_img

# def add_muoi_tieu(img, ratio=0.02):
#     nosy = img.copy()
#     soluong = int(ratio*img.size)

#     #rac muoi
#     toado = [np.random.randint(0, i-1,soluong) for i in img.shape]
#     nosy [ toado[0], toado[1]] = 255
#     #rac tieu
#     toado = [np.random.randint(0, i-1,soluong) for i in img.shape]
#     nosy [ toado[0], toado[1]] = 0

#     return nosy

# if __name__=="__main__":
#     url = "https://raw.githubusercontent.com/udacity/CarND-LaneLines-P1/master/test_images/solidWhiteCurve.jpg"
#     anh_goc = read_img_url(url)
#     cv.imshow("img",anh_goc)
#     cv.waitKey(0)
#     cv.destroyAllWindows()

#     edge = cv.Canny(anh_goc,50, 150)
#     cv.imshow("edge", edge)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
    
#Hình ảnh có hạt mè

import cv2 as cv
import numpy as np
import urllib.request

def read_img_url(url):
    req = urllib.request.urlopen(url)
    img_rw = np.asarray( bytearray(req.read()), dtype=np.uint8)
    img = cv.imdecode(img_rw, cv.IMREAD_COLOR)
    return img 

def add_noise(img):
    mean = 0
    sigma = 50
    noisy = np.random.normal(mean, sigma, img.shape)
    new_img = np.clip( img + noisy, 0, 255 ).astype(np.uint8)
    return new_img

def add_muoi_tieu(img, ratio=0.02):
    nosy = img.copy()
    soluong = int(ratio*img.size)

    #rac muoi
    toado = [np.random.randint(0, i-1,soluong) for i in img.shape]
    nosy [ toado[0], toado[1]] = 255
    #rac tieu
    toado = [np.random.randint(0, i-1,soluong) for i in img.shape]
    nosy [ toado[0], toado[1]] = 0

    return nosy

if __name__=="__main__":
    img = cv.imread(r"C:\Users\USer\Desktop\test\opencv_python\image\giaothong.jpg",cv.IMREAD_COLOR)  
    # cv.imshow("img",img)
    # cv.waitKey()
    # cv.destroyAllWindows()

    img2 = img.copy()
    clean_img = cv.medianBlur(img2, 5) #Lọc nhiễu số 2
    img3 = np.concatenate((img, clean_img), axis=1)
    cv.imshow("img3",img3)
    cv.waitKey(0)
    cv.destroyAllWindows()

    edge = cv.Canny(clean_img,50,150)
    cv.imshow("edge",edge)
    cv.waitKey(0)
    cv.destroyAllWindows()
