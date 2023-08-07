from pyb import Pin, ADC, Timer, LED, delay
from ophyra_mpu60 import MPU6050

LED3 = LED(3)

try:
	LED3.on()
	Sensor = MPU6050()
   Sensor.init(16, 2000)

   #SAG = MPU6050()
	#SAG.init(2,250)
   
   while True:
      LED1.on()
      LED3.on()
      acelX = Sensor.accX()
      acelY = Sensor.accY()
      acelZ = Sensor.accZ()

      giroscopioX = Sensor.gyrX()
      giroscopioY = Sensor.gyrY()
      giroscopioZ = Sensor.gyrZ()
      
      PWMT = Timer(5, freq = 15000)
      STBY = Pin(Pin.cpu.E15, Pin.OUT_PP) #Activación general del puente H
      
      AIN1 = Pin(Pin.cpu.E11, Pin.OUT_PP)
      AIN2 = Pin(Pin.cpu.E12, PIN.OUT_PP)
      PWMA = PWMT.channel(1, Timer.PWM, pin = Pin.cpu.A0, pulse_width_percent = 0) #Velocidad del PWM 1
      
      #Motor B Derecha visto desde arriba
      BIN1 = Pin(Pin.cpu.E13, Pin.OUT_PP)
      BIN2 = Pin(Pin.cpu.E14, Pin.OUT_PP)
      PWMB = PWMT.channel(1, Timer.PWM, pin = Pin.cpu.A1, pulse_width_percent = 0) #Velocidad del PWM 2

      #Encender el puente H
      STBY.on()
      #Dirección de movimiento hacia delante
      AIN1.on()
      AIN2.off()
      BIN1.on()
      BIN2.off()

finally:
	LED3.off()