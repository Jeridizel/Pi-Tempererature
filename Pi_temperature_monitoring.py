#!/usr/bin/env python

import subprocess
import RPi.GPIO as GPIO
import Adafruit_DHT
import pymysql
import time
import sys
import requests
import pathlib
import datetime
import os

# Definirajte parametre zahtjeva
zabbix_server = "ip_zabbix_servera"
host_name = "Pi_monitoring_NORTH"
key = "north.status"


relay_pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)
print("Relay is off")
GPIO.output(relay_pin, GPIO.LOW)


def get_values():
    humidity4, temperature4 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
    temperature4 = round(temperature4, 2)
    json_response = {
        temperature4
    }
    return temperature4

json_response = get_values()
print(json_response)
json_string = str(json_response)

command = ["zabbix_sender", "-z", zabbix_server, "-s", host_name, "-k", key, "-o", json_string]

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the process to complete and capture the output
output, error = process.communicate()

# Print the output and errors if any
print("Output:", output.decode())
print("Error:", error.decode())

counter_path="/dev/shm/counter.txt"

if os.path.isfile(counter_path):
    print('Datoteka već postoji.')
else:
    with open(counter_path, 'w') as file:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f'1\n{current_time}')

if json_response > 27:
    with open(counter_path, 'r') as file:
        lines = file.readlines()
        stored_time = datetime.datetime.strptime(lines[1].strip(), '%Y-%m-%d %H:%M:%S')
        current_time = datetime.datetime.now()
        time_difference = current_time - stored_time
        if time_difference >= datetime.timedelta(hours=3):
            print ("High temperature detected - AC OFF")
            GPIO.output (relay_pin, GPIO.HIGH)

            command = ["zabbix_sender", "-z", zabbix_server, "-s", "Pi_monitoring_NORTH", "-k", "trigger.north", "-o", "1"]
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            time.sleep(60)
            print ("AC BACK ON")
            GPIO.output (relay_pin,GPIO.LOW)
            with open(counter_path, 'w') as file2:
                current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file2.write(f'1\n{current_time}')
