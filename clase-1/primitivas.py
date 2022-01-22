#Importar librerías

from turtle import width
from OpenGL.GL import *
from glew_wish import *
import glfw

def draw():
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
        draw()

        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()

