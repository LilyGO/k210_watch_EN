#2.T-Watch_Demo.py T-Watch_K210示例程序

import lcd                  #导入LCD屏幕库
import time                 #导入time时间库
import sensor               #导入sensor摄像头传感库
from Maix import GPIO       #导入模块Maix的GPIO函数，分为通用和高速
from fpioa_manager import * #导入模块fpioa_manager的全部，缩写为fm

#开启屏幕背光，可参考开启LED灯1.LED.py 原理相同
fm.register(board_info.PIN17,fm.fpioa.GPIO0)
led=GPIO(GPIO.GPIO0,GPIO.OUT)
led.value(1)                #1:开启背光 0:关闭背光

lcd.init(freq=15000000)     #LCD屏幕初始化 运行频率15M
lcd.rotation(2)             #LCD旋转模式设置 2:向上 0:向下 1:向左 0:向右

sensor.reset()              #摄像头重置初始化
sensor.set_pixformat(sensor.RGB565) #摄像头图像格式RGB565 16位/像素
sensor.set_framesize(sensor.QVGA)   #摄像头图像帧大小QVGA
sensor.skip_frames(time=2000)       #摄像头跳帧时间2秒 使图像稳定传输到屏幕

while(True):                #while无限循环执行
    img = sensor.snapshot()         #摄像头获取图像数据赋值给变量img(image)
    lcd.display(img)                #LCD屏幕逐帧显示摄像头img图像
