from pyb import Pin, delay, ADC, DAC

#Configuracion de la salida
Cz = Pin(Pin.cpu.A4, Pin.OUT_PP)

rk_1 = 0
rk_2 = 0
ck_1 = 0
ck_2 = 0
c_k = 0

#Configuracion de la entrada
Rz = ADC('PA0')

try:
   while True:
      Entrada = Rz.read()
      Error = Entrada - c_k
      c_k = 1.5488*(ck_1) - 0.5488*(ck_2) + 0.14881*(rk_1) + 0.121905152*(rk_2)
      ck_2 = ck_1
      ck_1 = c_k
      rk_2 = rk_1
      rk_1 = Error
      print(Entrada)
      print(c_k)
      delay(500)
      Numero = int(c_k)
      Salida = DAC(Cz)
      Salida.write(Numero)
      print(Numero)
      print("###############")
      #4095 es el maximo 3.3v
      #~2700

except KeyboardInterrupt:
   print("Se ha parado el codigo mediante teclas fisicas")
   
finally:
   pass

############################################

from ophyra_tftdisp import ST7735
from pyb import Pin, ADC, Timer, LED, delay
from ophyra_mpu60 import MPU6050

SW1 = Pin('PC2', Pin.IN, Pin.PULL_UP)
SW2 = Pin('PD5', Pin.IN, Pin.PULL_UP)
SW3 = Pin('PD4', Pin.IN, Pin.PULL_UP)
SW4 = Pin('PD3', Pin.IN, Pin.PULL_UP)

LED1 = LED(1)
LED2 = LED(2)
LED3 = LED(3)

try:
	LED2.on()
	SAG = MPU6050()
	SAG.init(2,250)

	while True:
		if SW1.value() == 1:
			LED1.on()
			LED2.off()
			numeros_1 = SAG.accX()*66
			numeros_2 = SAG.accY()*66
			numeros_3 = SAG.accZ()*66
			
			snumeros_1 = "#" + str(numeros_1)+"#"
			snumeros_2 = str(numeros_2)+"#"
			snumeros_3 = str(numeros_3)+"#"

			cadena_numeros = snumeros_1 + snumeros_2 + snumeros_3
			print(cadena_numeros)

			delay(75)

finally:
	LED2.off()