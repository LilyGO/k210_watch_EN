# Untitled - By: 15840 - 周五 4月 24 2020

import time                 #导入time，使用延时sleep
from Maix import GPIO       #导入模块Maix的GPIO函数，分为通用和高速
from fpioa_manager import * #导入模块fpioa_manager的全部，缩写为fm

fm.register(22,fm.fpioa.GPIO1)    #通用GPIO0已用。故用GPIO1
light=GPIO(GPIO.GPIO1,GPIO.OUT)   #代码默认使用通用GPIO1进行控制

#fm.register(22,fm.fpioa.GPIOHS0) #高速GPIOHS0可用。故用GPIOHS0
#light=GPIO(GPIO.GPIOHS0,GPIO.OUT)#当使用高速IO时，要注释掉通用IO的代码

while True:                 #while无限循环
    light.value(0)                #设置LED低电平 灯亮
    time.sleep_ms(1000)           #延时1s
    light.value(1)                #设置LED高电平 灯灭
    time.sleep_ms(1000)           #延时1s
