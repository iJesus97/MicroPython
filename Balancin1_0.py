from pyb import Pin, ADC, Timer, LED, delay, udelay
from ophyra_mpu60 import MPU6050
import math

SW1 = Pin('PD5', Pin.IN, Pin.PULL_UP)
SW2 = Pin('PD4', Pin.IN, Pin.PULL_UP)

PWMT = Timer(4, freq = 15000)

AIN1 = Pin(Pin.cpu.D11, Pin.OUT_PP)
AIN2 = Pin(Pin.cpu.D9, Pin.OUT_PP)
PWMA = PWMT.channel(2, Timer.PWM, pin = Pin.cpu.D13, pulse_width_percent = 0)

BIN1 = Pin(Pin.cpu.D10, Pin.OUT_PP)
BIN2 = Pin(Pin.cpu.D8, Pin.OUT_PP)
PWMB = PWMT.channel(1, Timer.PWM, pin = Pin.cpu.D12, pulse_width_percent = 0)

Rojo = LED(1)
Verde = LED(2)
Azul = LED(3)                          

Sensor = MPU6050()
Sensor.init(16, 2000)
rk_1 = 0
rk_2 = 0
ck_1 = 0
ck_2 = 0
c_k = 0   

state = False

try:
   while True:
      Azul.on()
      sttbttn1 = SW1.value()
      if sttbttn1 == 0:
         state = True
      
      while state:
         sttbttn2 = SW2.value()
         if sttbttn2 == 0:
            print("hola"/0)

         acelX = Sensor.accX()
         acelY = Sensor.accY()
         acelZ = Sensor.accZ()
         
         giroscopioX = Sensor.gyrX()
         giroscopioY = Sensor.gyrY()
         giroscopioZ = Sensor.gyrZ()
         
         ang_rad = math.atan(acelY / acelZ)
         ang = math.degrees(ang_rad)
         ang = ang + 90
         #print(ang)

         udelay(10000)
         Entrada = acelZ
         
         Error = Entrada - c_k
         ck_2 = ck_1
         rk_2 = rk_1
         rk_1 = Error
         ck_1 = c_k
         c_k = 1.979978*(ck_1) - 9.8*(rk_1) + 10.897*(Error) - 0.974978*(ck_2)
         y = c_k * 0.280
         print(y, end = "#")
         
         x = int(y)
         print(x)

         if ang >= -2 and ang <= 65:
            AIN1.on()
            AIN2.off()
            BIN1.on()
            BIN2.off()
            PWMA.pulse_width_percent(100)
            PWMB.pulse_width_percent(100)

         elif ang > 70 and ang <= 85:
            AIN1.on()
            AIN2.off()
            BIN1.on()
            BIN2.off()
            PWMA.pulse_width_percent(100 - x)
            PWMB.pulse_width_percent(100 - x)

         elif ang > 85 and ang <= 95:
            AIN1.off()
            AIN2.off()
            BIN1.off()
            BIN2.off()
            PWMA.pulse_width_percent(0)
            PWMB.pulse_width_percent(0)
            delay(50)
         
         elif ang > 95 and ang <= 110:
            AIN1.off()
            AIN2.on()
            BIN1.off()
            BIN2.on()
            PWMA.pulse_width_percent(100 - x)
            PWMB.pulse_width_percent(100 - x)

         elif ang > 115 and ang <= 182:
            AIN1.off()
            AIN2.on()
            BIN1.off()
            BIN2.on()
            PWMA.pulse_width_percent(100)
            PWMB.pulse_width_percent(100)
            
         else:
            PWMA.pulse_width_percent(0)
            PWMB.pulse_width_percent(0)
            AIN1.off()
            AIN2.off()
            BIN1.off()
            BIN2.off()

except KeyboardInterrupt:
   print("Se ha parado el código mediante teclas en la computadora")

except ZeroDivisionError:
   print("Error inesperado")

except TypeError:
   print("Se ha parado el código mediante teclas en la tarjeta")

finally:
   Rojo.on()
   Verde.on()
   PWMA.pulse_width_percent(0)
   PWMB.pulse_width_percent(0)
   AIN1.off()
   AIN2.off()
   BIN1.off()
   BIN2.off()
   Azul.off()
   delay(1000)
   Rojo.off()
   Verde.off()

# Los valores mínimos del ángulo es de 63 y 112 grados
# El valor mínimo del PWM para el funcionamiento correcto de los motores es de 70% con voltaje de 6.3V
# El punto de equilibrio está en el intervalo de [85, 87] grados