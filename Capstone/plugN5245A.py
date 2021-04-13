import logging
import openhtf.plugs as plugs
from openhtf.util import conf
import time
try:
    import pyvisa
except ImportError:
    logging.error('Failed to import pyvisa, did you:\npip install pyvisa')
    raise

conf.declare('pna_net_analyzer_address', default_value='TCPIP::192.168.10.63::INSTR',
             description='Default IP address for PNA Network ANalyzer.')

class plugN5245A(plugs.BasePlug):
    """
    Class instrument to control N5245A PNA Network ANalyzer
    """
    @conf.inject_positional_args
    def __init__(self, pna_net_analyzer_address):
        rm = pyvisa.ResourceManager('@py')
        self.instrument = rm.open_resource(pna_net_analyzer_address)
        idn = self.instrument.query('*IDN?')
        print('Connected to', idn)  # We could probably use test info
    
    def close(self):
        """
        Disconnect.
        :return:
        """
        self.instrument.close()
            
    def reset(self):
        """ reset analyzer"""
        self.instrument.write('*RST')
        
    def preset(self):
        """ preset analyzer"""
        self.instrument.write('PRESet')
        
    def start_frequency(self):
        """ set start frequency in analyzer"""
        self.instrument.write('FREQuency:STARt %G MHZ' % (1.0))
        
    def power_on(self):
        """ turn on power: ON = 1 """            
        self.instrument.write(':OUTPut:STATe %d' % (1))
        
    def power_off(self):
        """ turn off power: OFF = 0 """
        self.instrument.write(':OUTPut:STATe %d' % (0))
        
    def power_limit(self):
        """ set power limit """
        self.instrument.write('POWer123456:LIMit %G' % (1.0))
        
    def read_current_frequency(self):
        """ 
        Choose any number between the min and max frequency limits of the analyzer.
        It will accept min or max instead of a numeric parameter.
        """
        return float (self.instrument.query_ascii_values('FREQuency:CENTer? %s' % ('MAXimum')))
        
    
    """ 
    S-parameter: S11 and S21
    - set the start frequency
    - set stop frequency
    - set the instrument to measure S11 and S21 
    """
         
    def set_start_freq(self):
        """ set start frequency to 88 MHZ"""
        self.instrument.write('FREQuency:STARt %G MHZ' % (88.0))
        
    def set_stop_freq(self):
        """ set stop frequency to 108 MHZ"""
        self.instrument.write('FREQuency:STOP %G MHZ' % (108.0))
        
    def measure_S11(self):
        """set the instrument to measure S11 port"""
        self.instrument.write(':CALCulate1:PARameter:DEFine "%s",%s' % ('MyMeas', 'S11'))
        
    def measure_S11(self):
        """set the instrument to measure S21 port"""
        self.instrument.write(':CALCulate1:PARameter:DEFine "%s",%s' % ('MyMeasu', 'S21'))

    def write(self, command):
        return self.write(command)
