import pyvisa
import time


class plugN9000B:

    """
    Class instrument to control N9000B Signal Analyzer
    """

    def __init__(self, address):
        print('Trying to connect to', address)
        try:
            self.instrument = pyvisa.ResourceManager().open_resource(address)
            idn = self.instrument.query('*IDN?')
            print('Connected to\n', idn)
        except:
            raise ("Couldn't connect to instrument " + address)
    
    def close(self):
        """
        Disconnect.
        :return:
        """
        self.instrument.close()

    # TODO: Set frequency on sig analyzer
    def set_frequency(self, type, hertz):
        # 
        if(self.check_frequency(hertz)):
            if(type == "Center"):
                self.write('FREQuency:CENTer ' + str(hertz))
            elif(type == "Step"):
                self.write('FREQuency:SPAN ' + str(hertz))

    # TODO: Set marker to frequency on sig analyzer
    def set_marker(self, hertz):
        if(self.check_frequency(hertz)):
            self.write('CALCulate:MARKer:X ' + str(hertz))

    # TODO: Move marker to frequency on sig analyzer
    def move_marker(self, hertz):
        if(self.check_frequency(hertz)):
            self.write('CALCulate:MARKer:X ' + str(hertz))

    # TODO: Read vertical axis on sig analyzer
    def read_power(self):
        self.write('CALCulate:MARKer:Y')

    # TODO: Check if frequency is within the bounds
    def check_frequency(self, hertz):
        if(hertz < (9*10**3) or hertz > (3*10**9)):
            return False
        else:
            return True

    def trace(self, method):
    
        if(method == 'WRIT'):
            return self.write(':TRACe:MONitor:TYPE %s' % ('WRITe'))
        elif(method == 'AVER'):
            return self.write(':TRACe:MONitor:TYPE %s' % ('AVERage'))
        elif(method == 'MAXH'):
            return self.write(':TRACe:MONitor:TYPE %s' % ('MAXHold'))
        elif(method == 'MINH'):
            return self.write(':TRACe:MONitor:TYPE %s' % ('MINHold'))
        else:
            print("Invalid method, please use one of the following\nWRIT:\nAVER:\nMAXH:\nMINH:\n")


    def write(self, command):
        return self.instrument.write(command)
