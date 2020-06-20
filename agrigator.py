def agrigator():
    while True:
        for x in range(step_count):
            GPIO.output(stepper, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(stepper, GPIO.LOW)
            time.sleep(delay)
        print('finished loop')
        GPIO.output(dir, CCW)
        for x in range(step_count):
            GPIO.output(stepper, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(stepper, GPIO.LOW)
            time.sleep(delay)
        print('finished loop2')