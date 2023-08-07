from pyb import delay, Pin, ADC, Timer, UART, LED, udelay
from ophyra_tftdisp import ST7735
import re

tft = ST7735()
tft.init()
tft.backlight(1)

uart = UART(3, 9600)
uart.init(9600, bits=8, parity=None, stop=1)

lf_value = ""
ls_value = ""
lt_value = ""
last = ""
bg = tft.rgbcolor(0, 0, 0)
fg = tft.rgbcolor(255, 255, 255)
gr = tft.rgbcolor(0, 255, 0)
bl = tft.rgbcolor(150, 150, 255)
textos = ["Lavadora", "Tiempo", "Velocidad"]
filtro = r"[0-9]"
filtro2 = r"[A-Z]"

PWMT = Timer(9, freq = 15000)

AIN1 = Pin(Pin.cpu.E5, Pin.OUT_PP)
AIN2 = Pin(Pin.cpu.E4, Pin.OUT_PP)
POTA = ADC('PA0')
POTB = ADC('PA1')
POTC = ADC('PA2')
PB1 = Pin('PD5', Pin.IN, Pin.PULL_UP)
PWMA = PWMT.channel(2, Timer.PWM, pin = Pin.cpu.E6, pulse_width_percent = 0)

AIN1.on()
AIN2.off()

def UI():
   tft.clear(0)
   delay(50)
   tft.text(52,5,textos[0],fg)
   tft.text(53,5,textos[0],fg)
   tft.line(0,15,160,15,fg)
   tft.line(80,15,80,69,fg)
   tft.line(0,69,160,69,fg)
   tft.line(0,85,160,85,fg)
   tft.line(0,101,160,101,fg)
   tft.line(0,117,160,117,fg)
   tft.text(100,25,textos[1],fg)
   tft.text(7,25,textos[2],fg)
   tft.text(4,74, "Resistencia tela",fg)
   tft.text(4,90, "Tipo de suciedad",fg)
   tft.text(1,106,"Nivel de suciedad",fg)

LEDR = LED(1)
LEDV = LED(2)
LEDA = LED(3)

while True:
   UI()

   try:
      while True:
         w = 0
         LEDA.on()
         value_1 = (POTA.read()/4095)*3
         f_value = "{:.2f}".format(value_1)
         value_2 = POTB.read()/4095
         s_value = "{:.2f}".format(value_2)
         value_3 = POTC.read()/4095
         t_value = "{:.2f}".format(value_3)

         values = (str(f_value) + "#" + str(s_value) + "#" + str(t_value) + "#" + '0' + "\n")
         values.encode('uint8')
         
         if lf_value != f_value:
            tft.text(127,74, lf_value,bg)
            tft.text(127,74, f_value,fg)
            uart.write(values)
            delay(500)

         if ls_value != s_value:
            tft.text(127,90, ls_value,bg)
            tft.text(127,90, s_value,fg)
            uart.write(values)
            delay(500)

         if lt_value != t_value:
            tft.text(127,106, lt_value,bg)
            tft.text(127,106, t_value,fg)
            uart.write(values)
            delay(500)

         lf_value = f_value
         ls_value = s_value
         lt_value = t_value

         sttbttn1 = PB1.value()
         if sttbttn1 == 0:
            print(0/0)

   except ZeroDivisionError:
      tft.text(127,74, f_value,bl)
      tft.text(127,90, s_value,bl)
      tft.text(127,106, t_value,bl)

   finally:
      for x in range(1,10):
         values = (f_value + "#" + s_value + "#" + t_value + "#" + '1'  + "\n")
         uart.write(values)
         delay(400)
         LEDA.off()

   try:
      while w == 0:
         inMatLab = uart.read()

         firststring = ""
         newstring = ""

         try:
            for x in str(inMatLab):
               if re.search(filtro, x):
                  newstring = newstring + x
               elif re.search(filtro2, x):
                  firststring = newstring
                  newstring = ""
         except:
            inMatLab = "No llegó naaa"
         finally:
            pass

         if firststring == "":
            LEDV.on()
            delay(500)
            LEDV.off()
         else:
            LEDA.on()
            LEDR.on()
            w = 1
            if int(firststring) > 9:
               tft.text(110, 40,firststring,fg)
               tft.text(125, 40, 's',fg)
            else:
               tft.text(118, 40,firststring,fg)
               tft.text(125, 40, 's',fg)
            if newstring == "100":
               tft.text(25, 40,newstring,fg)
               tft.text(50, 40, '%',fg)
            else:
               tft.text(30, 40,newstring,fg)
               tft.text(45, 40, '%',fg)
            delay(500)
            LEDA.off()
            LEDR.off()
            
         last = firststring
         try:
            x = int(firststring) * 1000
            LEDR.on()
            pwm = (int(newstring) / 100) * 50
            pwm = 60 + pwm
            PWMA.pulse_width_percent(pwm)
            
            for i in range(0, 159):
               tft.pixel(0+i, 122, gr)
               delay(int((int(firststring) / 155) * 1000))

            LEDR.off()
            PWMA.pulse_width_percent(0)
         except:
            pass
         finally:
            pass
         

   except KeyboardInterrupt:
      print("Algo ha pasa'o")
   finally:
      tft.backlight(0)
      tft.clear(0)
      tft.rst()
      LEDV.off()
      LEDA.off()
      LEDR.off()
      PWMA.pulse_width_percent(0)
print("Fin del proceso")
