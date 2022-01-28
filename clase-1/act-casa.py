from turtle import width
from OpenGL.GL import *
from glew_wish import *
import glfw
import math

def draw_nubes():
    #A-1
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)

    for angulo in range(0,359,5):
        glVertex3f(0.1 * math.cos(angulo * math.pi / 180) - 0.07, 0.05 * math.sin(angulo * math.pi / 180) + 0.75, 0)
    
    glEnd()
    
    #A-2
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)

    for angulo in range(0,359,5):
        glVertex3f(0.15 * math.cos(angulo * math.pi / 180) - 0.2, 0.08 * math.sin(angulo * math.pi / 180) + 0.68, 0)

    glEnd()

    #B-1
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)

    for angulo in range(0,359,5):
        glVertex3f(0.1 * math.cos(angulo * math.pi / 180) + 0.45, 0.05 * math.sin(angulo * math.pi / 180) + 0.35, 0)
    
    glEnd()
    
    #B-2
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)

    for angulo in range(0,359,5):
        glVertex3f(0.15 * math.cos(angulo * math.pi / 180) + 0.6, 0.08 * math.sin(angulo * math.pi / 180) + 0.3, 0)

    glEnd()

    #C-1
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)

    for angulo in range(0,359,5):
        glVertex3f(0.1 * math.cos(angulo * math.pi / 180) + 0.85, 0.05 * math.sin(angulo * math.pi / 180) + 0.68, 0)
    
    glEnd()
    
    #C-2
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)

    for angulo in range(0,359,5):
        glVertex3f(0.15 * math.cos(angulo * math.pi / 180) + 0.9, 0.08 * math.sin(angulo * math.pi / 180) + 0.6, 0)

    glEnd()

#--------------------------------------------------------------

def darw_sol():
    glBegin(GL_LINES)
    glColor3f(1,1,0)

    glVertex3f(-0.45,0.9,0)
    glVertex3f(-0.65,0.8,0)

    glVertex3f(-0.75,1,0)
    glVertex3f(-0.75,0.9,0)

    glVertex3f(-0.45,0.45,0)
    glVertex3f(-0.65,0.6,0)

    glVertex3f(-0.7,0.25,0)
    glVertex3f(-0.75,0.5,0)

    glVertex3f(-0.88,0.58,0)
    glVertex3f(-0.99,0.45,0)

    glVertex3f(-0.88,0.8,0)
    glVertex3f(-0.99,0.9,0)

    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 0)

    for angulo in range(0,359,5):
        glVertex3f(0.1 * math.cos(angulo * math.pi / 180) - 0.75, 0.125 * math.sin(angulo * math.pi / 180) + 0.7, 0)

    glEnd()

#--------------------------------------------------------------

def draw_casa():
    glBegin(GL_QUADS)
    glColor3f(0.8,0.75,0.66)
    glVertex3f(-0.2,0.1,0)
    glVertex3f(0.5,0.1,0)
    glVertex3f(0.5,-0.6,0)
    glVertex3f(-0.2,-0.6,0)
    glEnd()

#--------------------------------------------------------------

def draw_puerta():
    glBegin(GL_QUADS)
    glColor3f(0.39,0.26,0.12)
    glVertex3f(-0.07,-0.25,0)
    glVertex3f(0.1,-0.25,0)
    glVertex3f(0.1,-0.6,0)
    glVertex3f(-0.07,-0.6,0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0, 1)

    for angulo in range(0,359,5):
        glVertex3f(0.01 * math.cos(angulo * math.pi / 180) + 0.058, 0.013 * math.sin(angulo * math.pi / 180) - 0.43, 0)

    glEnd()

#--------------------------------------------------------------

def darw_techo():
    glBegin(GL_TRIANGLES)
    glColor3f(0.3,0,0)
    glVertex3f(-0.3,0.1,0)
    glVertex3f(0.6,0.1,0)
    glVertex3f(0.13,0.5,0)
    glEnd()

#--------------------------------------------------------------

def draw_ventana():
    glBegin(GL_QUADS)
    glColor3f(0.8,0.95,0.6)
    glVertex3f(0.45,-0.35,0)
    glVertex3f(0.15,-0.35,0)
    glVertex3f(0.15,-0.05,0)
    glVertex3f(0.45,-0.05,0)
    glEnd()
    
    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex3f(0.45,-0.2,0)
    glVertex3f(0.15,-0.2,0)
    glVertex3f(0.3,-0.35,0)
    glVertex3f(0.3,-0.05,0)
    glEnd()

#--------------------------------------------------------------

def draw_arbol():
    glBegin(GL_POLYGON)
    glColor3f(0.55,0.30,0.13)
    glVertex3f(-0.7,-0.1,0)
    glVertex3f(-0.6,-0.1,0)
    glVertex3f(-0.6,-0.6,0)
    glVertex3f(-0.7,-0.6,0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0,0.7,0.3)
    for angulo in range(0,359,5):
        glVertex3f(0.2 * math.cos(angulo * math.pi / 180) - 0.65, 0.25 * math.sin(angulo * math.pi / 180) + 0.2, 0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0,0.7,0.3)
    for angulo in range(0,359,5):
        glVertex3f(0.2 * math.cos(angulo * math.pi / 180) - 0.65, 0.25 * math.sin(angulo * math.pi / 180) + -0.05, 0)
    glEnd()

#--------------------------------------------------------------

def draw_pasto():
    glBegin(GL_QUADS)
    glColor3f(0.2,0.4,0)
    glVertex3f(-1,-1,0)
    glVertex3f(1,-1,0)
    glVertex3f(1,-0.6,0)
    glVertex3f(-1,-0.6,0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.5,0.7,0)
    glVertex3f(-0.83,-0.8,0)
    glVertex3f(-0.8,-0.73,0)
    glVertex3f(-0.83,-0.8,0)
    glVertex3f(-0.85,-0.73,0)

    glVertex3f(-0.4,-0.9,0)
    glVertex3f(-0.45,-0.84,0)
    glVertex3f(-0.4,-0.9,0)
    glVertex3f(-0.38,-0.84,0)

    glVertex3f(-0.2,-0.8,0)
    glVertex3f(-0.25,-0.71,0)
    glVertex3f(-0.2,-0.8,0)
    glVertex3f(-0.2,-0.71,0)

    glVertex3f(0.3,-0.9,0)
    glVertex3f(0.35,-0.8,0)
    glVertex3f(0.3,-0.9,0)
    glVertex3f(0.3,-0.8,0)

    glVertex3f(0.85,-0.8,0)
    glVertex3f(0.8,-0.72,0)
    glVertex3f(0.85,-0.8,0)
    glVertex3f(0.75,-0.72,0)
    glEnd()

#--------------------------------------------------------------

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
        glClearColor(0.1,0.8,0.9,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        #Dibujar
        draw_nubes()
        draw_casa()
        darw_techo()
        draw_puerta()
        draw_ventana()
        draw_arbol()
        draw_pasto()
        darw_sol()

        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()

