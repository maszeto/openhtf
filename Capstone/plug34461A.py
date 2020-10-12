import pyvisa

class plug34461A:

    """
    Class instrument to control 34461A Series Digital Multimeter
    """

    def __init__(self, address):
        print('Trying to connect to', address)
        try:
            self.instrument = pyvisa.ResourceManager().open_resource(address)
            idn = self.instrument.query('*IDN?')
            print('Connected to\n', idn)
        except:
            raise "Couldn't connect to instrument " + address
    
    def close(self):
        """
        Disconnect.
        :return:
        """
        self.instrument.close()


    # TODO: Read the resistance
    def read_resist(self):
        return 0

    # TODO: Read the current
    def read_current(self):
        return 0

    # TODO: Add ranges and other parameters
    def read_voltage(self, mode):
        """
        Args:
            mode (int): A value of 1 or 2, representing ac or dc respectively, if the number is greater than 2, it will be treated as dc, less than 1, ac
        Returns:
            voltage (float): The voltage in volts
        """
        if mode <= 1:
            values = instrument.query_ascii_values(':MEASure:VOLTage:AC?')
            acVoltage = values[0]
            return acVoltage

        else:
            values = instrument.query_ascii_values(':MEASure:VOLTage:DC?')
            dcVoltage = values[0]
            return dcVoltage

        return 0

    # TODO: Check the continuity
    def continuity_check(self):
        """
        Args:
            None
        Returns:
            continuity(bool): True if beep, else false
        """
        values = instrument.query_ascii_values(':MEASure:CONTinuity?')
        continuity = values[0]

        if continuity <= 10:
            #10 is the threshold for the beep
            return True 
        else:
            return False

        return 0