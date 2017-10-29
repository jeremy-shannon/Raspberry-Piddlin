import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.OUT)

light_on = False

while True:
  input_state = GPIO.input(26)
  if input_state == False:
    GPIO.output(18,GPIO.HIGH)
    if light_on == False:
      print("light on")
      light_on = True
  else:
    GPIO.output(18,GPIO.LOW)
    if light_on == True:
      print("light off")
      light_on = False
