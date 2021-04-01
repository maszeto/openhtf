import logging
import openhtf.plugs as plugs
from openhtf.util import conf
import time
try:
    import pyvisa
except ImportError:
    logging.error('Failed to import pyvisa, did you:\npip install pyvisa')
    raise

conf.declare('average_meter_address', default_value='TCPIP::192.168.10.63::INSTR',
             description='Default IP address for Power Meter - Average - Dual Channel.')

class plugN1914A(plugs.BasePlug):

    """
    Class instrument to control N1914A Power Meter - Average - Dual Channel
    """
    @conf.inject_positional_args
    def __init__(self, average_meter_address):
        rm = pyvisa.ResourceManager('@py')
        self.instrument = rm.open_resource(average_meter_address)
        idn = self.instrument.query('*IDN?')
        print('Connected to', idn)  # We could probably use test info

    def close(self):
        """
        Disconnect.
        :return:
        """
        self.instrument.close()

    def getPowerRelativeAC(self):
        """
        Gets the relative AC power
        """
        return self.instrument.query_ascii_values(':READ:SCALar:POWer:AC:RELative?')

    def calculateGainMagnitude(self, mode="DEF"):
        """
        Calculates the max gain
        mode is "MIN" for minimum or "MAX" for maximum
        """
        if(mode is "MAX"):
            return self.write(':CALCulate:GAIN:MAGNitude %s' % ('MAXimum'))

        elif(mode is "MIN"):
            return self.write(':CALCulate:GAIN:MAGNitude %s' % ('MINimum'))
        
        elif(mode is "DEF"):
            return self.write(':CALCulate:GAIN:MAGNitude %s' % ('DEFault'))
        
        else:
            print("Invalid mode " + mode + " given, using default mode.")
            return self.write(':CALCulate:GAIN:MAGNitude %s' % ('DEFault'))

    def write(self, command):
        return self.instrument.write(command)