from machine import I2S
from machine import Pin
import math, struct

def make_tone(rate, bits, frequency):
    # create a buffer containing the pure tone samples
    samples_per_cycle = rate // frequency
    sample_size_in_bytes = bits // 8
    samples = bytearray(samples_per_cycle * sample_size_in_bytes)
    volume_reduction_factor = 32
    range = pow(2, bits) // 2 // volume_reduction_factor
    
    if bits == 16:
        format = "<h"
    else:  # assume 32 bits
        format = "<l"
    
    for i in range(samples_per_cycle):
        sample = range + int((range - 1) * math.sin(2 * math.pi * i / samples_per_cycle))
        struct.pack_into(format, samples, i * sample_size_in_bytes, sample)
        
    return samples

bck_pin = Pin(26)   # Bit clock output (BCLK)
ws_pin = Pin(0)    # Word clock output (or left right clock; LRC)
sdout_pin = Pin(25) # Serial data output (SDATA)

audio_out = I2S(0,                                  # create I2S peripheral to write audio
                sck=bck_pin,
                ws=ws_pin,
                sd=sdout_pin,   # sample data to an Adafruit I2S Amplifier
                mode=I2S.TX,  # breakout board,
                bits=16,
                format=I2S.MONO,                        # based on MAX98357A device
                rate=22_050,
                ibuf=2000)
               
samples = make_tone(22_050, 16, 440)

num_bytes_written = audio_out.write(samples)              # write audio samples to amplifier
                                                          # note:  blocks until sample array is emptied
                                                          # - see optional timeout argument
                                                          # to configure maximum blocking duration       

