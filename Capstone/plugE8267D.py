import logging
import openhtf.plugs as plugs
from openhtf.util import conf
import time
try:
    import pyvisa
except ImportError:
    logging.error('Failed to import pyvisa, did you:\npip install pyvisa')
    raise

conf.declare('sig_gen_address', default_value='TCPIP::192.168.10.63::INSTR',
             description='Default IP address for Signal Generator.')

class plugE8267D(plugs.BasePlug):

    """
    Class instrument to control E8267D Signal Generator
    """
    @conf.inject_positional_args
    def __init__(self, sig_gen_address):
        rm = pyvisa.ResourceManager('@py')
        self.instrument = rm.open_resource(sig_gen_address)
        idn = self.instrument.query('*IDN?')
        print('Connected to', idn)  # We could probably use test info
    
    def close(self):
        """
        Disconnect.
        :return:
        """
        self.instrument.close()

    # Set the frequency mode
    def set_mode(self, mode):
        self.write(':SOURce:FREQuency:MODE ' + mode)

    # Set frequency on sig gen
    def set_frequency(self, hertz):
        if(self.check_frequency(hertz)):
            self.write(':SOURce:FREQuency:CW ' + str(hertz))


    # Set output power on sig gen
    def set_power(self, decibels):
        if(self.check_power(decibels)):
            self.write(':SOURce:POWer:LEVel:IMMediate:AMPLitude ' + str(decibels))
            

    # Check if frequency is within the bounds
    def check_frequency(self, hertz):
        if(hertz < (25*10**3) or hertz > (20*10**9)):
            return False
        else:
            return True

    # Check if power is within the bounds
    def check_power(self, decibels):
        if(decibels < (-90) or decibels > (25)):
            return False
        else:
            return True


    def write(self, command):
        return self.write(command)