import sys
import vrep
import numpy as np
import time

import platform
import struct
import ctypes as ct
from vrepConst import *

libsimx = ct.CDLL("./remoteApi.dll")
vrep.simxFinish(-1) #Terminar todas las conexiones
clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5)

if clientID!=-1:
    print ('Conexion establecida')
 
else:
    sys.exit("Error: no se puede conectar") #Terminar este script


    

#Guardar la referencia de los motores
_, left_motor_handle_tracer=vrep.simxGetObjectHandle(clientID, 'DynamicLeftJoint', vrep.simx_opmode_oneshot_wait)
_, right_motor_handle_tracer=vrep.simxGetObjectHandle(clientID, 'DynamicRightJoint', vrep.simx_opmode_oneshot_wait)
 

#Guardar la referencia de los sensores
_, LeftSensor = vrep.simxGetObjectHandle(clientID, 'LeftSensor', vrep.simx_opmode_oneshot_wait)
_, MiddleSensor = vrep.simxGetObjectHandle(clientID, 'MiddleSensor', vrep.simx_opmode_oneshot_wait)
_, RightSensor = vrep.simxGetObjectHandle(clientID, 'RightSensor', vrep.simx_opmode_oneshot_wait)
