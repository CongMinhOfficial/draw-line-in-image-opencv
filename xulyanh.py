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
#     url = "https://raw.githubusercontent.com/opencv/opencv/refs/heads/4.x/samples/data/lena.jpg"
#     anh_goc = read_img_url(url)
#     # cv.imshow("img",anh_goc)
#     # cv.waitKey(0)
#     # cv.destroyAllWindows()
    
#     anh_nam = add_noise(anh_goc)
#     # cv.imshow("img2",anh_nam)
#     # cv.waitKey(0)
#     # cv.destroyAllWindows()

#     # img3 = np.concatenate((img, img2), axis=1)
#     # # cv.imshow("img3",img3)
#     # cv.waitKey(0)
#     # cv.destroyAllWindows()

#     anh_muoi_tieu = add_muoi_tieu(anh_goc, 0.03)

#     img2 = anh_muoi_tieu.copy()
#     clean_img = cv.blur(img2, (3,3)) #Lọc nhiễu số 1
#     img3 = np.concatenate((anh_muoi_tieu, clean_img, anh_goc),axis = 1)
#     cv.imshow("img3",img3)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
#     # img_n = anh_muoi_tieu.copy()
#     # n,m,_= anh_muoi_tieu.shape
#     # for i in range(n):
#     #     for j in range(m):
#     #         if img_n[i,j] == 255:
#     img4 = anh_muoi_tieu.copy()
#     clean_img = cv.medianBlur(img4, 5) #Lọc nhiễu số 2
#     img5 = np.concatenate((anh_muoi_tieu, clean_img, anh_goc),axis = 1)
#     cv.imshow("img5",img5)
#     cv.waitKey(0)
#     cv.destroyAllWindows()

#     ed1 = cv.Canny(anh_muoi_tieu, 50 , 150)
#     ed2 = cv.Canny(clean_img, 50 , 150)
#     ed3 = cv.Canny(anh_goc, 50 , 150)
#     img7 = np.concatenate((ed1, ed2, ed3),axis = 1)
#     cv.imshow("img7",img7)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
#     img6 = np.concatenate((anh_goc,anh_nam,anh_muoi_tieu), axis=1)
#     # cv.imshow("img6",img6)
#     # cv.waitKey(0)
#     # cv.destroyAllWindows()
