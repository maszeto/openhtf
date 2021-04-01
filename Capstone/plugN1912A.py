import logging
import openhtf.plugs as plugs
from openhtf.util import conf
import time
try:
    import pyvisa
except ImportError:
    logging.error('Failed to import pyvisa, did you:\npip install pyvisa')
    raise

conf.declare('p_series_power_meter_address', default_value='TCPIP::192.168.10.63::INSTR',
             description='Default IP address for Power Meter - P Series - Dual Channel.')

class plugN1912A(plugs.BasePlug):

    """
    Class instrument to control N1912A Power Meter - P Series - Dual Channel
    """
    @conf.inject_positional_args
    def __init__(self, p_series_power_meter_address):
        rm = pyvisa.ResourceManager('@py')
        self.instrument = rm.open_resource(p_series_power_meter_address)
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