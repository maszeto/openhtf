import logging
import openhtf.plugs as plugs
from openhtf.util import conf
import time
try:
    import pyvisa
except ImportError:
    logging.error('Failed to import pyvisa, did you:\npip install pyvisa')
    raise

conf.declare('power_sensor_address', default_value='TCPIP::192.168.10.63::INSTR',
             description='Default IP address for Dynamic Range Power Sensor.')


class plugU2049XA:

    """
    Class instrument to control U2049XA LAN Wide Dyamic Range Power Sensor
    """
    @conf.inject_positional_args
    def __init__(self, power_sensor_address):
        rm = pyvisa.ResourceManager('@py')
        self.instrument = rm.open_resource(power_sensor_address)
        idn = self.instrument.query('*IDN?')
        print('Connected to', idn)  # We could probably use test info

    def close(self):
        """
        Disconnect.
        :return:
        """
        self.instrument.close()

    # Get the current power reading
    def read_power_instant(self, trace, percentage):
        if check_percentage(percentage):
            self.write(':TRACe' + str(trace) +
                       ':MEASurement:INSTant:REFerence? ' + str(percentage))

    # Read the power over a set duration

    def read_power_over_time(self, trace, pulse, mode):
        if check_power_constraints(trace, pulse):
            self.write(':TRACe' + str(trace) +
                       ':MEASurement:PULSe' + str(pulse) + ':' + mode + '?')

    # Changes the way the instrument will read the measurement
    def measurement_speed(self, trigger, sequence):
        self.write(':TRIGger' + str(trigger) + ':SEQuence' +
                   str(sequence) + ':IMMediate')

    # Check if the correct power constraint value was given
    def check_power_constraint(self, trace, pulse):
        if (trace < 1 or trace > 20) and (pulse < 1 or pulse > 20):
            return False
        else:
            return True

    # Check the percentage passed by read_power_instant
    def check_percentage(self, value):
        if (value < -25 or value > 125):
            return False
        else:
            return True

    def write(self, command):
        return self.write(command)
