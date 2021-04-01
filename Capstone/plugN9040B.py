import logging
import openhtf.plugs as plugs
from openhtf.util import conf
import time
try:
    import pyvisa
except ImportError:
    logging.error('Failed to import pyvisa, did you:\npip install pyvisa')
    raise

conf.declare('uxa_sig_analyzer_address', default_value='TCPIP::192.168.10.63::INSTR',
             description='Default IP address for UXA Signal Analyzer.')

class plugN9040B(plugs.BasePlug):

    """
    Class instrument to control N9040B UXA Signal Analyzer
    """
    @conf.inject_positional_args
    def __init__(self, uxa_sig_analyzer_address):
        rm = pyvisa.ResourceManager('@py')
        self.instrument = rm.open_resource(uxa_sig_analyzer_address)
        idn = self.instrument.query('*IDN?')
        print('Connected to', idn)  # We could probably use test info
    
    def close(self):
        """
        Disconnect.
        :return:
        """
        self.instrument.close()

    def write(self, command):
        return self.write(command)