# import cv2 as cv
# import numpy as np

# img = cv.imread(r'C:\Users\USer\Desktop\test\opencv_python\image\image.png')
# img = cv.resize(img, (640,480))

# def make_coordinates(image, line_parameters):
#     """Chuyển đổi slope và intercept thành tọa độ điểm để vẽ"""
#     try:
#         slope, intercept = line_parameters
#     except:
#         return None
    
#     # Xác định chiều cao để vẽ đường thẳng (từ đáy ảnh lên đến 60% ảnh)
#     y1 = image.shape[0]
#     y2 = int(y1 * 0.6)
    
#     # Từ phương trình $y = mx + b$ suy ra $x = \frac{y - b}{m}$
#     x1 = int((y1 - intercept) / slope)
#     x2 = int((y2 - intercept) / slope)
#     return np.array([x1, y1, x2, y2])

# def average_slope_intercept(image, lines):
#     """Gom nhóm các đoạn vạch đứt thành 2 đường thẳng duy nhất"""
#     left_fit = []
#     right_fit = []
#     if lines is None:
#         return None
    
#     for line in lines:
#         x1, y1, x2, y2 = line[0]
#         # Tính toán hệ số đường thẳng bằng polyfit
#         parameters = np.polyfit((x1, x2), (y1, y2), 1)
#         slope = parameters[0]
#         intercept = parameters[1]
        
#         # Lọc bỏ nhiễu: chỉ lấy các đường có độ dốc phù hợp với làn đường
#         if abs(slope) < 0.4 or abs(slope) > 0.9:
#             continue
            
#         if slope < 0: # Bên trái (trục Y hướng xuống nên slope âm là bên trái)
#             left_fit.append((slope, intercept))
#         else:         # Bên phải
#             right_fit.append((slope, intercept))
            
#     # Tính trung bình cộng và tạo tọa độ
#     left_line = make_coordinates(image, np.average(left_fit, axis=0)) if left_fit else None
#     right_line = make_coordinates(image, np.average(right_fit, axis=0)) if right_fit else None
    
#     lines_to_draw = [l for l in [left_line, right_line] if l is not None]
#     return np.array(lines_to_draw) if lines_to_draw else None

# # --- BẮT ĐẦU XỬ LÝ ---
# img = cv.imread('image_9673da.jpg') # Đảm bảo đúng tên file ảnh của bạn
# if img is None:
#     print("Không tìm thấy ảnh!")
#     exit()

# img = cv.resize(img, (640, 480))
# h, w = img.shape[:2]

# # 1. Lọc màu (HLS giúp tách vạch trắng/vàng tốt hơn Gray thông thường)
# hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)
# white_mask = cv.inRange(hls, np.array([0, 200, 0]), np.array([180, 255, 255]))
# yellow_mask = cv.inRange(hls, np.array([10, 0, 100]), np.array([40, 255, 255]))
# mask_combined = cv.bitwise_or(white_mask, yellow_mask)
# res = cv.bitwise_and(img, img, mask=mask_combined)

# # 2. Phát hiện cạnh (Canny)
# gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(gray, (5, 5), 0)
# edge = cv.Canny(blur, 50, 150)

# # 3. Giới hạn vùng quan tâm (ROI) - Hình thang tập trung vào làn đường
# mask = np.zeros_like(edge)
# polygon = np.array([[
#     (0, h),
#     (w, h),
#     (w//2 + 120, h//2 + 60),
#     (w//2 - 120, h//2 + 60)
# ]], dtype=np.int32)
# cv.fillPoly(mask, polygon, 255)
# roi = cv.bitwise_and(edge, mask)

# # 4. Tìm các đường thẳng (Hough Lines)
# lines = cv.HoughLinesP(roi, 1, np.pi/180, 20, minLineLength=20, maxLineGap=200)

# # 5. Vẽ kết quả
# averaged_lines = average_slope_intercept(img, lines)
# img_line = img.copy()

# if averaged_lines is not None:
#     for line in averaged_lines:
#         x1, y1, x2, y2 = line
#         cv.line(img_line, (x1, y1), (x2, y2), (0, 0, 255), 8) # Đường đỏ dày 8px cho rõ

# cv.imshow("Lane Detection Improved", img_line)
# cv.waitKey(0)
# cv.destroyAllWindows()

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# edge = cv.Canny(gray, 50, 150)

# h, w = edge.shape
# mask = np.zeros_like(edge)

# polygon = np.array([[
#     (0, h),
#     (w, h),
#     (w//2 + 80, h//2),
#     (w//2 - 80, h//2)
# ]], dtype=np.int32)

# cv.fillPoly(mask, polygon, 255)
# roi = cv.bitwise_and(edge, mask)

# def make_coordinates(image, line_parameters):
#     """Hàm phụ trợ để chuyển đổi slope/intercept thành tọa độ pixel"""
#     try:
#         slope, intercept = line_parameters
#     except TypeError:
#         return None
#     y1 = image.shape[0]
#     y2 = int(y1 * 0.6)  # Vẽ lên đến 60% chiều cao ảnh
#     x1 = int((y1 - intercept) / slope)
#     x2 = int((y2 - intercept) / slope)
#     return np.array([x1, y1, x2, y2])

