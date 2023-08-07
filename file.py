from pyb import Pin, delay, ADC, Timer, LED

LED1 = LED(1)
LED2 = LED(2)
LED3 = LED(3)

SW1 = Pin('PC2', Pin.IN, Pin.PULL_UP)
SW2 = Pin('PD5', Pin.IN, Pin.PULL_UP)
SW3 = Pin('PD4', Pin.IN, Pin.PULL_UP)
SW4 = Pin('PD3', Pin.IN, Pin.PULL_UP)
Prueba = Pin('PA7', Pin.OUT_PP)

try:
	while True:
		Prueba.on()
		if not SW1.value():
			LED1.on()
		else:
			LED1.off()

		if not SW2.value():
			LED2.on()
		else:
			LED2.off()

		if not SW3.value():
			LED3.on()
		else:
			LED3.off()

		if not SW4.value():
			LED1.on()
			delay(200)
			LED2.on()
			delay(200)
			LED3.on()
			delay(200)
			LED3.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
			LED2.toggle()
			delay(200)
			LED3.toggle()
			delay(200)
			LED1.toggle()
			delay(200)
finally:
	LED1.off()
	LED2.off()
	LED3.off()
	Prueba.off()