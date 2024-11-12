from Arm_Lib import Arm_Device
import time
Arm = Arm_Device()
time.sleep(.1)

#Arm.Arm_serial_servo_write(id,20, 500)
#time.sleep(1)
#Arm.Arm_serial_servo_write(id,180,500)
#time.sleep(1)


## BOW
Arm.Arm_serial_servo_write(2, 30,1500)
time.sleep(.1)
Arm.Arm_serial_servo_write(3, 50,1500)
time.sleep(.1)
Arm.Arm_serial_servo_write(4, 70,1500)
time.sleep(1)
Arm.Arm_serial_servo_write(6, 90, 500)
time.sleep(.75)
Arm.Arm_serial_servo_write(6,180,500)
time.sleep(.75)
Arm.Arm_serial_servo_write(5, 180,500)
time.sleep(.55)
## GO HOME
Arm.Arm_serial_servo_write(5,90,500)
time.sleep(1)
Arm.Arm_serial_servo_write(2, 90,1500)
time.sleep(.1)
Arm.Arm_serial_servo_write(3, 90,1500)
time.sleep(.1)
Arm.Arm_serial_servo_write(4, 90,1500)
time.sleep(3)
pos = Arm.Arm_serial_servo_read(2)
print(pos)
