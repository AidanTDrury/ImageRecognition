from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import mpldatacursor

def ImagePlot(img,Px,Py):
    imgplot = plt.imshow(img,  cmap='gray', interpolation="nearest")
    plt.imshow(img, cmap='gray',interpolation="nearest")
    plt.plot(Px,Py,color='yellow')
    mpldatacursor.datacursor(hover=True, bbox=dict(alpha=1, fc='w'))
    plt.axis('on')
    plt.show()
def ImageHairLineIndicator(img):
    def HairLine(PHairLinesCount):
        count=0
        HairLineStart=0
        if len(PHairLinesCount)!=1:
            while count<len(PHairLinesCount)-1:
                if(
                    PHairLinesCount[count]==(PHairLinesCount[count+1]-1)
                    or
                    PHairLinesCount[count]==(PHairLinesCount[count+1]+1)
                    or
                    PHairLinesCount[count]==(PHairLinesCount[count+1])
                    or
                    PHairLinesCount[count]==(PHairLinesCount[count-1]-1)
                    or
                    PHairLinesCount[count]==(PHairLinesCount[count-1]+1)
                    or
                    PHairLinesCount[count]==(PHairLinesCount[count-1])
                    or
                    PHairLinesCount[count+1]-3==PHairLinesCount[count]#>=HPupilCount[count+1]+3)
                    ):

                    HairLineStart=PHairLinesCount[count]
                    break
                count+=1
        else:
            HairLineStart=PHairLinesCount[0]
        HairLineEnd=(img.shape[1]-HairLineStart)
        HLS=HairLineStart
        HLE=HairLineEnd
        return HLS,HLE
    def PossibleHairLines(img):
        count=10
        ProbableHairLines=[]
        PHairLinesCount=[]
        while count<(img.shape[0]-img.shape[0]/1.5):
            PossibleHairLines=(
                            img[count][count]
                            +img[count+1][count]
                            +img[count+2][count]

                            +img[count][count+1]
                            +img[count+1][count+1]
                            +img[count+2][count+1]

                            +img[count][count+2]
                            +img[count+1][count+2]
                            +img[count+2][count+2]
                            )/9
            if(30<=PossibleHairLines<=40
               and img[count+1][count+1]<img[count+2][count+1]
               and img[count+1][count+1]<img[count-2][count+1]
               and img[count+1][count+1]<img[count+1][count+2]
               and img[count+1][count+1]<img[count+1][count-2]
                
               and
               (
                img[count+2][count+1]>=img[count+4][count+1]
               or img[count-2][count+1]>=img[count-4][count+1]
               or img[count+1][count+2]>=img[count+1][count+4]
               or img[count+1][count-2]>=img[count+1][count-4]
               )
               ):
                ProbableHairLines.append(PossibleHairLines)
                PHairLinesCount.append(count+1)
            count+=1
        print(ProbableHairLines)
        HLS,HLE=HairLine(PHairLinesCount)
        return HLS,HLE
    HLS,HLE=PossibleHairLines(img)
    return HLS,HLE
def ImageFormat(img):
    img=Image.open(img).convert('L')
    img.thumbnail((256, 256), Image.ANTIALIAS)
    img=np.asarray(img,dtype='int64')
    #img = img[25:195,6:]
    Y=img.shape[0]
    X=img.shape[0]
    HLS,HLE=ImageHairLineIndicator(img)
    Px=[HLS,HLE]
    Py=[HLS,HLS]
    Px=np.asarray(Px,dtype='int64')
    Py=np.asarray(Py,dtype='int64')
    ImagePlot(img,Px,Py)
def ImageGet(imgN):
    img = Image.open(imgN+'.jpg').convert('L')
    ImageFormat(img)
def Order():
    imgName=input()+'.jpg'
    ImageFormat(imgName)
Order()
