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
            idn = self.instrument.query('*IDN?')
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
    

