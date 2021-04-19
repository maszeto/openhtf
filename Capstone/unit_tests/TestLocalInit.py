import sys
sys.path.append('../')

import unittest
from plug34461A import *
from plug346CK01 import *
from plug34970A import *
from plugDSOS204A import *
from plugE36313A import *
from plugE5052B import *
from plugE8257D import *
from plugE8267D import *
from plugMSOX3104 import *
from plugN1912A import *
from plugN1914A import *
from plugN5183B import *
from plugN5245A import *
from plugN9000B import *
from plugN9020B import *
from plugN9040B import *
from plugU2049XA import *
from plugU7227F import *





class TestPlug34461A(unittest.TestCase):

    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))

class TestPlug346CK01(unittest.TestCase):
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))
class TestPlug34970A(unittest.TestCase):
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))
class TestPlugDSOS204A(unittest.TestCase):
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))
class TestPlugE36313A(unittest.TestCase):
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))
class TestPlugE5052B(unittest.TestCase):
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))
class TestPlugE8257D(unittest.TestCase):
    
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))

class TestPlugE8267D(unittest.TestCase):
    
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))

class TestPlugMSOX3104(unittest.TestCase):
    
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))

class TestPlugN1912A(unittest.TestCase):
    
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))

class TestPlugN1914A(unittest.TestCase):
    
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))

class TestPlugN5183B(unittest.TestCase):
        
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))

class TestPlugN5245A(unittest.TestCase):
        
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))

class TestPlugN9000B(unittest.TestCase):
        
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))

class TestPlugN9020B(unittest.TestCase):
        
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))

class TestPlugN9040B(unittest.TestCase):
        
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))

class TestPlugU2049XA(unittest.TestCase):
        
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))

class TestPlugU7227F(unittest.TestCase):
        
    def setUp(self):
        self.curPlug = None
        self.testIP = '127.0.0.1'

    def tearDown(self):
        pass

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have an instrument on the ip.
        """
        try:
            self.curPlug = plug34461A(dmm_address = self.testIP)

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_INV_RSRC_NAME" in  str(e))

    def test_init_ip(self):
        """
        Our __init__ method should fail, since we do not have access to the instruments locally.
        """
        try:
            self.curPlug = plug34461A()

        except Exception as e:
            print(e)
            self.assertTrue("VI_ERROR_RSRC_NFOUND" in  str(e))



if __name__ == '__main__':
    unittest.main()