import lcd                  #导入LCD屏幕库
import image                #导入Image图像库
from Maix import GPIO       #导入模块Maix的GPIO函数，分为通用和高速
from fpioa_manager import * #导入模块fpioa_manager的全部，缩写为fm

#开启屏幕背光，可参考开启LED灯1.LED.py 原理相同
fm.register(board_info.PIN17,fm.fpioa.GPIO0)
led=GPIO(GPIO.GPIO0,GPIO.OUT)
led.value(1)                #1:开启背光 0:关闭背光

lcd.init(freq=15000000)     #LCD屏幕初始化 运行频率15M
lcd.rotation(2)             #LCD旋转模式设置 2:向上 0:向下 1:向左 0:向右


img = image.Image("/flash/image.jpg")                   #读取image.jpg图像数据
lcd.display(img)                                        #显示image

lcd.draw_string(20, 140, "Hello", lcd.RED, lcd.WHITE)   #在X坐标20，Y坐标140的位置显示文本Hello
lcd.draw_string(20, 160, "T-Watch" , lcd.RED, lcd.WHITE)#在X坐标20，Y坐标160的位置显示文本T-Watch
