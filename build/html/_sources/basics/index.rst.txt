******************
Basic
******************

1. MaixPy IDE
==================

.. figure:: ../_static/zza.png
   :scale: 90
   :align: center

1.1 Download IDE
~~~~~~~~~~~~~~~~~~~~~
:download:`MaixPy IDE <../download/maixpy-ide-windows-0.2.5.exe>`

1.2 Steps：
~~~~~~~~~~~~~~~~~
Open the IDE and select the model of the development board in the upper toolbar.

.. figure:: ../_static/ide.jpg
   :scale: 100
   :align: center

* 选择 **工具(Tool)** -> 
* 鼠标 **选择开发板(Select board)** -> 
* 点击 **T-Watch**

2.The first program:Blink the LED
=====================================

.. code-block:: python

    import time                                 #import time, use delay sleep
    from Maix import GPIO                       #import the GPIO function of Maix module, divided into general and high-speed
    from fpioa_manager import *                 #import all of the module fpioa_manager, abbreviated as fm

    fm.register(22,fm.fpioa.GPIO1)              #general GPIO0 has been used. So use GPIO1
    light=GPIO(GPIO.GPIO1,GPIO.OUT)             #the code uses general GPIO1 for control by default

    #fm.register(22,fm.fpioa.GPIOHS0)           #high-speed GPIOHS0 is available. So use GPIOHS0
    #light=GPIO(GPIO.GPIOHS0,GPIO.OUT)          #when using high-speed IO, comment out the general IO code

    while True:                                 #while infinite loop
        light.value(0)                          #set the low level of the LED to light up
        time.sleep_ms(1000)                     #delay 1s
        light.value(1)                          #set the LED high level, the light is off
        time.sleep_ms(1000)                     #delay 1s
   
2.1 Download the firmware:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* :download:`LED.py <../download/LED.py>`

3. T-Watch Example
=====================
.. code-block:: python

    import lcd                                  #import LCD screen library
    import time                                 #import time time library
    import sensor                               #import sensor camera sensor library
    from Maix import GPIO                       #import the GPIO function of Maix module, divided into general and high-speed
    from fpioa_manager import *                 #import all of the module fpioa_manager, abbreviated as fm

    #Turn on the screen backlight, please refer to turning on the LED light 1. The principle of LED.py is the same
    fm.register(board_info.PIN17,fm.fpioa.GPIO0)
    led=GPIO(GPIO.GPIO0,GPIO.OUT)
    led.value(1)                                #1: Turn on the backlight 0: Turn off the backlight

    lcd.init(freq=15000000)                     #LCD screen initialization operating frequency 15M
    lcd.rotation(2)                             #LCD rotation mode setting 2: up 0: down 1: left 0: right

    sensor.reset()                              #camera reset initialization
    sensor.set_pixformat(sensor.RGB565)         #camera image format RGB565 16 bits/pixel
    sensor.set_framesize(sensor.QVGA)           #camera image frame size QVGA
    sensor.skip_frames(time=2000)               #the frame skipping time of the camera is 2 seconds so that the image is transmitted to the screen stably

    while(True): #while infinite loop execution
        img = sensor.snapshot()                 #The camera gets the image data and assigns it to the variable img(image)
        lcd.display(img)                        #LCD screen displays camera img image frame by frame

3.1 Download firmware：
~~~~~~~~~~~~~~~~~~~~~~~

* :download:`T-Watch_Demo.py <../download/T-Watch_Demo.py>`

