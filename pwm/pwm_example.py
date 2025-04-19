from periphery import PWM
import time

pwm = PWM(2, 0)  #PWM object is initialized for pwmchip2 channel0

try:
    pwm.frequency = 50 #PWM frequency is set to 1000 Hz
    pwm.duty_cycle = 0
    pwm.polarity = "normal"
    pwm.enable()
    direction = 1  

    while True:
        pwm.duty_cycle += 0.01 * direction
        pwm.duty_cycle = round(pwm.duty_cycle, 2) #round function is used to keep it to two decimal places
        if pwm.duty_cycle == 0.2: #reaching the maximum the direction is reversed
            direction = -1
        elif pwm.duty_cycle == 0.0: ##reaching the minimum the direction is reversed
            direction = 1
            
        time.sleep(0.05) 

except KeyboardInterrupt:
    pass

finally:
    pwm.close()