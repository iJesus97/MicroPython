from pyb import Pin, delay, ADC, Timer

#Configuracion de los LEDS indicadores
LI1 = Pin(Pin.cpu.E12, Pin.OUT_PP)
LI2 = Pin(Pin.cpu.E13, Pin.OUT_PP)
LI3 = Pin(Pin.cpu.E14, Pin.OUT_PP)
LI4 = Pin(Pin.cpu.E15, Pin.OUT_PP)
LI5 = Pin(Pin.cpu.D0, Pin.OUT_PP)
LI6 = Pin(Pin.cpu.D1, Pin.OUT_PP)
LI7 = Pin(Pin.cpu.D2, Pin.OUT_PP)
LI8 = Pin('D3', Pin.OUT_PP)

#Configuracion de los Switch
SW1 = Pin('PD5', Pin.IN, Pin.PULL_UP)
SW2 = Pin('PD4', Pin.IN, Pin.PULL_UP)

#Configuracion de los sensores ópticos
S1 = ADC('PB1')
S2 = ADC('PB0')
S3 = ADC('PC5')
S4 = ADC('PC4')
S5 = ADC('PA7')
S6 = ADC('PA6')
S7 = ADC('PA5')
S8 = ADC('PA4')

#Señales de control del puente H y los motores
PWMT = Timer(4, freq = 15000) #Timer del PWM
STBY = Pin(Pin.cpu.B12, Pin.OUT_PP) #Activación general del puente H
#Motor A Izquierda visto desde arriba
AIN1 = Pin(Pin.cpu.B15, Pin.OUT_PP)
AIN2 = Pin(Pin.cpu.D8, Pin.OUT_PP)
PWMA = PWMT.channel(2, Timer.PWM, pin = Pin.cpu.D13, pulse_width_percent = 0) #Velocidad del PWM 1
#Motor B Derecha visto desde arriba
BIN1 = Pin(Pin.cpu.B13, Pin.OUT_PP)
BIN2 = Pin(Pin.cpu.D14, Pin.OUT_PP)
PWMB = PWMT.channel(1, Timer.PWM, pin = Pin.cpu.D12, pulse_width_percent = 0) #Velocidad del PWM 2

#Encender el puente H
AIN1.on()
AIN2.off()
BIN1.on()
BIN2.off()
STBY.on()

A = 100
B = A*0.85
C = A*0.85
D = B
E = C

#Dirección de movimiento hacia delante
try:
	while True:
		x = SW1.value() #Regresa un 1 o 0
		if x == 0:
			while True:
				y = SW2.value() #Regresa un 1 o 0
				
				S1R = round((S1.read()/4096)-0.3) #Devuelve un 1 o 0
				S2R = round((S2.read()/4096)-0.3)
				#S3R = round((S3.read()/4096)-0.3)
				S4R = round((S4.read()/4096)-0.3)
				S5R = round((S5.read()/4096)-0.3)
				#S6R = round((S6.read()/4096)-0.3)
				S7R = round((S7.read()/4096)-0.3)
				S8R = round((S8.read()/4096)-0.3)

				if S1R == 0 and S2R == 1 and S4R == 1 and S5R == 1 and S7R == 1 and S8R == 1:
					PWMA.pulse_width_percent(0)
					PWMB.pulse_width_percent(100)

				elif S1R == 0 and S2R == 0 and S4R == 1 and S5R == 1 and S7R == 1 and S8R == 1:
					PWMA.pulse_width_percent(0)
					PWMB.pulse_width_percent(100)

				elif S1R == 1 and S2R == 0 and S4R == 0 and S5R == 1 and S7R == 1 and S8R == 1:
					PWMA.pulse_width_percent(40)
					PWMB.pulse_width_percent(100)

				elif S1R == 1 and S2R == 0 and S4R == 1 and S5R == 1 and S7R == 1 and S8R == 1:
					PWMA.pulse_width_percent(50)
					PWMB.pulse_width_percent(100)

				elif S1R == 0 and S2R == 0 and S4R == 0 and S5R == 1 and S7R == 1 and S8R == 1:
					PWMA.pulse_width_percent(50)
					PWMB.pulse_width_percent(100)

				elif S1R == 1 and S2R == 1 and S4R == 0 and S5R == 1 and S7R == 1 and S8R == 1:
					PWMA.pulse_width_percent(50)
					PWMB.pulse_width_percent(100)

				elif S1R == 1 and S2R == 1 and S4R == 0 and S5R == 0 and S7R == 1 and S8R == 1:
					PWMA.pulse_width_percent(100)
					PWMB.pulse_width_percent(100)

				elif S1R == 1 and S2R == 1 and S4R == 1 and S5R == 0 and S7R == 0 and S8R == 1:
					PWMA.pulse_width_percent(100)
					PWMB.pulse_width_percent(50)

				elif S1R == 1 and S2R == 1 and S4R == 1 and S5R == 1 and S7R == 0 and S8R == 1:
					PWMA.pulse_width_percent(100)
					PWMB.pulse_width_percent(50)

				elif S1R == 1 and S2R == 1 and S4R == 1 and S5R == 1 and S7R == 0 and S8R == 0:
					PWMA.pulse_width_percent(100)
					PWMB.pulse_width_percent(0)

				elif S1R == 1 and S2R == 1 and S4R == 1 and S5R == 1 and S7R == 1 and S8R == 0:
					PWMA.pulse_width_percent(100)
					PWMB.pulse_width_percent(30)

				elif S1R == 1 and S2R == 1 and S4R == 1 and S5R == 0 and S7R == 0 and S8R == 0:
					PWMA.pulse_width_percent(100)
					PWMB.pulse_width_percent(0)

				elif S1R == 1 and S2R == 1 and S4R == 1 and S5R == 0 and S7R == 1 and S8R == 1:
					PWMA.pulse_width_percent(100)
					PWMB.pulse_width_percent(0)

				elif S1R == 1 and S2R == 1 and S4R == 1 and S5R == 1 and S7R == 1 and S8R == 1:
					PWMA.pulse_width_percent(0)
					PWMB.pulse_width_percent(0)

				
				else:
					PWMA.pulse_width_percent(0)
					PWMB.pulse_width_percent(0)

				if y == 0:
					LI1.off()
					LI2.off()
					LI3.off()
					LI4.off()
					PWMA.pulse_width_percent(0)
					PWMB.pulse_width_percent(0)
					break

except KeyboardInterrupt:
	print("Se ha parado el codigo mediante teclas fisicas")
	
finally:
	PWMA.pulse_width_percent(0)
	PWMB.pulse_width_percent(0)
	LI1.off()
	LI2.off()
	LI3.off()
	LI4.off()
	LI5.off()
	LI6.off()
	LI7.off()
	LI8.off()
	AIN1.off()
	AIN2.off()
	BIN1.off()
	BIN2.off()
	STBY.off()