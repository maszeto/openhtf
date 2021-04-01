import logging
import openhtf.plugs as plugs
from openhtf.util import conf
import time
try:
    import pyvisa
except ImportError:
    logging.error('Failed to import pyvisa, did you:\npip install pyvisa')
    raise

conf.declare('sig_analyzer_address', default_value='TCPIP::192.168.10.63::INSTR',
             description='Default IP address for Signal Analyzer.')


class plugN9000B(plugs.BasePlug):

    """
    Class instrument to control N9000B Signal Analyzer
    """
    @conf.inject_positional_args
    def __init__(self, sig_analyzer_address):
        rm = pyvisa.ResourceManager('@py')
        self.instrument = rm.open_resource(sig_analyzer_address)
        idn = self.instrument.query('*IDN?')
        print('Connected to', idn)  # We could probably use test info
    
    def close(self):
        """
        Disconnect.
        :return:
        """
        self.instrument.close()

    # TODO: Set frequency on sig analyzer
    def set_frequency(self, type, hertz):
        # 
        if(self.check_frequency(hertz)):
            if(type == "Center"):
                self.write('FREQuency:CENTer ' + str(hertz))
            elif(type == "Step"):
                self.write('FREQuency:SPAN ' + str(hertz))

    # TODO: Set marker to frequency on sig analyzer
    def set_marker(self, hertz):
        if(self.check_frequency(hertz)):
            self.write('CALCulate:MARKer:X ' + str(hertz))

    # TODO: Move marker to frequency on sig analyzer
    def move_marker(self, hertz):
        if(self.check_frequency(hertz)):
            self.write('CALCulate:MARKer:X ' + str(hertz))

    # TODO: Read vertical axis on sig analyzer
    def read_power(self):
        self.write('CALCulate:MARKer:Y')

    # TODO: Check if frequency is within the bounds
    def check_frequency(self, hertz):
        if(hertz < (9*10**3) or hertz > (3*10**9)):
            return False
        else:
            return True

    def write(self, command):
        return self.write(command)
