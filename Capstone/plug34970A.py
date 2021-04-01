import logging
import openhtf.plugs as plugs
from openhtf.util import conf
import time
try:
    import pyvisa
except ImportError:
    logging.error('Failed to import pyvisa, did you:\npip install pyvisa')
    raise

conf.declare('data_logger_address', default_value='TCPIP::192.168.10.63::INSTR',
             description='Default IP address for Data Logger.')

class plug34970A(plugs.BasePlug):
	
	"""
    Class instrument to control 34970A Temp and Voltage Data Logger
    """
    @conf.inject_positional_args
    def __init__(self, data_logger_address):
        rm = pyvisa.ResourceManager('@py')
        self.instrument = rm.open_resource(data_logger_address)
        idn = self.instrument.query('*IDN?')
        print('Connected to', idn)  # We could probably use test info
    
    def close(self):
        """
        Disconnect.
        :return:
        """
        self.instrument.close()
			
	def reset(self):
		""" reset """
		self.instrument.write('*RST')
		
	def preset(self):
		""" preset """
		self.instrument.write('PRESet')
		
	
	def conf_temperature(self):
		""" configure temperatur with channel 101, 102, 103"""
		self.instrument.write(':CONFigure:TEMPerature %s,%s,(%s)' % ('TCouple', 'J', '@101,102,103'))
	
		
	def scan_temp_channel(self):
		""" scan channels"""
		self.instrument.write(':ROUTe:SCAN (%s)' % ('@101,102,103'))	
		
	def conf_voltage(self):
		""" configure temperatur with channel 105, 106, 107"""
		self.instrument.write(':CONFigure:VOLTage:DC (%s)' % ('@105,106,107'))

	
	def scan_voltage_channel(self):
		""" scan voltage channel"""
		self.instrument.write(':ROUTe:SCAN (%s)' % ('@105,106,107'))
		
	def init(self):
		"""starts measurement """
		self.instrument.write(':INITiate')
		
	def fetch(self):
		"""Fetches data from memory after the scan list was completed """
		readings = self.instrument.query(':FETCh?')

	def write(self, command):
        return self.write(command)