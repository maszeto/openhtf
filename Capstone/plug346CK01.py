import logging
import openhtf.plugs as plugs
from openhtf.util import conf
import time
try:
    import pyvisa
except ImportError:
    logging.error('Failed to import pyvisa, did you:\npip install pyvisa')
    raise

conf.declare('noise_source_address', default_value='TCPIP::192.168.10.63::INSTR',
             description='Default IP address for Agilent Noise Source.')

class plug346CK01(plugs.BasePlug):

    """
    Class instrument to control 346CK01 Agilent Noise Source
    """
    @conf.inject_positional_args
    def __init__(self, noise_source_address):
        rm = pyvisa.ResourceManager('@py')
        self.instrument = rm.open_resource(noise_source_address)
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
