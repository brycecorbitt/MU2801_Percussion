from bottle import route, get, post, run, request, redirect
from percussion import PercussionMotor

drum = PercussionMotor(0, 13, 26, 16)

@get('/')
def index():
  return '''<h1> MU2801 Percussion Controller </h1>
          <form action="/" method="post">
            Set Sensor Threshold between 0-65535 (Default is 255, higher = less sensitive) <input name="sensor" type="text" />
            <input value="Submit" type="submit" />
        </form>
        <a href="/hit">Click to execute motor hit()</a>
        '''

@get('/hit')
def execute():
  drum.hit()
  redirect('/')

@post('/')
def process():
  if request.forms.get('sensor'):
    try:
      value = int(request.forms.get('sensor'))
      drum.set_sensor_thresh(value)
    except ValueError:
      pass
  redirect('/')


run(host='percussion.dyn.wpi.edu', port=8080)
