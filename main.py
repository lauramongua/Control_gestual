import cv2
import mediapipe as mp
import numpy as np
import webbrowser
import time
import os
import subprocess
import pyautogui #libreria para usar atajo de teclado

# Importar el nuevo motor de tareas de MediaPipe
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Configurar el detector usando el archivo que acabamos de descargar
options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=VisionRunningMode.VIDEO, # Indicamos que procesaremos un vídeo
    num_hands=1 # Solo buscamos 1 mano
)

# Inicializar la webcam
cap = cv2.VideoCapture(0)

PUNTA_DEDOS = [8, 12, 16, 20]
NUDILLOS_DEDOS = [6, 10, 14, 18]
tiempo_inicio = 0.0
accion_ejecutada = False


# Abrir el detector moderno
with HandLandmarker.create_from_options(options) as landmarker:
    print("Buscando webcam... Presiona 'q' para salir.")
    
    timestamp = 0 # Necesario para el modo vídeo de MediaPipe
    gesto_anterior = "Desconocido"
    

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Error al acceder a la webcam.")
            break
            
        frame = cv2.flip(frame, 1) # Efecto espejo
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Convertir el fotograma al formato especial que pide el nuevo MediaPipe
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
        
        # Incrementar el contador de tiempo del vídeo (milisegundos)
        timestamp += 1
        
        # Procesar la imagen con el nuevo método
        detection_result = landmarker.detect_for_video(mp_image, timestamp)

        # Si el detector encuentra una mano...
        if detection_result.hand_landmarks:
            # Dibujar los puntos "a mano" de forma sencilla para no depender de drawing_utils
            for hand_landmarks in detection_result.hand_landmarks:

                # LOGICA DETECCION DE DEDOS 
                dedos_levantados = 0 # contador de dedos abiertos

                for i in range(4):
                    punta_y = hand_landmarks[PUNTA_DEDOS[i]].y
                    nudillo_y = hand_landmarks[NUDILLOS_DEDOS[i]].y

                    if punta_y < nudillo_y:
                        dedos_levantados += 1
                
                punto_indice = hand_landmarks[8].y
                nudillo_indice = hand_landmarks[6].y

                punta_corazon = hand_landmarks[12].y
                nudillo_corazon = hand_landmarks[10].y

                punta_anular = hand_landmarks[16].y
                nudillo_anular = hand_landmarks[14].y

                punta_menique = hand_landmarks[20].y
                nudillo_menique = hand_landmarks[18].y

                gesto_actual = "Desconocido"

                if dedos_levantados == 0:
                    gesto_actual = "Puno cerrado"
                elif (punto_indice < nudillo_indice) and (punta_corazon < nudillo_corazon) and (punta_menique > nudillo_menique):
                    gesto_actual = "Dos"
                elif dedos_levantados >= 4:
                    gesto_actual = "Mano abierta"     

                                
                # Pinta el gesto en pantalla
                cv2.putText(frame, f"Gesto: {gesto_actual}", (30, 60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

                for landmark in hand_landmarks:
                    # Convertir las coordenadas relativas (0.0 a 1.0) a píxeles de tu pantalla
                    x = int(landmark.x * frame.shape[1])
                    y = int(landmark.y * frame.shape[0])
                    # Dibujar un circulito verde en cada punto de la mano
                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

                # --- CONTROL DE CRONÓMETRO --
                if gesto_actual == gesto_anterior:
                    tiempo_transcurrido = time.time() - tiempo_inicio
                    
                  
                    # Añadimos la condición final para que solo responda al puño cerrado
                    if (tiempo_transcurrido >= 2.0) and (accion_ejecutada == False) and (gesto_actual == "Mano abierta"):
                        subprocess.Popen("start https://www.google.com", shell=True)
                        accion_ejecutada = True
                    elif (tiempo_transcurrido >= 2.0 ) and (accion_ejecutada == False) and (gesto_actual == "Puno cerrado"):
                        pyautogui.hotkey('alt', 'f4')
                        accion_ejecutada = True
                    elif (tiempo_transcurrido >= 2.0) and (accion_ejecutada == False) and (gesto_actual == "Victoria"):
                        pyautogui.hotkey('win', 'd')
                        accion_ejecutada = True
                        
                elif gesto_actual != gesto_anterior:
                    tiempo_inicio = time.time()
                    gesto_anterior = gesto_actual
                    accion_ejecutada = False


        # Mostrar el vídeo en la ventana
        cv2.imshow('Control Gestual - Hito 1 (Moderno)', frame)

        # Si pulso la 'q', rompe el bucle
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

cap.release()
cv2.destroyAllWindows()