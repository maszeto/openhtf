import logging
import openhtf.plugs as plugs
from openhtf.util import conf
import time
try:
    import pyvisa
except ImportError:
    logging.error('Failed to import pyvisa, did you:\npip install pyvisa')
    raise

conf.declare('power_supply_address_1', default_value='TCPIP::192.168.10.63::INSTR',
             description='Default IP address for Triple Output Power Supply.')


class plugMSOX3104(plugs.BasePlug):

    """
    Class instrument to control E36300 Series Triple Output Power Supply
    """
    @conf.inject_positional_args
    def __init__(self, power_supply_address):
        # used to store how many captures have been taken, so images are not overwritten
        capture_count = 0
        rm = pyvisa.ResourceManager('@py')
        self.instrument = rm.open_resource(power_supply_address_1)
        idn = self.instrument.query('*IDN?')
        print('Connected to', idn)  # We could probably use test info

    def close(self):
        """
        Disconnect
        :return:
        """
        self.instrument.close()

    def get_VRMS(self):
        """
        Returns the voltage root mean squared value
        """
        return(self.write(':MEASure:VRMS'))

    def get_current(self):
        """
        Returns current measurement
        """
        return(self.write(':MEASure:STATistics %s' % ('CURRent')))

    def get_stats(self):
        """
        Returns statistics
        Args:
            None

        Returns:
            stats (Dictionary): Dictionary of the format {"min":val, "max":val, "mean":val, "stdDev":val}
        """
        mean = self.write(':MEASure:STATistics %s' % ('MEAN'))
        minVal = self.write(':MEASure:STATistics %s' % ('MINimum'))
        maxVal = self.write(':MEASure:STATistics %s' % ('MAXimum'))
        stdDev = self.write(':MEASure:STATistics %s' % ('STDDev'))

        return {"min": minVal, "max": maxVal, "mean": mean, "stdDev": stdDev}

    def capture_display(self, destination=None, fileName=None, text=None):
        """
        This function captures the current oscilloscope display and saves it at the current working directory or
        specified location

        Args:
            Destination (string): Path to where to place file
            fileName (string): file name
            text (string): capture caption 

        Returns:
            None
        """

        # add an annotation if specified
        if text is not None:
            self.write(':DISPlay:ANNotation1 %d' % (1))
            self.write(':DISPlay:ANNotation1:TEXT "%s"' % (text))

        # get bytes
        displayData = self.query_binary_values(
            ':DISPlay:DATA? %s,%s' % ('PNG', 'COLor'), 'B', False)

        filePath = 'Capture' + \
            int(self.capture_count) if destination is None else destination + \
            'Capture' + int(self.capture_count)

        f = open(filePath, 'wb')
        f.write(displayData)

    def clear_display(self):
        """
        Clears the display
        """
        return self.write(':DISPlay:CLEar')

    # TODO add try except and handle error
    def query(self, command):
        # """Handle all queries to instrument"""
        return self.instrument.query(command)

    # TODO add try except and handle error
    def write(self, command):
        # """ Custom write command """
        return self.instrument.write(command)
