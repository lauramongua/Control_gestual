# Control Gestual del Sistema 🖐️💻

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?style=for-the-badge&logo=google&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-Automation-2EA44F?style=for-the-badge)

Aplicación de **visión artificial** desarrollada en **Python** que permite controlar acciones y atajos del sistema operativo utilizando únicamente gestos de la mano captados a través de la webcam en tiempo real.

---

### ✨ Características Principales

* **🦴 Detección de 21 puntos clave (Landmarks):** Utiliza el motor moderno `HandLandmarker` de **MediaPipe** en modo vídeo para rastrear con precisión las articulaciones de la mano y dibujar el esqueleto en pantalla.
* **⏱️ Sistema anti-falsos positivos (Temporizador de 2 segundos):** Incorpora un control de tiempo que exige mantener el mismo gesto de forma estable durante **2.0 segundos** antes de disparar la acción, evitando ejecuciones accidentales al mover la mano.
* **🪞 Procesamiento fluido con efecto espejo:** Captura de vídeo en tiempo real con **OpenCV**, inversión horizontal intuitiva y visualización en pantalla del gesto detectado.

---

### 🕹️ Mapa de Gestos y Acciones

| Gesto Detectado | Condición Anatómica | Tiempo | Acción Ejecutada |
| :--- | :--- | :---: | :--- |
| 🖐️ **Mano abierta** | 4 o más dedos extendidos | `2.0 seg` | Abre el navegador web en **Google** |
| ✊ **Puño cerrado** | 0 dedos extendidos | `2.0 seg` | Cierra la ventana activa (`Alt + F4`) |
| ✌️ **Dos / Victoria** | Índice y corazón levantados | `2.0 seg` | Minimiza todo y muestra el escritorio (`Win + D`) |

---

### 🛠️ Tecnologías Utilizadas

* **[OpenCV (`cv2`)](https://opencv.org/):** Captura de fotogramas desde la webcam, transformación de color (`BGR` a `RGB`) y renderizado visual de puntos y texto.
* **[MediaPipe Tasks Vision](https://developers.google.com/mediapipe):** Inferencia del modelo de seguimiento de manos (`hand_landmarker.task`).
* **[PyAutoGUI](https://pyautogui.readthedocs.io/):** Automatización de atajos de teclado del sistema operativo.
* **Subprocess & Time:** Ejecución de comandos del sistema y gestión del cronómetro de confirmación.

---

### 🚀 Instalación y Uso

#### 1. Clonar el repositorio e instalar dependencias
```bash
git clone [https://github.com/lauramongua/Control-gestual.git](https://github.com/lauramongua/Control-gestual.git)
cd Control-gestual
pip install opencv-python mediapipe numpy pyautogui
