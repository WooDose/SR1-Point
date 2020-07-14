# SR1-Point
Create a point in a BMP file using OpenGL funcction names,

Puntos:
* (05 puntos) Deben crear una función glInit() que inicialice cualquier objeto interno que requiera su software renderer:
  * Creada, pero no hace nada.
* (05 puntos) Deben crear una función glCreateWindow(width, height) que inicialice su framebuffer con un tamaño (la imagen resultante va a ser de este tamaño:
  * Creada
* (10 puntos)  Deben crear una función glViewPort(x, y, width, height) que defina el área de la imagen sobre la que se va a poder dibujar:
  * Creada. Tiene un tremendo chapus para evitar que de problema cuando se utiliza 1,1 en gl_vertex.
  ```python
  #Este es el chapus
  xW = (xW - 1) if xW == self.width else xW
  yW = (yW - 1) if yW == self.height else yW
  ```
* (20 puntos) Deben crear una función glClear() que llene el mapa de bits con un solo color:
  * Creada, pero no la uso aun.
* (10 puntos) Deben crear una función glClearColor(r, g, b) con la que se pueda cambiar el color con el que funciona glClear(). Los parámetros deben ser números en el rango de 0 a 1.:
  * Creada, pero no entendi la parte de que el color debe ser entre 0 y 1. Lo preguntare en la clase de mañana. Lo que hice fue multiplicar el valor del parametro por 255 al pasarlo a la funcion Color

* (30 puntos) Deben crear una función glVertex(x, y) que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron con glViewPort.:
  * Creada, el chapus de arriba se relaciona a este.

* (15 puntos) Deben crear una función glColor(r, g, b) con la que se pueda cambiar el color con el que funciona glVertex(). Los parámetros deben ser números en el rango de 0 a 1.:
  * Creada, pero tiene la misma observacion que glClearColor
  
* (05 puntos) Deben crear una función glFinish() que escriba el archivo de imagen:
  * Creada, pero aun no tiene padding para non-4multiples
