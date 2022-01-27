#Importar librerías

from turtle import width
from OpenGL.GL import *
from glew_wish import *
import glfw

def draw_triangles():
    glBegin(GL_TRIANGLES)

    #Establecer color
    glColor3f(1,0,0)

    #Manda vertices a dibujar
    glVertex3f(-1,0,0)
    glVertex3f(0,1,0)
    glVertex3f(1,0,0)

    glColor3f(0,0,1)
    glVertex3f(-1,0,0)
    glVertex3f(0,-1,0)
    glVertex3f(1,0,0)

    glEnd()

def draw_point():
    glBegin(GL_POINTS)
    glColor3f(1.0,1.0,1.0)
    glVertex(0,0,0)
    glColor3f(1.0,1.0,1.0)
    glVertex(-0.5,-0.5,0)
    glEnd()

def draw_lines():
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    glVertex3f(0.2,-0.8,0.0)
    glVertex3f(0.8,-0.4,0.0)
    glEnd()

def draw_line_strip():
    glBegin(GL_LINE_STRIP)
    glColor3f(0.5,0.5,0.0)
    glVertex3f(0.7,-0.5,0.0)
    glVertex3f(0.9,-0.5,0.0)
    glVertex3f(0.7,-0.7,0.0)
    glVertex3f(0.9,-0.7,0.0)
    glEnd()

def draw_line_loop():
    glBegin(GL_LINE_LOOP)
    glColor3f(0.7,0.0,0.7)
    glVertex3f(-0.6,0.5,0.0)
    glVertex3f(-0.9,0.3,0.0)
    glVertex3f(-0.7,0.6,0.0)
    glEnd()

def draw_triangle_strip():
    glBegin(GL_TRIANGLE_STRIP)

    glColor3f(0.7,0.0,0.7)
    glVertex3f(-0.2,-0.8,0.0)

    glColor3f(0.6,0.6,0.0)
    glVertex3f(-0.6,-0.7,0.0)

    glColor3f(0.5,0.4,0.9)
    glVertex3f(-0.75,-0.3,0.0)

    glColor3f(0.0,0.7,0.7)
    glVertex3f(-0.9,-0.9,0.0)
    glEnd()

def draw_quads():
    glBegin(GL_QUADS)
    glColor3f(0.0,0.4,0.7)
    glVertex3f(-0.2,-0.2,0.0)
    glColor3f(0.5,0.4,0.9)
    glVertex3f(0.2,0.2,0.0)
    glColor3f(1.0,1.0,1.0)
    glVertex3f(0.2,-0.2,0.0)
    glColor3f(0.0,0.4,0.7)
    glVertex3f(-0.2,0.2,0.0)
    glEnd()

def draw_polygon():
    glBegin(GL_POLYGON)
    glColor3f(0.0,0.4,0.7)
    glVertex3f(0.0,0.0,0.0)
    glColor3f(0.14,0.4,0.9)
    glVertex3f(0.0,-0.4,0.0)
    glColor3f(1.0,1.0,1.0)
    glVertex3f(0.3,-0.4,0.0)
    glColor3f(0.0,0.4,0.7)
    glVertex3f(0.3,0.4,0.0)
    glColor3f(0.0,-0.4,0.7)
    glVertex3f(-0.3,0.1,0.0)
    glEnd()

def main():
    width = 800
    height = 600
    #Inicializar GLFW
    if not glfw.init():
        return
    
    #Declarar una ventana 
    window = glfw.create_window(width, height, "Mi ventana", None, None)

    #Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    if not window:
        glfw.terminate()
        return

    #Establecer el contexto
    glfw.make_context_current(window)

    #Le dice a GLEW que si usaremos el GPU
    glewExpermental = True

    #Inicializar el glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Imprimir version
    version = glGetString(GL_VERSION)
    print(version)

    #Draw loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        # glViewport(0,0,width,height)
        #Establecer color de borrado
        glClearColor(0.5,0.5,0.5,0.5)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        #Dibujar
        # draw_triangles()
        # draw_point()
        # draw_lines()
        # draw_line_strip()
        # draw_line_loop()
        # draw_triangle_strip()
        # draw_quads()
        draw_polygon()

        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()

