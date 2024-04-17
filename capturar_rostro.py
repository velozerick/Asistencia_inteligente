import cv2

class Capturar_rostro:
    
    def cocodrilo(self, nombre_imagen, numero_cuenta):
        #Adquisición de Información
        count = 0
        #Iniciar Cámara
        cap = cv2.VideoCapture(0)

        #Capturar imagen y mostrarla en tiempo real
        while True:
            ret, frame = cap.read()
            cv2.imshow("frame", frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == ord('s'):
                count += 1
                filename = f"fotos/{nombre_imagen}_{numero_cuenta}.jpg"  # Concatenar número de cuenta al nombre de la imagen
                cv2.imwrite(filename, frame)
        cap.release()
        cv2.destroyAllWindows()
