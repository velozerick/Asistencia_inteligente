import cv2
import os

class Extraccion_rostros:

    def pinguino(self):
        imagesPath = "C:\\Users\erick\Desktop\VELOZER\PROYECTO FINAL\Asistencia_inteligente\\fotos"

        if not os.path.exists("faces"):
            os.makedirs("faces")
            print("Nueva carpeta: faces")

        #Detector facial
        facecCassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml" )

        count = 0
        for imageName in os.listdir(imagesPath):
            print(imageName)
            image = cv2.imread(imagesPath + "/" + imageName)
            faces = facecCassif.detectMultiScale(image, 1.1,4)
            for(x,y,w,h) in faces:
                #cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2) 
                face = image[y:y + h, x:x + w]
                face = cv2.resize(face,(150,150))
                cv2.imwrite("faces/" + imageName , face)
                count +=1
        return 0