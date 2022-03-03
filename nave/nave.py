from OpenGL.GL import *
from glew_wish import *
import glfw

class Nave:
    posicion_x = 0.0
    posicion_y = 0.0
    posicion_z = 0.0
    velocidad = 0.5
    angulo = 0.0
    fase = 90.0
    velocidad_rotacion = 90.0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y,0.0)
        glRotatef(self.angulo, 0.0, 0.0, 1.0)
        glBegin(GL_TRIANGLES)

        #Establecer color
        glColor3f(1,0,0)

        #Manda vertices a dibujar
        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0.0,0.05,0)
        glVertex3f(0.05,-0.05,0)

        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(-0.05, -0.05, 0)
        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05, 0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glEnd()

        glPopMatrix()