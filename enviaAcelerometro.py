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
			LED3.on()
			numeros_1 = SAG.accX()*66
			numeros_2 = SAG.accY()*66
			numeros_3 = SAG.accZ()*66
			
			snumeros_1 = "#" + str(numeros_1)+"#"
			snumeros_2 = str(numeros_2)+"#"
			snumeros_3 = str(numeros_3)+"#"

			cadena_numeros = snumeros_1 + snumeros_2 + snumeros_3
			print(cadena_numeros)

			delay(75)
			LED1.off()
			LED3.off()

finally:
	LED2.off()