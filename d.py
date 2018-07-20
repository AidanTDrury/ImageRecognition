import numpy as np
from PIL import Image
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
import mpldatacursor
import os, fnmatch
listOfFiles = os.listdir('.')  
pattern = "*.jpg"
images=[]
for entry in listOfFiles:  
    if fnmatch.fnmatch(entry, pattern):
            images.append(entry)
for i in images:
    print(i)

imagename=input()+'.jpg'
img = Image.open(imagename).convert('L')
img.thumbnail((128,128), Image.ANTIALIAS)
img=np.asarray(img,dtype='int64')

x=[]
y=[]
n=0
nn=0
while n<(img.shape[0]/1.05):
        px1=img[n,nn]
        px2=img[n,nn+1]
        nn+=1
        if nn==(img.shape[1]-1):
            n+=1
            nn=0
            continue
        px=img[n,nn]
        Data=[img[n-1,nn-1],img[n-1,nn],img[n-1,nn+1]

              ,img[n,nn-1],px,img[n,nn+1]

              ,img[n+1,nn-1],img[n+1,nn],img[n+1,nn+1]
              ]
        #print("\n\n--------------\n",img[n-1,nn-1],img[n-1,nn],img[n-1,nn+1])
        #print(img[n,nn-1],px,img[n,nn+1])
        #print(img[n+1,nn-1],img[n+1,nn],img[n+1,nn+1])
        DataAim=min(Data)
        if px==DataAim:
            print(True)
            #print(DataAim)
        else:
            count=0
            while count<len(Data):
                #print(count)
                if Data[count]==DataAim:
                    px=img[n,nn]
                    y.append(n)
                    y.append(n+1)
                    x.append(nn)
                    x.append(nn+1)
                    #print(True)
                    break
                count+=1
            #print(count,px,"To",DataAim)0
plt.figure()
imgplot = plt.imshow(img,  cmap='gray', interpolation="nearest")
plt.imshow(img, cmap='gray',interpolation="nearest")
plt.plot(x,y,x[1:],y[1:],linewidth=.5,linestyle='-.',color='gray')
plt.show()
