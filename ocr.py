import cv2
import matplotlib.pyplot as plt
import numpy as np
import easyocr
path='img.png'
reader=easyocr.Reader(['en'],gpu=False)
res=reader.readtext(path)
extracted_text = []
text=''
for result in res:
    extracted_text.append(result[1])
    text=text+' '+result[1]

print(extracted_text)
print(text)
