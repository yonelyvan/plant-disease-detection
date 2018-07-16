import cv2
imagen = cv2.imread("img.jpg")
cv2.imshow("ventana", imagen)

gray_image = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow("gris", gray_image)

#sin_ruido = cv2.GaussianBlur(gray_image,(3,3),0)#pierde detalle
#cv2.imshow("sin ruido", sin_ruido)

#unblalizacion
ret,thresh1 = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)
cv2.imshow("threashold", thresh1)





cv2.waitKey(0)