# def average_slope_intercept(image, lines):
#     """Gom nhóm các đoạn thẳng tìm được thành 2 đường bên trái và bên phải"""
#     left_fit = []
#     right_fit = []
#     if lines is None:
#         return None
    
#     for line in lines:
#         x1, y1, x2, y2 = line[0]
#         # Tính toán hệ số đường thẳng y = mx + b
#         parameters = np.polyfit((x1, x2), (y1, y2), 1)
#         slope = parameters[0]
#         intercept = parameters[1]
        
#         # Lọc bỏ các đường nằm ngang hoặc quá dốc không thực tế
#         if abs(slope) < 0.4 or abs(slope) > 0.9:
#             continue
            
#         if slope < 0: # Độ dốc âm là làn bên trái
#             left_fit.append((slope, intercept))
#         else:         # Độ dốc dương là làn bên phải
#             right_fit.append((slope, intercept))
            
#     left_line = make_coordinates(image, np.average(left_fit, axis=0)) if left_fit else None
#     right_line = make_coordinates(image, np.average(right_fit, axis=0)) if right_fit else None
    
#     return np.array([l for l in [left_line, right_line] if l is not None])

# # 1. Đọc và tiền xử lý ảnh
# img = cv.imread('image_9673da.jpg') # Thay bằng đường dẫn của bạn
# img = cv.resize(img, (640, 480))
# h, w = img.shape[:2]

# # 2. Lọc màu Trắng và Vàng (Quan trọng nhất để tránh vết bánh xe)
# hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)
# # Lọc màu trắng
# lower_white = np.array([0, 200, 0])
# upper_white = np.array([180, 255, 255])
# white_mask = cv.inRange(hls, lower_white, upper_white)
# # Lọc màu vàng
# lower_yellow = np.array([10, 0, 100])
# upper_yellow = np.array([40, 255, 255])
# yellow_mask = cv.inRange(hls, lower_yellow, upper_yellow)
# # Kết hợp mặt nạ
# mask_combined = cv.bitwise_or(white_mask, yellow_mask)
# res = cv.bitwise_and(img, img, mask=mask_combined)

# # 3. Canny Edge Detection trên ảnh đã lọc màu
# gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(gray, (5, 5), 0)
# edge = cv.Canny(blur, 50, 150)

# # 4. Vùng quan tâm (ROI)
# mask = np.zeros_like(edge)
# polygon = np.array([[
#     (0, h),
#     (w, h),
#     (w//2 + 100, h//2 + 50),
#     (w//2 - 100, h//2 + 50)
# ]], dtype=np.int32)
# cv.fillPoly(mask, polygon, 255)
# roi = cv.bitwise_and(edge, mask)

# # 5. Phát hiện đường thẳng Hough
# lines = cv.HoughLinesP(roi, 1, np.pi/180, 30, minLineLength=20, maxLineGap=150)

# # 6. Xử lý trung bình hóa và vẽ
# averaged_lines = average_slope_intercept(img, lines)

# img_line = img.copy()
# if averaged_lines is not None:
#     for line in averaged_lines:
#         x1, y1, x2, y2 = line
#         cv.line(img_line, (x1, y1), (x2, y2), (0, 0, 255), 5)

# # Hiển thị kết quả
# cv.imshow("Result", img_line)
# cv.waitKey(0)
# cv.destroyAllWindows()

# lines = cv.HoughLinesP(
#     roi,
#     rho=1,
#     theta=np.pi/180,
#     threshold=50,
#     minLineLength=50,
#     maxLineGap=100
# )

# img_line = img.copy()
# if lines is not None:
#     for line in lines:
#         x1, y1, x2, y2 = line[0]
#         cv.line(img_line, (x1, y1), (x2, y2), (0,0,255), 2)

# # cv.imshow("edge", edge)
# # cv.imshow("roi", roi)
# cv.imshow("lane detection", img_line)
# cv.waitKey(0)
# cv.destroyAllWindows()


# import cv2 as cv
# import numpy as np

# img = cv.imread(r'C:\Users\USer\Desktop\test\opencv_python\image\Flag_of_Vietnam.svg.webp')

# # 1️⃣ Chuyển sang HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# # 2️⃣ Khoảng màu vàng (có thể tinh chỉnh)
# lower_yellow = np.array([20, 100, 100])
# upper_yellow = np.array([35, 255, 255])

# # 3️⃣ Tạo mask cho sao vàng
# mask = cv.inRange(hsv, lower_yellow, upper_yellow)

# # 4️⃣ Dùng mask để lấy sao
# star = cv.bitwise_and(img, img, mask=mask)

# cv.imshow("mask", mask)
# cv.imshow("yellow_star", star)
# cv.waitKey(0)
# cv.destroyAllWindows()

