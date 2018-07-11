
import RPi as RPi
GPIO = RPi.GPIO
from flask import Flask

GPIO.setmode(GPIO.BOARD) # now use the fake GPIO
GPIO.setup([11,13,15], GPIO.OUT, initial=GPIO.LOW)


app = Flask(__name__)

@app.route('/<string:upc>', methods=['GET'])
def process(upc):
  if upc == 'T1':
    blink(11)
    return 'white'
  if upc == 'T2':
    blink(13)
    return 'green'
  if upc == 'T3':
    blink(15)
    return 'blue'
  return 'FAIL'

def blink(id):
    GPIO.output(id, GPIO.HIGH)

app.run(debug=True)
