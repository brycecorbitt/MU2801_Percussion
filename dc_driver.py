import time
import RPi.GPIO as GPIO          

GPIO.setmode(GPIO.BCM)

class DCDriver(object):
  def __init__(self, en, in1, in2):
    self.en = en
    self.in1 = in1
    self.in2 = in2
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(en, GPIO.OUT)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    self.p=GPIO.PWM(en, 1000)
    self.p.start(0)

  def set_direction(self, value):
    if value:
      GPIO.output(self.in1, GPIO.HIGH)
      GPIO.output(self.in2, GPIO.LOW)
    else:
      GPIO.output(self.in1, GPIO.LOW)
      GPIO.output(self.in2, GPIO.HIGH)

  def set_speed(self, value):
    self.p.ChangeDutyCycle(value)
  
  def stop(self):
    self.p.ChangeDutyCycle(0)

# driver = DCDriver(13, 26, 16)
# driver.set_speed(100)
# time.sleep(2)
# driver.set_direction(0)
# time.sleep(2)

# GPIO.cleanup()
