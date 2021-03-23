import visa
import time 

class plugU2049XA:
    """
    Class instrument to control U2049XA LAN Dynamic Wide Range Power Sensor
    """

    def __init__(self, address):
        print('Trying to connect to', address)
        try:
            self.instrument = pyvisa.ResourceManager().open_resource(address)
            self.idn = self.instrument.query('*IDN?')
            print('Connected to\n', idn)

            #set output mode
            self.instrument.write(':FORMat:READings:DATA %s' % ('ASCii'))
        except:
            raise ("Couldn't connect to instrument " + address)

    def close(self):
        """
        Disconnect.
        :return:
        """
        self.instrument.close()

    def check_identity(): 
        """
        Returns the identity of the instrument
        """
        if not self.idn:
            self.idn = self.instrument.query('*IDN?')
        
        return self.idn
    SCPI_U2040.write('*RST')
SCPI_U2040.write(':CALibration:AUTO %s' % ('ON'))
SCPI_U2040.write(':CALibration:AUTO %s' % ('OFF'))
SCPI_U2040.write(':CALibration:AUTO %s' % ('ONCE'))
SCPI_U2040.write(':SENSe:FREQuency:FIXed %s' % ('MIN'))
SCPI_U2040.write(':SENSe:FREQuency:FIXed %s' % ('MAX'))
SCPI_U2040.write(':SENSe:FREQuency:FIXed %s' % ('DEF'))
temp_values = SCPI_U2040.query_binary_values(':SYSTem:HELP:HEADers?','s',False)
headers = temp_values[0].decode().split('\n')
    def reset():
        return self.instrument.write('*RST')

    def calibrate(mode):
        if (mode is 'ONCE') or (mode is 'ON') or (mode is 'OFF'):
            return self.write(':CALibration:AUTO %s' % (mode))
        else:
            print("ERROR: Incorrect mode, use 'ONCE', 'ON', or 'OFF'")
            return None

    def get_measurement_type():
        return
    
    def set_frequency():
        return

    def read_frequency():
        return

    def read_power(mode = ""):
        """
        Reads the power, 3 modes are available
        default, ratio, and difference
        """
        if(mode == ""):
            return self.instrument.query_ascii_values(':READ:SCALar:POWer:AC:RELative?')
        elif(mode == "RAT"):
            return self.instrument.query_ascii_values(':READ:SCALar:POWer:AC:RATio:RELative?')
        elif(mode == "DIFF"):
            return self.instrument.query_ascii_values(':READ:SCALar:POWer:AC:DIFFerence:RELative?')
        else:
            print('Error, incorrect parameter, available modes are: RAT,DIFF, and ""')
    
    def measure_power(mode = ""):
        """
        Measueres the power, 3 modes are available
        default, ratio, and difference
        """
        if(mode == ""):
            return self.instrument.query_ascii_values(':MEASure:SCALar:POWer:AC:RELative?')
        elif(mode == "RAT"):
            return self.instrument.query_ascii_values(':MEASure:SCALar:POWer:AC:RATio:RELative?')
        elif(mode == "DIFF"):
            return self.instrument.query_ascii_values(':MEASure:SCALar:POWer:AC:DIFFerence:RELative?')
        else:
            print('Error, incorrect parameter, available modes are: RAT,DIFF, and ""')

    def set_impedence(impedance = "HIGH"):
        """
        Sets the impedence as either high 100 kohms or low 50 ohms
        """
        self.instrument.write(':INPut:TRIGger:IMPedance %s' % (impedance))
    

