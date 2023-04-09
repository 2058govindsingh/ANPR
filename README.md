# AUTOMATIC NUMBER PLATE RECOGNITION (ANPR)
Click [here](https://drive.google.com/file/d/1a52Jcj2OTLLYDQ6oF9aFt-7TRixo8XnX/view?usp=share_link) for the video presentation with app demo.
## GOAL AND OBJECTIVE :
➢ The main goal of this project is to detect and output the license plate number of the vehicles.

➢ The objective of this project is to develop a low cost, high efficient and accurate model to
achieve the goal.

➢ This can be achieved by making use of existing surveillance cameras in order to detect the
plate number by converting the video into frames. Therefore the consumption of any type of
hardware material is very less, making it cost-effective.

➢ The precision of the license plate number that is detected via this method is high as the
frames undergo filtration by converting it into an image in order to discard noise, if any.

➢ Additionally, the system is versatile enough to convert the extracted region of license plate
into text by using OCR (Optical Character Recognition). OCR is one of the finest Image
Preprocessing techniques and this makes the system more accurate.

➢ Considering the above mentioned features, an attempt is made to design the License Plate
Detection System.

## SCOPE :
➢ Automated solution that replaces the conventional way of noting down license plate numbers of the vehicles.

➢ Reduces errors.

➢ Produces high accurate results without compromising on the efficiency and making it a cost-effective system.

➢ Uses already existing infrastructure.

➢ Provides user-friendly software applications with no hardware materials used and with latest, efficient methodologies available in AI.

➢ Real time application.

## IMPLEMENTAION DETAILS :

In order to achieve accuracy and efficient results of license plate detection based on Machine
Learning, testing has been done on many factors.

Performance in various environments:

● Weather conditions

● Colour conflicts

● Rotation of image

● Transparency of the image

The main objective of the testing phase is to make sure that the final application is able to perform
flawlessly in terms of accuracy,consistency and performance.In order to achieve that,the
application needs to undergo testing for different scenarios such that the system is versatile enough
to detect any kind of image.

![image](https://user-images.githubusercontent.com/91799812/230790090-ae83df43-d0dd-445f-8214-dd68fd297005.png)

## Software Requirements :
The following describes the software requirements of the application:

● Python Programming Language:

  ● OpenCV 
  
  ● Numpy
  
  ● Matplotlib
  
  ● EasyOCR
  
  ● Scikit-image
  
## STAGES

  Step - 1:
  
    ● This is the first and foremost step of the model. In this stage, the video that is
    obtained from the camera is converted into the frames.
    
    ● Binarization : The frame which has a clear picture of license plate number is
    considered and is converted into gray scale image from rgb format image. This is
    done to improve the quality of the image and prepare it to the next stages.
    
    ● Noise removal : The gray scale image is further converted into binary image so that
    the unwanted information/data and noise is removed from the image while
    preserving the sharpness of the image. The Libraries used in this step are Opencv,
    numpy.
    
  ![image](https://user-images.githubusercontent.com/91799812/230790432-4022fa79-12dc-441d-9ab3-d719a09adf96.png)
  
  Step - 2:
  
    ● This is the second stage in the development of the project. In this stage, the binary
    image that is obtained from the above step, is used to extract the regions whose
    dimensions are similar to that of license plate number of the vehicle.
    
    ● These regions are extracted using the methods present in matplotlib library, stored in
    numpy array and further filtration is done on all extracted rectangular regions
    considering the height,width, coordinates of the extracted regions.
    
  ![image](https://user-images.githubusercontent.com/91799812/230790626-efe4fd68-e3f3-4fbe-aea7-ee792bbb7eec.png)
    
  Step - 3:

    ● In the last step, the rectangular patches that have been extracted in the above stage
    are subjected to OCR in order to determine the text from the image.
    This procedure consists of two important steps, training and recognition.

    ● Training : The program is first trained with a set of sample images for each of the
    characters to extract the important features based on which the recognition operation
    would be performed. Our program is trained on a set of 36 characters with 10
    samples of each.

    ● Recognition : Now for the extracted number plate we calculate the score for each of
    the characters present in the plate image.We calculate the matching score of the
    segmented character from the templates of the character stored by the following
    algorithm. We compare the pixel values of the matrix of segmented character and the
    template matrix, and for every match we add one to the matching score and for every
    mis-match we decrement the score by one. This is done for all 225 pixels. The match
    score is generated for every template and the one which gives the highest score is
    taken to be the recognized character.

  ![image](https://user-images.githubusercontent.com/91799812/230790709-a2e1c065-562a-40b9-8b0d-0566cb9db941.png)
    
