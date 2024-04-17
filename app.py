from flask import Flask
from flask import render_template, request, url_for, redirect,flash, Response
import os
import cv2
import os
from f_reconigtion import F_reconigtion
from extraccion_rostros import Extraccion_rostros
from capturar_rostro import Capturar_rostro

app=Flask(__name__,template_folder='template')
UPLOAD_FOLDER = 'C:\\Users\erick\Desktop\VELOZER\PROYECTO FINAL\Asistencia_inteligente\\fotos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# objeto extraccion
extra = Extraccion_rostros()
# objeto reconocimineot
recog = F_reconigtion()
# objeto capturar
captu = Capturar_rostro()


#CONFIGURACIONES PARA SESIONES?
app.secret_key='mysecretkey'
    
#DIRIGIMOS AL INDEX
@app.route('/')
def INDEX():
    return render_template('index.html')

#//////////////////////////////////////

@app.route('/capturar', methods=['GET', 'POST'])
def capturar_caras():
    nombre_imagen = request.form['nombre_imagen']
    numero_cuenta = request.form['numero_cuenta']  # Obtener el número de cuenta del formulario
    captu.cocodrilo(nombre_imagen, numero_cuenta)  # Pasar el número de cuenta a la función cocodrilo
    flash('Foto guardada')
    return redirect(url_for('INDEX'))
#//////////////////////////////////////


@app.route('/detect_faces', methods=['GET', 'POST'])
def detect_faces_route():
    extra.pinguino()
    flash('Rostro extraido')
    return redirect(url_for('INDEX'))


@app.route('/recognize_faces', methods=['GET', 'POST'])
def recognize_faces_route():
    numero_cuenta = request.form['numero_cuenta']  # Obtener el número de cuenta del formulario
    recog.ositopanda(numero_cuenta)  # Pasar el número de cuenta a la función ositopanda()
    flash('Reconociendo rostros')
    return redirect(url_for('INDEX'))


#VALIDAMOS QUE SI EJECUTAMOS EL app.py INICIAMOS EL SERVIDOR
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000,threaded=True)
