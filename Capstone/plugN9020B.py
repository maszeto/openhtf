import logging
import openhtf.plugs as plugs
from openhtf.util import conf
import time
try:
    import pyvisa
except ImportError:
    logging.error('Failed to import pyvisa, did you:\npip install pyvisa')
    raise

conf.declare('mxa_sig_analyzer_address', default_value='TCPIP::192.168.10.63::INSTR',
             description='Default IP address for UXA Signal Analyzer.')


class plugN9020B(plugs.BasePlug):

    """
    Class instrument to control N9020B MXA Signal Analyzer
    """
    @conf.inject_positional_args
    def __init__(self, mxa_sig_analyzer_address):
        rm = pyvisa.ResourceManager('@py')
        self.instrument = rm.open_resource(mxa_sig_analyzer_address)
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