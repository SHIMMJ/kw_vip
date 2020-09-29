from PIL import Image
import matplotlib.pyplot as plt

#원본
image=Image.open("./lenna.png")
plt.imshow(image)
plt.show()

#좌우반전
image1=image.transpose(Image.FLIP_LEFT_RIGHT)
plt.imshow(image1)
plt.show()
#180도 회전
image2=image.transpose(Image.ROTATE_180)
plt.imshow(image2)
plt.show()
#가로, 세로 길이 2배 축소
image3=image.resize((int(image.width/2),int(image.height/2)))
plt.imshow(image3)
plt.show()

