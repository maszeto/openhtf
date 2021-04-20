import logging
import openhtf.plugs as plugs
from openhtf.util import conf
import time
try:
    import pyvisa
except ImportError:
    logging.error('Failed to import pyvisa, did you:\npip install pyvisa')
    raise

conf.declare('power_supply_address', default_value='TCPIP::192.168.10.63::INSTR',
             description='Default IP address for Power Supply.')

class plugE36313A(plugs.BasePlug):

    """
    Class instrument to control E36300 Series Triple Output Power Supply
    """
    @conf.inject_positional_args
    def __init__(self, power_supply_address):
        rm = pyvisa.ResourceManager('@py')
        self.instrument = rm.open_resource(power_supply_address)
        idn = self.instrument.query('*IDN?')
        print('Connected to', idn)  # We could probably use test info
    
    def close(self):
        """
        Disconnect.
        :return:
        """
        self.instrument.close()

    # Set the voltage of the instrument
    def set_voltage(self, source, volts):
        # Check if the voltage is within the limits
        if(self.check_voltage(source, volts)):
            # Set the voltage to the value given by the user
            self.write(':INSTrument:NSELect %d' % (source))
            self.write('VOLT ' + str(volts) + ', (@' + str(source) + ')')
            self.write('OUTP ON, (@' +  str(source) + ')')
            # Set the current to keep the power level consistant: MIGHT NOT NEED
            # self.write('CURR ' + str(self.powerLimit/volts) + ', (@' + str(source) + ')')     

    # Set the current of the instrument
    def set_current(self, source, amps):
        if(self.check_current(source, amps)):
            # Set the current to the value given by the user
            self.write('CURR ' + str(amps) + ', (@' + str(source) + ')')
            # Set the voltage to keep the power level consistant: MIGHT NOT NEED
            # self.write('VOLT ' + str(self.powerLimit/amps) + ', (@' + str(source) + ')')    


    # Completes a step function on our power supply
    def step_voltage(self, source, startVal, endVal, step, seconds):
        if(self.check_voltage(source, startVal) and self.check_voltage(source, endVal)):
            if(statVal < endVal):
                # Continues to change the voltage until we meet or exceed our threshold
                while(startVal <= endVal):
                    # Set the voltage and then change our current value
                    self.set_voltage(source, startVal)
                    
                    # Wait for a duration of time(seconds) for the next change to occur
                    time.sleep(seconds)

                    # Increment our current value
                    startVal += step

            else:
                # Continues to change the voltage until we meet or exceed our threshold
                while(startVal >= endVal):
                    # Set the voltage and then change our current value
                    self.set_voltage(source, startVal)
                    
                    # Wait for a duration of time(seconds) for the next change to occur
                    time.sleep(seconds)

                    # Increment our current value
                    startVal -= step


    # Ensure the voltage given is within the bounds of the power supply
    def check_voltage(self, source, enteredVoltage):
        """
        Source1: 0 to 6 volts
        Source2: 0 to 25 volts
        Source3: 0 to 25 volts
        """
        if(source < 1 or source > 3):
            print(f"Incorrect source: {source} is not within 1-3")
            return False
        elif(source == 1 and (enteredVoltage < 0 or enteredVoltage > 6)):
            print(f"{enteredVoltage} Volts are not within the bounds")
            return False
        elif(enteredVoltage < 0 or enteredVoltage > 25):
            print(f"{enteredVoltage} Volts are not within the bounds")
            return False
        else:
            return True


    # Ensure the current given is within the bounds of the power supply
    def check_current(self, source, enteredAmps):
        """
        Source1: 0 to 10 amps
        Source2: 0 to 2 amps
        Source3: 0 to 2 amps
        """
        if(source < 1 or source > 3):
            print(f"Incorrect source: {source} is not within 1-3")
            return False
        elif(source == 1 and (enteredAmps < 0 or enteredAmps > 10)):
            print(f"{enteredAmps} Amps are not within the bounds")
            return False
        elif(enteredAmps < 0 or enteredAmps > 2):
            print(f"{enteredAmps} Amps are not within the bounds")
            return False
        else:
            return True

    # Return the current displayed on the PS
    def read_voltage(self, source):
        return (self.query(':MEASure:SCALar:VOLTage:DC? (@' + str(source) + ')'))

    # Return the current displayed on the PS
    def read_current(self, source):
        return (self.query(':MEASure:SCALar:CURRent:DC? (@' + str(source) + ')'))

    # TODO add try except and handle error
    def query(self, command):
        # """Handle all queries to instrument"""
        return self.instrument.query(command)

    # TODO add try except and handle error
    def write(self, command):
        # """ Custom write command """
        return self.instrument.write(command)