import logging
import openhtf.plugs as plugs
from openhtf.util import conf
try:
    import pyvisa
except ImportError:
    logging.error('Failed to import pyvisa, did you:\npip install pyvisa')
    raise

conf.declare('dmm_address', default_value='TCPIP::192.168.10.62::INSTR',
             description='Default IP address for Digital Multimeter.')

class plug34461A(plugs.BasePlug):

    """
    Class instrument to control 34461A Series Digital Multimeter
    """
    @conf.inject_positional_args
    def __init__(self, dmm_address):
        self.instrument = pyvisa.ResourceManager('@py').open_resource(dmm_address)
        idn = self.instrument.query('*IDN?')
        print('Connected to', idn)

    def close(self):
        """
        Disconnect.
        :return:
        """
        self.instrument.close()

    # TODO: Read the resistance
    def read_resistance(self):
        return float(self.query('MEASure:RESistance?'))

    # TODO: Read the current
    def read_current(self, mode):
        """
        Args:
            mode (int): A value of 1 or 2, representing ac or dc respectively, 
            if the number is greater than 2, it will be treated as dc, less than 1, ac
        Returns:
            current (float): The current in amps
        """
        if mode <= 1:
            return self.query(':MEASure:CURRent:AC?')

        else:
            return self.query(':MEASure:CURRent:DC?')

    # TODO: Add ranges and other parameters
    def read_voltage(self, mode):
        """
        Args:
            mode (int): A value of 1 or 2, representing ac or dc respectively, 
            if the number is greater than 2, it will be treated as dc, less than 1, ac
        Returns:
            voltage (float): The voltage in volts
        """
        if mode <= 1:
            return self.query(':MEASure:VOLTage:AC?')

        else:
            return self.query(':MEASure:VOLTage:DC?')

        return 0

    # TODO: Check the continuity
    def continuity_check(self):
        """
        Args:
            None
        Returns:
            continuity(bool): True if beep, else false
        """
        values = self.query(':MEASure:CONTinuity?')
        continuity = values[0]

        if continuity <= 10:
            #10 is the threshold for the beep
            return True 
        else:
            return False

    # TODO add try except and handle error
    def query(self, command):
        """Handle all queries to instrument"""
        return self.instrument.query(command)

    # TODO add try except and handle error
    def write(self, command):
        """ Handle all writes to instrument """
        self.instrument.write(command)
        
