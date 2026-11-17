<div align="center">

  <h1>Control Gestual del Sistema</h1>
  <p><strong>Interacción humano-computadora sin contacto mediante visión artificial y seguimiento de 21 puntos clave en tiempo real.</strong></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV" />
    <img src="https://img.shields.io/badge/MediaPipe-0097A7?style=for-the-badge&logo=google&logoColor=white" alt="MediaPipe" />
    <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
    <img src="https://img.shields.io/badge/PyAutoGUI-Automation-2EA44F?style=for-the-badge" alt="PyAutoGUI" />
  </p>

  <p>
    <a href="#-arquitectura-del-flujo"><img src="https://img.shields.io/badge/01_ARQUITECTURA-FF6B00?style=for-the-badge" /></a>
    <a href="#-mapa-de-gestos"><img src="https://img.shields.io/badge/02_MAPA_DE_GESTOS-1E293B?style=for-the-badge" /></a>
    <a href="#-stack-técnico"><img src="https://img.shields.io/badge/03_TECNOLOGÍAS-1E293B?style=for-the-badge" /></a>
    <a href="#-despliegue-local"><img src="https://img.shields.io/badge/04_INSTALACIÓN-FF6B00?style=for-the-badge" /></a>
  </p>

</div>

---

<table>
  <tr>
    <td width="55%" valign="center">
      <h3>🎯 Visión del Proyecto</h3>
      <p>
        Sistema desarrollado en <strong>Python</strong> que transforma la webcam en un sensor de comandos para el sistema operativo. Procesa fotogramas en vivo, detecta la geometría de la mano y ejecuta atajos de teclado tras validar la estabilidad del gesto.
      </p>
      <ul>
        <li>⚡ <strong>Baja latencia:</strong> Procesamiento fluido cuadro a cuadro.</li>
        <li>🛡️ <strong>Anti-falsos positivos:</strong> Validación temporal de 2.0 segundos.</li>
        <li>🦴 <strong>21 Landmarks:</strong> Mapeo anatómico completo de falanges y nudillos.</li>
      </ul>
    </td>
    <td width="45%" align="center">
      <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaG5tZ3F4Y3Z4Y3Z4Y3Z4Y3Z4Y3Z4Y3Z4Y3Z4Y3Z4Y3Z4/L1R1tvI9svkIWwpVYr/giphy.gif" width="100%" alt="AI Vision Isometric" />
    </td>
  </tr>
</table>

---

### ⚙️ 01 Arquitectura del Flujo (Pipeline)

<div align="center">

```mermaid
flowchart LR
    A["01 Captura Webcam<br/>(OpenCV BGR → RGB)"] --> B["02 Inferencia IA<br/>(MediaPipe HandLandmarker)"]
    B --> C["03 Geometría Dedos<br/>(Puntas vs Nudillos)"]
    C --> D["04 Cronómetro<br/>(Estabilidad ≥ 2.0s)"]
    D --> E["05 Ejecución OS<br/>(PyAutoGUI / Subprocess)"]
    
    style A fill:#161b22,stroke:#ff6b00,stroke-width:2px,color:#fff
    style B fill:#161b22,stroke:#38bdf8,stroke-width:2px,color:#
