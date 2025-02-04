import time

from common.python_mqtt.mqtt_client import MQTTClient

robot_ip = "192.168.8.209"

mqtt_client = MQTTClient(robot_ip)


capture_number = 2 # Number of times robot pauses to capture
capture_interval = 15 # Time between captures

def pause_robot():
    while mqtt_client.is_paused() == False:
        mqtt_client.pause()
        time.sleep(1)

def dock_robot():
    while mqtt_client.is_docking() == False:
        mqtt_client.dock()
        time.sleep(1)

def move_robot_off_dock_NO_VAC():
     if mqtt_client.is_docked():
        mqtt_client.clean()
        mqtt_client.set_fan_speed(0)
        time.sleep(15)
        pause_robot()


def basic_photo_run(capture_number: int, capture_interval: int):
    capture_time = 5 # Amount of time robot pauses to capture
    
    mqtt_client.resume()
    
    for i in range(capture_number):
        time.sleep(capture_interval)
        pause_robot()
        time.sleep(capture_time)
        mqtt_client.resume()

basic_photo_run(capture_number,capture_interval)
dock_robot()