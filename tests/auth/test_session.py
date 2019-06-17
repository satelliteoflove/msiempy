import unittest
import msiempy.session

class T(unittest.TestCase):

    def test(self):

        session=msiempy.session.NitroSession()
        
        tz=session.request('time_zones')
        for t in tz :
            if not 'offset' in t:
                self.fail("Timezone object from the SIEM doesn't represent a offset attribute")

