import logging
import openhtf.plugs as plugs
from openhtf.util import conf
import time
try:
    import pyvisa
except ImportError:
    logging.error('Failed to import pyvisa, did you:\npip install pyvisa')
    raise

conf.declare('microwave_sig_gen_address', default_value='TCPIP::192.168.10.63::INSTR',
             description='Default IP address for Microwave Analog Signal Generator.')


class plugN5183B(plugs.BasePlug):

    """
    Class instrument to control N5183B MXG X-Series Microwave Analog Signal Generator
    """
    @conf.inject_positional_args
    def __init__(self, microwave_sig_gen_address):
        rm = pyvisa.ResourceManager('@py')
        self.instrument = rm.open_resource(microwave_sig_gen_address)
        idn = self.instrument.query('*IDN?')
        print('Connected to', idn)  # We could probably use test info

    def close(self):
        """
        Disconnect.
        :return:
        """
        self.instrument.close()
