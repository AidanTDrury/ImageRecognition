from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import mpldatacursor
import os, fnmatch
def ImagePlot(img,CPHCy,CPHCx,CPBCy,CPBCx,m):
    imgplot = plt.imshow(img,  cmap='gray', interpolation="nearest")
    plt.imshow(img, cmap='gray',interpolation="nearest")
    #plt.scatter(CPHCx,CPHCy,color='black')
    #plt.scatter(CPBCx,CPBCy,color='white')
    contours = plt.contour(img, 3, cmap='RdGy')
    plt.clabel(contours, inline=True, fontsize=8)
    #plt.contour(img,cmap='RdGy')
    mpldatacursor.datacursor(hover=True, bbox=dict(alpha=1, fc='w'))
    plt.axis('on')
    plt.show()
def ImageDataAlgorithms(img):
    n=0
    nn=0
    m=[]
    PHC=[]
    CPHCx=[]
    CPHCy=[]
    PBC=[]
    CPBCx=[]
    CPBCy=[]
    while n<(img.shape[0]/1.05):
        px1=img[n,nn]
        px2=img[n,nn+1]
        nn+=1
        if nn==(img.shape[1]-1):
            n+=1
            nn=0
            continue
        if(
            px1<=80
            and px1>=5
            and px1>px2
        ):
            PHC.append(px1)
            CPHCx.append(nn)
            CPHCy.append(n)
        elif(
            px1>=210
            ):
            PBC.append(px1)
            CPBCx.append(nn)
            CPBCy.append(n)
    BC=np.asarray((CPBCy,CPBCx), dtype='int64')
    HC=np.asarray((CPHCy,CPHCx), dtype='int64')
    ImagePlot(img,CPHCy,CPHCx,CPBCy,CPBCx,m)
def ImageFormat(img):
    img.thumbnail((256, 256), Image.ANTIALIAS)
    img=np.asarray(img,dtype='int64')
    ImageDataAlgorithms(img)
def ImageGet(imagename):
    img = Image.open(imagename).convert('L')
    ImageFormat(img)
def Images():
    listOfFiles = os.listdir('.')  
    pattern = "*.jpg"
    images=[]
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
                images.append(entry)
    for i in images:
        print(i)
    
def Order():
    Images()
    imagename=input()+'.jpg'
    ImageGet(imagename)
Order()
