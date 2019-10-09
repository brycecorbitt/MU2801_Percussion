import time
from adc import ADC
from dc_driver import DCDriver

class PercussionMotor(object):
  delay_time = .12
  def __init__(self, analog_channel, en, in1, in2):
    self.sensor = ADC.add_channel(analog_channel)
    self.driver = DCDriver(en, in1, in2)
    self.driver.set_direction(0)
    self.sensor_thresh = 255


  def set_sensor_thresh(self, value):
    self.sensor_thresh = value
  
  def hit(self):
    self.driver.set_direction(0)
    self.driver.set_speed(100)
    start_time = time.time()
    while self.sensor.value <= self.sensor_thresh:
      time.sleep(.0001)
      if time.time() - start_time > 10:
        self.driver.set_speed(0)
        return
    elapsed_time = time.time() - start_time
    self.driver.set_direction(1)
    if(elapsed_time > PercussionMotor.delay_time):
      elapsed_time -= PercussionMotor.delay_time
    else:
      elapsed_time = PercussionMotor.delay_time
    time.sleep(elapsed_time)
    self.driver.set_speed(0)


    


