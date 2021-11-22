#-------------------------------------------------------------------------------
# Name:        OpenGL loop
# Purpose:
#
# Author:      Siro
#
# Created:     18.11.2021
# Copyright:   (c) Multiryzz 2020-2021
# Licence:     All rights reserved
#-------------------------------------------------------------------------------

import glfw
import OpenGL.GL.shaders
import numpy
from OpenGL.GL import *
from Objects import Form
#TODO Bugfixing from FixedUpdate import SlowFixedUpdate
import time
import pyrr
import sys

a = 0
b = 0
c = 0
d = 0
RunTime = 0
allow = False
def stableLoop(runTime, precision):
    global a
    global b
    global c
    global d

    try:
        if int(precision) <= 3:
            #TODO: make some fancy function stuff
            print("bb")
        else:
            print("please use an Int, that is smaller then 4...")
            exit()
    except ValueError:
        try:
            int(precision)
        except ValueError:
            print("you need to use an int for precision")
            exit()
    if precision > 3:
        exit()
    #50x per second


    if (((runTime - c) > 0.02) ):
        c = runTime
    # DEBUG ONLY it makes the program super slow because of print
        #print(format((runTime - b), ".2f"))

    #10x per second
    if((runTime - d) > 0.1):
        d = runTime
        #every second


    if((runTime - b) > 1):
        print("1 Second Passed...")
        b = runTime
        num = a/1
        fps = "fps: " + str(num)+ "\n"
        sys.stdout.write(fps)

def main():
    triangle = Form("Triangle", 40, 40, 2, 2)
    print(triangle.name)
    # setting up basic things for glfw
    if not glfw.init():
        return

    window = glfw.create_window(1200, 1200, "OPENGL TEST", None, None)

    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    #button left, buttom left, and then up
            #positions        Colors
    cube = [-0.5, -0.5,  0.5, 0.9, 0.4, 1.0,
             0.5, -0.5,  0.5, 0.9, 1.0, 0.4,
             0.5,  0.5,  0.5, 0.9, 0.4, 0.4,
            -0.5,  0.5,  0.5, 0.9, 0.3, 0.4,

            -0.5, -0.5, -0.5, 1.0, 0.0, 0.0,
             0.5, -0.5, -0.5, 0.5, 1.0, 0.0,
             0.5,  0.5, -0.5, 0.5, 0.0, 0.4,
            -0.5,  0.5, -0.5, 0.1, 0.5, 0.3]

    cube = numpy.array(cube, dtype = numpy.float32)

    indices = [0, 1, 2, 2, 3, 0,
               4, 5, 6, 6, 7, 4,
               4, 5, 1, 1, 0, 4,
               6, 7, 3, 3, 2, 6,
               5, 6, 2, 2, 1, 5,
               7, 4, 0, 0, 3, 7]


    indices = numpy.array(indices , dtype = numpy.uint32)
    vertex_shader = """
    #version 330
    in vec3 position;
    in vec3 color;
    uniform mat4 transform;
    out vec3 newColor;
    void main()
    {
        gl_Position = transform * vec4(position, 1.0f);
        newColor = color;
    }
    """

    fragment_shader = """
    #version 330
    in vec3 newColor;
    out vec4 outColor;
    void main()
    {
        outColor = vec4(newColor, 1.0f);
    }

    """

    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                               OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))
    #vertex buffer object
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, 192, cube, GL_STATIC_DRAW)

    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 144, indices, GL_STATIC_DRAW)

    position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))#this is the byte where the vertex starts
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shader, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))#this is the byte where the color starts
    glEnableVertexAttribArray(color)

    glUseProgram(shader)


    global RunTime
    #main openGL loop
    while not glfw.window_should_close(window):
        glClearColor(255, 255, 000, 1.0)
        glEnable(GL_DEPTH_TEST)
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        rot_x = pyrr.Matrix44.from_x_rotation(0.2 * glfw.get_time())
        rot_y = pyrr.Matrix44.from_y_rotation(0.4 * glfw.get_time())
        stableLoop(glfw.get_time(), 3)
        RunTime = glfw.get_time()
        transfromLoc = glGetUniformLocation(shader, "transform") #goes to the shader program and get transform from it
        glUniformMatrix4fv(transfromLoc, 1, GL_FALSE, rot_x * rot_y)#makes fancy math stuff


        glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_INT, None)
        glfw.swap_buffers(window)


    glfw.terminate()

if __name__ == "__main__":
    main()
