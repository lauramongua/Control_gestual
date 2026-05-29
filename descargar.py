import urllib.request
import os

url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
destino = "hand_landmarker.task"

print("Descargando el modelo de IA de Google (puede tardar unos segundos)...")
urllib.request.urlretrieve(url, destino)
print(f"¡Hecho! Archivo guardado correctamente en: {os.path.abspath(destino)}")