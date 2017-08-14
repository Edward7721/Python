import api_request
import unittest

class SimpleTest(unittest.TestCase):
    def testRest(self):
        self.assertEqual(api_request.getStatusCode("cat"), 200, 'Status is not OK')
     #TODO:
     #   def testLibCreated(self):
     #   def testSCVCreatedAndNotEmpty(self):
     #   def testNumberNodesInRequestAndNumberRowsInSVN
     #   etc
     #


if __name__ == '__main__':
    unittest.main()

