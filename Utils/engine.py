import minimalmodbus
from Utils.Register_Config import RegisterConfiguration

registers = RegisterConfiguration()


# Link for CRC Calculation
# https://crccalc.com/
# DATA: 0x0106000008008E0A example CRC-16/MODBUS : 0x8E0A
# DATA: 0x0106000007008BFA example CRC-16/MODBUS : 0x8BFA
class Engine():
    def __init__(self, serial_port, slave_address=1, serial_baudrate=9600, serial_timeout=10, instrument_mode=None):
        self.instrument = minimalmodbus.Instrument(serial_port, slave_address)  # port name, slave address (in decimal)
        self.instrument.serial.baudrate = serial_baudrate
        self.instrument.serial.timeout = serial_timeout
        self.instrument.mode = minimalmodbus.MODE_RTU

    ############################################## WRITE ROUTINES ######################################################

    def open(self, channel):
        # [Slave ID] [Function] [Channel Number/Register Address]    [DATA]      [CRC CHECK]
        #   0x01       0x06               0x00 0x00                0x01 0x00
        try:
            _value = registers.convert_to_decimal(registers.OPEN_CODE)
            self.instrument.write_register(registeraddress=channel,
                                           value=_value,
                                           number_of_decimals=0,
                                           functioncode=6)

        except Exception as e:
            print(e)
            return False
        return True

    def close(self, channel):
        # [Slave ID] [Function] [Channel Number/Register Address]    [DATA]      [CRC CHECK]
        #   0x01       0x06               0x00 0x00                0x02 0x00
        try:
            _value = registers.convert_to_decimal(registers.CLOSE_CODE)
            self.instrument.write_register(registeraddress=channel,
                                           value=_value,
                                           number_of_decimals=0,
                                           functioncode=6)

        except Exception as e:
            print(e)
            return False
        return True

    def toggle(self, channel):
        # [Slave ID] [Function] [Channel Number/Register Address]    [DATA]      [CRC CHECK]
        #   0x01       0x06               0x00 0x00                0x03 0x00
        try:
            _value = registers.convert_to_decimal(registers.TOGGLE_CODE)
            self.instrument.write_register(registeraddress=channel,
                                           value=_value,
                                           number_of_decimals=0,
                                           functioncode=6)

        except Exception as e:
            print(e)
            return False
        return True

    def latch(self, channel):
        # [Slave ID] [Function] [Channel Number/Register Address]    [DATA]      [CRC CHECK]
        #   0x01       0x06               0x00 0x00                0x04 0x00
        try:
            _value = registers.convert_to_decimal(registers.LATCH_CODE)
            self.instrument.write_register(registeraddress=channel,
                                           value=_value,
                                           number_of_decimals=0,
                                           functioncode=6)

        except Exception as e:
            print(e)
            return False
        return True

    def momentary(self, channel):
        # [Slave ID] [Function] [Channel Number/Register Address]    [DATA]      [CRC CHECK]
        #   0x01       0x06               0x00 0x00                0x05 0x00
        try:
            _value = registers.convert_to_decimal(registers.MOMENTARY_CODE)
            self.instrument.write_register(registeraddress=channel,
                                           value=_value,
                                           number_of_decimals=0,
                                           functioncode=6)

        except Exception as e:
            print(e)
            return False
        return True

    def delay(self, channel, time):
        # time: 0 - 255 s
        # [Slave ID] [Function] [Channel Number/Register Address]    [DATA]      [CRC CHECK]
        #   0x01       0x06               0x00 0x00                0x06 0x00

        # second byte group : time in seconds 0x00 -> 0xff or '00' -> 'ff' (formatting rule)
        try:
            _value = registers.DELAY_CODE + format(time, '02x')
            _value = registers.convert_to_decimal(_value)

            self.instrument.write_register(registeraddress=channel,
                                           value=_value,
                                           number_of_decimals=0,
                                           functioncode=6)

        except Exception as e:
            print(e)
            return False
        return True

    def open_all(self):
        # [Slave ID] [Function] [Channel Number/Register Address]    [DATA]      [CRC CHECK]
        #   0x01       0x06               0x00 0x00                0x07 0x00      0x8B  0xFA
        try:
            _value = registers.convert_to_decimal(registers.OPEN_ALL_CODE)
            self.instrument.write_register(registeraddress=0,
                                           value=_value,
                                           number_of_decimals=0,
                                           functioncode=6)

        except Exception as e:
            print(e)
            return False
        return True

    def close_all(self):
        # [Slave ID] [Function] [Channel Number/Register Address]    [DATA]      [CRC CHECK]
        #   0x01       0x06               0x00 0x00                0x08 0x00     0x8E  0x0A
        try:
            _value = registers.convert_to_decimal(registers.CLOSE_ALL_CODE)
            self.instrument.write_register(registeraddress=0,
                                           value=_value,
                                           number_of_decimals=0,
                                           functioncode=6)

        except Exception as e:
            print(e)
            return False
        return True

    ############################################## READ ROUTINES #######################################################

    def read_channel_state(self, channel):
        # Reading channel 1 state example
        # [Slave ID] [Function]    [Start Register Address]    [DATA Length]      [CRC CHECK]
        #   0x01       0x03               0x00 0x01              0x00 0x01        0xD5  0xCA
        try:
            result = self.instrument.read_register(registeraddress=channel,
                                                   number_of_decimals=0,
                                                   functioncode=3)

        except Exception as e:
            print(e)
            return False
        return result

    def read_multiple_channel_state(self, start_channel, number_of_channels):
        # Reading channel 1 state example
        # [Slave ID] [Function]    [Start Register Address]    [DATA Length]      [CRC CHECK]
        #   0x01       0x03               0x00 0x01              0x00 0x10        0x15  0xC6
        try:
            result = self.instrument.read_registers(registeraddress=start_channel,
                                                   number_of_registers=number_of_channels,
                                                   functioncode=3)

        except Exception as e:
            print(e)
            return False
        return result
