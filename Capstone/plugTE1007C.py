class plugTE1007C:
    """
    Class for the Temperature Chamber plug 
    """

    def __init__(self, address):
        print('Trying to connect to', address)
        try:
            self.instrument = pyvisa.ResourceManager().open_resource(address)
            idn = self.instrument.query('*IDN?')
            print('Connected to\n', idn)
        except:
            raise ("Couldn't connect to instrument " + address)
    
    
    def write(self, command):
        """ Handle all writes to instrument """
        self.instrument.write(command)