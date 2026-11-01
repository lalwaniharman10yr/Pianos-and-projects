My Special Library link below

https://github.com/lalwaniharman10yr/MicroPython-Libraries-for-Hardware-and-Stuff/tree/main

My micropython code, depends on your pinout

import utime
from mylib import Keypad4x4, PBUZZER

# --- PIN CONFIGURATIONS ---
# Define the GPIO pin where your passive buzzer is connected
BUZZER_PIN = 15

# Define your 4x4 matrix keypad GPIO pin connections
R1, R2, R3, R4 = 2, 3, 4, 5
C1, C2, C3, C4 = 6, 7, 8, 9

# --- PIANO KEY MAP CONFIGURATION ---
# Map every matrix key character to a dedicated musical frequency (Hz)
NOTE_FREQUENCIES = {
    '1': 262,  # C4
    '2': 294,  # D4
    '3': 330,  # E4
    'A': 349,  # F4
    
    '4': 392,  # G4
    '5': 440,  # A4
    '6': 494,  # B4
    'B': 523,  # C5
    
    '7': 587,  # D5
    '8': 659,  # E5
    '9': 698,  # F5
    'C': 784,  # G5
    
    '*': 880,  # A5
    '0': 988,  # B5
    '#': 1047, # C6
    'D': 1175  # D6
}

print("=========================================")
print("  Hammu Piano System Online!             ")
print("  Press keypad buttons to play tones.     ")
print("=========================================")

# --- MAIN RUNTIME LOOP ---
while True:
    # Scan the keypad using your library function
    key = Keypad4x4(R1, R2, R3, R4, C1, C2, C3, C4)
    
    if key is not None:
        # Get the frequency mapped to the pressed key
        frequency = NOTE_FREQUENCIES[key]
        print(f"Key Matrix Hit: [{key}] -> Playing {frequency} Hz")
        
        # Call your library's PBUZZER function (pi, man, dice)
        # pi = pin, man = frequency, dice = duration in milliseconds
        PBUZZER(BUZZER_PIN, frequency, 150)
        
        # Debounce breakdown to ensure clean, singular note triggers
        utime.sleep_ms(150)
        
    # Standard slight sleep loop to prevent core strain
    utime.sleep_ms(10)
