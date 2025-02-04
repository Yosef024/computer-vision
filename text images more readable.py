import cv2

var=cv2.imread("img.png")
cv2.imshow('image1',var)
cv2.waitKey(0)
var=cv2.cvtColor(var,cv2.COLOR_RGB2GRAY)
_,res=cv2.threshold(var,140,255,cv2.THRESH_BINARY)
adapt=cv2.adaptiveThreshold(var,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,20)
cv2.imshow('image',res)
cv2.imshow('image',adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()
