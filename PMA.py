import numpy as np
import math

def MAPT(speed, heading, wind_direction, wind_speed, current_direction, current_speed):
    speed = np.array(speed)
    heading = np.deg2rad(heading)
    wind_direction = np.deg2rad(wind_direction)
    current_direction = np.deg2rad(current_direction)
    
    wind_effect = wind_speed * np.array([np.cos(wind_direction), np.sin(wind_direction)])
    current_effect = current_speed * np.array([np.cos(current_direction), np.sin(current_direction)])
    total_effect = wind_effect + current_effect
    
    speed_x = speed * np.cos(heading)
    speed_y = speed * np.sin(heading)
    total_speed_x = speed_x + total_effect[0]
    total_speed_y = speed_y + total_effect[1]
    
    MAPT = speed * speed / np.sqrt(total_speed_x**2 + total_speed_y**2)
    MAPT_heading = np.arctan2(total_speed_y, total_speed_x)
    MAPT_heading = np.rad2deg(MAPT_heading)
    MAPT_heading = (MAPT_heading + 360) % 360
    return MAPT, MAPT_heading

# Ejemplo de uso:
"""speed = 10 # knots
heading = 90 # grados
wind_direction = 30 # grados
wind_speed = 5 # knots
current_direction = 120 # grados
current_speed = 2 # knots"""

MAPT, MAPT_heading = MAPT(speed, heading, wind_direction, wind_speed, current_direction, current_speed)
print("El punto máximo de aproximación es:", MAPT, "knots a un rumbo de", MAPT_heading, "grados")
# Tenga en cuenta que este es un ejemplo simplificado y que puede ser necesario ajustarlo en función de sus necesidades específicas. 
# Además, es importante tener en cuenta que el cálculo del MAPT es una tarea compleja que requiere una comprensión profunda de la navegación marítima 
# y los factores que influyen en la ruta de una embarcación. Por lo tanto, es recomendable consultar con un profesional capacitado antes de utilizar 
# cualquier cálculo para la planificación de rutas




