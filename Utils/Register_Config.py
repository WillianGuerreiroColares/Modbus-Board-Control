import struct

#Register table

class RegisterConfiguration:
    def __init__(self):
        #Write Registers
        self.WRITE_FUNCTION_CODE = '06'
        self.OPEN_CODE = '0100'
        self.CLOSE_CODE = '0200'
        self.TOGGLE_CODE = '0300'
        self.LATCH_CODE = '0400'
        self.MOMENTARY_CODE = '0500'
        self.DELAY_CODE = '06'
        self.OPEN_ALL_CODE = '0700'
        self.CLOSE_ALL_CODE = '0800'

    def convert_to_decimal(self, code):
        new_value = int(code, 16)
        return new_value
