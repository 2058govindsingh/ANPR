import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.patches as patches
from skimage.measure import regionprops
from skimage import measure
from skimage.io import imread

IMAGE_PATH='D:\Documents\project\TPH\Images\png1\Test.png'
ans=""
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("png files",
                                                      "*.png"),("all files",
                                                      "*.*")
                                                     ))

    if(filename=="") :
        return
    global IMAGE_PATH
    IMAGE_PATH=filename
    print(filename)
    p1.configure(file=IMAGE_PATH)
    l3.configure(text="File Opened: "+filename)
    l3.place(x=200)
    l4.configure(text="")
    
    
def number_plate_recognition():
    global ans
    l4.configure(text="")
    if IMAGE_PATH=='D:\Documents\project\TPH\Images\png1\Test.png':
        messagebox.showerror('ERROR!','Please Select Some Image')
    else:
        if(IMAGE_PATH[:36]=='D:/Documents/project/TPH/Images/png1'):
            img=cv2.imread(IMAGE_PATH[:35]+'2'+IMAGE_PATH[36:])
        else:
            img=cv2.imread(IMAGE_PATH)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        if(ckvar.get()==1):
            plt.imshow(cv2.cvtColor(gray,cv2.COLOR_BGR2RGB))
            plt.title="GrayScale Image"
            plt.show()
        bfilter =cv2.bilateralFilter(gray,11,17,17)
        edged=cv2.Canny(bfilter,30,200)
        if(ckvar.get()==1):
            plt.imshow(cv2.cvtColor(edged,cv2.COLOR_BGR2RGB))
            plt.title="Edged Image"
            plt.show()
            label_image = measure.label(edged)
            plate_objects_cordinates = []
            plate_like_objects = []
            fig, (ax1) = plt.subplots(1)
            ax1.imshow(edged, cmap="gray")
            flag = 0
            for region in regionprops(label_image):
                if region.area < 50:
                    continue
                min_row, min_col, max_row, max_col = region.bbox
                region_height = max_row - min_row
                region_width = max_col - min_col
                flag = 1
                plate_like_objects.append(edged[min_row:max_row, min_col:max_col])
                plate_objects_cordinates.append((min_row, min_col, max_row, max_col))
                rectBorder = patches.Rectangle((min_col, min_row), max_col - min_col, max_row - min_row,
                                            edgecolor="red",
                                            linewidth=2, fill=False)
                ax1.add_patch(rectBorder)
            if (flag == 1):
                plt.show()
        # all approx proper shapes will be stored in keypoints
        keypoints= cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contours=imutils.grab_contours(keypoints)
        contours=sorted(contours,key=cv2.contourArea,reverse=True)[:10]
        location=None
        flag=0
        ref=""
        for contour in contours:
            approx =cv2.approxPolyDP(contour,10,True)
            if(len(approx))==4:
                location=approx
                mask=np.zeros(gray.shape,np.uint8)
                new_image =cv2.drawContours(mask,[location],0,255,-1)
                new_image=cv2.bitwise_and(img,img,mask=mask)
                (x,y)=np.where(mask==255)
                (x1,y1)=(np.min(x),np.min(y))
                (x2,y2)=(np.max(x),np.max(y))
                cropped_image=gray[x1:x2+1,y1:y2+1]
                reader = easyocr.Reader(['en'])
                result = reader.readtext(cropped_image,paragraph="False")
                if(len(result)==0):
                    continue
                else:
                    if(len(result[0][-1])<7 or len(result[0][-1])>12):
                        continue
                    flag=1
                    ref=result[0][-1]
                    break
        if flag==0:
            ans="Number Plate Not Found"
            l4.configure(text=ans,fg="black")
        else:
            mask=np.zeros(gray.shape,np.uint8)
            new_image =cv2.drawContours(mask,[location],0,255,-1)
            new_image=cv2.bitwise_and(img,img,mask=mask)
            if(ckvar.get()==1):
                plt.imshow(cv2.cvtColor(new_image,cv2.COLOR_BGR2RGB))
                plt.show()
            (x,y)=np.where(mask==255)
            (x1,y1)=(np.min(x),np.min(y))
            (x2,y2)=(np.max(x),np.max(y))
            cropped_image=gray[x1:x2+1,y1:y2+1]
            if(ckvar.get()==1):
                plt.imshow(cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB))
                plt.show()
            reader = easyocr.Reader(['en'])
            result = reader.readtext(cropped_image,paragraph="False")
            ans=ref
            l4.configure(text="The License plate number is:\n"+ans,fg="black")
            

    return

window = Tk()
window.title('ANPR')

window.geometry("1000x600")
window.maxsize(1000,600)
window.config(background="white")

l2=Label(window,text="Automatic Number Plate Recognition",font=("permanent marker",35, "bold"),fg="#57106B",bg="white")
l2.place(x=50,y=10)
l3=Label(window,text="No image is selected",font=("aleo",15,"bold"),fg="gray",bg="white")
l3.place(x=400,y=100)
Button(window,text="Browse",command=browseFiles,cursor="hand2",font=("aleo",25,"bold"),fg="white",bg="#57106B").place(x=375,y=145,height=50,width=250)

f1=Frame(window,bg="#57106B").place(x=20,y=250,width=600,height=330)
Label(f1,text="CLICK ON BROWSE BUTTON ",font=("aleo",15,"bold"),fg="white",bg="#57106B").place(x=150,y=380)
p1=PhotoImage(file=IMAGE_PATH)
Label(f1,image=p1).place(x=20,y=250)
#Tap button
b2=Button(window,text="Extract License Plate Number",command=number_plate_recognition,cursor="hand2",font=("aleo",15,"bold"),fg="white",bg="#57106B").place(x=675,y=295,height=50,width=300)
#checkbox
ckvar=IntVar()
ckbutton=Checkbutton(f1,text="Show Steps",font=("aleo",15,"bold"),bg="white",variable=ckvar)
ckbutton.place(x=685,y=355)

l4= Label(window,text=ans,font=("aleo",15,"bold"),fg="gray",bg="white")
l4.place(x=670,y=450)

window.mainloop()
