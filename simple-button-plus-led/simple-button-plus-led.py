import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.OUT)

while True:
  input_state = GPIO.input(26)
  if input_state == False:
    print('Button Pressed')
    time.sleep(0.2)
    print "LED on"
    GPIO.output(18,GPIO.HIGH)
  else:
    print "LED off"
    GPIO.output(18,GPIO.LOW)