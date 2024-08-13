import cv2 as cv

video=cv.VideoCapture('How Much Can Your Sharingan See_ _ Naruto Shippuden.mp4')

sub=cv.createBackgroundSubtractorMOG2(20,10)

while True:
   ret, frame=video.read()
   if ret:
       mask=sub.apply(frame)
       cv.imshow('mask',mask)
       if cv.waitKey(5)==ord('x'):
           break
   else:
       video = cv.VideoCapture('How Much Can Your Sharingan See_ _ Naruto Shippuden.mp4')

cv.destroyAllWindows()
video.release()
