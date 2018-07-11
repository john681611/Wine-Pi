
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
  if upc == 'T1':
    threading.Thread(target=blink, kwargs={'pin': 11}).start()
    return 'white'
  if upc == 'T2':
    threading.Thread(target=blink, kwargs={'pin': 13}).start()
    return 'green'
  if upc == 'T3':
    threading.Thread(target=blink, kwargs={'pin': 15}).start()
    return 'blue'
  return 'FAIL'

def blink(pin):
  for _ in range(30):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)

app.run(debug=True)
