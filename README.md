<div align="center">
  
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Raised%20Hand.png" alt="Hand Tracking" width="90" height="90" />

  <h1>Control Gestual del Sistema</h1>
  <p><strong>Interacción humano-computadora sin contacto mediante visión artificial y seguimiento de 21 puntos clave en tiempo real.</strong></p>

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
    style B fill:#161b22,stroke:#38bdf8,stroke-width:2px,color:#fff
    style C fill:#161b22,stroke:#a855f7,stroke-width:2px,color:#fff
    style D fill:#161b22,stroke:#38bdf8,stroke-width:2px,color:#fff
    style E fill:#ff6b00,stroke:#fff,stroke-width:2px,color:#fff
