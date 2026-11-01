from machine import I2C, Pin, PWM
import utime

i2c = I2C(0, scl=Pin(5), sda=Pin(4)) #change these as per your wiring
MPR121_ADDR = 0x5A

def init_mpr121():
    try:
        # Soft reset the chip
        i2c.writeto_mem(MPR121_ADDR, 0x80, b'\x63')
        utime.sleep_ms(10)
        
        # Configure baseline filtering and thresholds for touch/release
        # This tells the chip how sensitive to be when you touch the fruit
        for i in range(12):
            # We bumped these up even higher to stop the vegetable noise!
            i2c.writeto_mem(MPR121_ADDR, 0x41 + (i*2), b'\x3C') # Touch threshold 
            i2c.writeto_mem(MPR121_ADDR, 0x42 + (i*2), b'\x32') # Release threshold
            
        # Set filtering registers
        i2c.writeto_mem(MPR121_ADDR, 0x2B, b'\x01')
        i2c.writeto_mem(MPR121_ADDR, 0x2C, b'\x01')
        i2c.writeto_mem(MPR121_ADDR, 0x2D, b'\x00')
        i2c.writeto_mem(MPR121_ADDR, 0x2E, b'\x00')
        i2c.writeto_mem(MPR121_ADDR, 0x2F, b'\x01')
        i2c.writeto_mem(MPR121_ADDR, 0x30, b'\x01')
        i2c.writeto_mem(MPR121_ADDR, 0x31, b'\xff')
        i2c.writeto_mem(MPR121_ADDR, 0x32, b'\x02')
        
        # Enable all 12 electrodes (turn on electrode configuration register)
        i2c.writeto_mem(MPR121_ADDR, 0x5E, b'\x0C') 
        print("✅ MPR121 configured successfully without libraries!")
    except Exception as e:
        print("❌ Error connecting to MPR121. Check your wiring!", e)

# 4. Custom Function to read which pins are touched
def read_touch():
    # Read the status registers (0x00 and 0x01) which hold the 12 bits of touch data
    data = i2c.readfrom_mem(MPR121_ADDR, 0x00, 2)
    # Combine the two 8-bit bytes into one 16-bit binary integer
    touch_status = data[0] | (data[1] << 8)
    return touch_status
