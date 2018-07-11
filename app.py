
try:
  import RPi.GPIO as GPIO
except:
  print("fallingback")
  import RPi as RPi
  GPIO = RPi.GPIO

from flask import Flask

import threading
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup([11,13,15], GPIO.OUT, initial=GPIO.LOW)


app = Flask(__name__)

@app.route('/<string:upc>', methods=['GET'])
def process(upc):
  if upc == '00332408':
    threading.Thread(target=blink, kwargs={'pin': 11}).start()
    return 'white'
  if upc == '00537377':
    threading.Thread(target=blink, kwargs={'pin': 13}).start()
    return 'blue'
  if upc == '00490344':
    threading.Thread(target=blink, kwargs={'pin': 15}).start()
    return 'green'
  return 'FAIL'

def blink(pin):
  for _ in range(5):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)

app.run(debug=True)
