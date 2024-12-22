# Для роботи з комп’ютерним зором у Python є OpenCV (Open Source Computer Vision Library). 
# Дозволяє працювати з камерами, обробляти зображення, розпізнавати об’єкти та багато іншого.

# Встановлення OpenCV

# pip install opencv-python

# Роширені можливості OpenCV робота з відео

# pip install opencv-contrib-python

# ВІДКРИВАННЯ ЗОБРАЖЕННЯ
# # Імпорт модуля OpenCV
# import cv2
# # Завантаження зображення
# image = cv2.imread('C:\\Users\\olegz\\Desktop\\Coding\\experiment_code\\image\\wp12194597.jpg')
# # Відображення зображення
# cv2.imshow("Image", image)
# # Чекаємо, на натискання калвіші
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ПОКАЗ ЗОБРАЖЕННЯ З КАМЕРИ
# # Імпортувати модуль OpenCV
# import cv2
# # Підключення до камери
# cam = cv2.VideoCapture(0)
# while True:
#     # Зчитуємо кадр
#     frame = cam.read()[1]
#     # Відображення
#     cv2.imshow("Camera", frame)
#     # Очікування натискання / клавіші 't'
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
# # Закриваємо камеру
# cam.release()
# cv2.destroyAllWindows()

# НАКЛАДАННЯ ФІЛЬТРА НА ЗОБРАЖЕННЯ
# # Імпортувати модуль
# import cv2
# # Відкрити катритну
# img = cv2.imread("C:\\Users\\olegz\\Desktop\\Coding\\experiment_code\\image\\wp12194597.jpg")
# # Фільтр
# blue_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# # Відобразити
# cv2.imshow("Image", blue_img)
# while True:
#     # Очікавання натискання
#     if cv2.waitKey(0) & 0xFF == ord("q"):
#         # Закриття
#         cv2.destroyAllWindows()

# РОЗПІЗНАВАННЯ ОБЛИЧ ЗА ДОПОМОГОЮ МОДЕЛІ HAAR CASCADE
# Імпорт OpenCV
import cv2
import cv2.data
# Запуск камери
camera = cv2.VideoCapture(0)
# Завантаження моделі haar cascade
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')
while True:
    # Зчитування з камери
    camera_frame = camera.read()[1]
    # Фільтр
    camera_filt = cv2.cvtColor(camera_frame, cv2.COLOR_BGR2GRAY)
    # Розпізнаємо обличчя
    face = haar_cascade.detectMultiScale(camera_filt, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Прямоктуник навколо обличчя
    for (x, y, w, h) in face:
        cv2.rectangle(camera_filt, (x, y), (x+w, y+h), (255, 0, 0), 1)
    # Відмалювування
    cv2.imshow("Camera Face", camera_filt)
    # Очіуквання натискання / натискання з умовю на 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# Закриття камери
camera.release()
# Закриття вікон
cv2.destroyAllWindows()