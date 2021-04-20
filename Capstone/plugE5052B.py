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


class plugE5052B(plugs.BasePlug):

    """
    Class instrument to control E5052B Signal Generator
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

    def setPowerDelay(self, num):
        """
        Sets the power delay to num in seconds. 
        """
        return (self.write(':SOURce:VOLTage:POWer:DELay %G' % (num)))

    def getPowerDelay(self):
        """
        Gets the power delay to num in seconds. 
        """
        return (self.write(':SOURce:VOLTage:POWer:DELay?'))

    def setVoltagePowerAmplitude(self, num):
        """
        This command sets fixed voltage power value at voltage control sweep.
        num must be between 0 and 16
        """
        return self.write(':SOURce:VOLTage:POWer:LEVel:AMPLitude %G' % (num))

    def getVoltagePowerAmplitude(self):
        """
        This command gets fixed voltage power value at voltage control sweep.
        """
        return self.write(':SOURce:VOLTage:POWer:LEVel:AMPLitude?')

    def write(self, command):
        return self.instrument.write(command)
