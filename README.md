# 🚀 Iron Man en el Espacio

Un emocionante juego de acción desarrollado en Python usando Pygame, donde controlas a Iron Man defendiendo el espacio de enemigos alienígenas.

## 📋 Descripción

Iron Man en el Espacio es un juego de disparos en 2D donde el jugador controla a Iron Man y debe destruir enemigos que aparecen desde arriba de la pantalla. El objetivo es obtener la mayor puntuación posible antes de que los enemigos lleguen al suelo.

## ✨ Características

- **🎮 Controles intuitivos**: Movimiento con flechas izquierda/derecha y disparo con espacio
- **🎵 Audio inmersivo**: Música de fondo y efectos de sonido para disparos y explosiones
- **⏸️ Sistema de pausa**: Pausa el juego en cualquier momento con un clic
- **📊 Sistema de puntuación**: Rastrea tu puntuación en tiempo real
- **🎨 Gráficos atractivos**: Sprites personalizados para Iron Man, enemigos y proyectiles
- **💥 Efectos de colisión**: Detección precisa de colisiones entre balas y enemigos

## 🛠️ Requisitos del Sistema

- Python 3.6 o superior
- Pygame 2.0 o superior

## 📦 Instalación

1. **Clona o descarga el proyecto**:
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd GAME_IRON-MAN
   ```

2. **Instala Pygame**:
   ```bash
   pip install pygame
   ```

3. **Asegúrate de tener todos los archivos de recursos**:
   - `jugador.png` - Sprite de Iron Man
   - `enemigo.png` - Sprite de los enemigos
   - `bala.png` - Sprite de los proyectiles
   - `fondo.png` - Imagen de fondo del espacio
   - `icono.ico` - Icono del juego
   - `musica_fondo.wav` - Música de fondo
   - `disparo.wav` - Efecto de sonido para disparos
   - `explosion.wav` - Efecto de sonido para explosiones

## 🎮 Cómo Jugar

1. **Ejecuta el juego**:
   ```bash
   python juego.py
   ```

2. **Controles**:
   - **Flecha Izquierda** ← : Mover Iron Man hacia la izquierda
   - **Flecha Derecha** → : Mover Iron Man hacia la derecha
   - **Espacio** : Disparar proyectiles
   - **Clic en botón de pausa** : Pausar/reanudar el juego

3. **Objetivo**:
   - Destruye los enemigos antes de que lleguen al suelo
   - Cada enemigo destruido suma 1 punto a tu puntuación
   - Si un enemigo llega al suelo, el juego termina

## 🎯 Mecánicas del Juego

- **Movimiento del jugador**: Iron Man se mueve horizontalmente por la parte inferior de la pantalla
- **Sistema de disparos**: Dispara proyectiles hacia arriba para destruir enemigos
- **IA de enemigos**: Los enemigos se mueven de lado a lado y descienden gradualmente
- **Detección de colisiones**: Sistema preciso de colisiones entre balas y enemigos
- **Sistema de vidas**: El juego termina cuando un enemigo llega al suelo

## 📁 Estructura del Proyecto

```
GAME_IRON-MAN/
├── juego.py              # Archivo principal del juego
├── jugador.png           # Sprite de Iron Man (64x64)
├── enemigo.png           # Sprite de enemigos (70x70)
├── bala.png              # Sprite de proyectiles (32x32)
├── fondo.png             # Imagen de fondo del espacio
├── icono.ico             # Icono del juego
├── musica_fondo.wav      # Música de fondo
├── disparo.wav           # Efecto de sonido de disparo
├── explosion.wav         # Efecto de sonido de explosión
└── README.md             # Este archivo
```

## 🔧 Personalización

Puedes modificar fácilmente varios aspectos del juego editando las variables en `juego.py`:

- **Número de enemigos**: Cambia `num_de_enemigos` (línea 36)
- **Velocidad de movimiento**: Modifica `jugadorX_cambio` y `enemigoX_cambio`
- **Velocidad de balas**: Ajusta `balaY_cambio` (línea 48)
- **Tamaño de pantalla**: Modifica las dimensiones en `pygame.display.set_mode()` (línea 10)

## 🐛 Solución de Problemas

### Error: "No module named 'pygame'"
```bash
pip install pygame
```

### Error: "No such file or directory" para archivos de imagen/sonido
- Asegúrate de que todos los archivos de recursos estén en la misma carpeta que `juego.py`
- Verifica que los nombres de archivo coincidan exactamente

### El juego no reproduce sonido
- Verifica que los archivos `.wav` estén presentes
- Asegúrate de que tu sistema tenga audio habilitado

## 🎨 Créditos

- **Desarrollado por**: [Tu Nombre]
- **Motor de juego**: Pygame
- **Inspiración**: Iron Man de Marvel Comics

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el juego:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📞 Contacto

Si tienes preguntas o sugerencias, no dudes en contactarme.

---

¡Disfruta defendiendo el espacio con Iron Man! 🚀✨
