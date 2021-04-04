# Main file from which the whole script will run
import unittest
from Models.English.FbLogin import GoogleSearch
from Models.English.CheckOut import CheckOut

# Set testcases
tc1 = unittest.TestLoader().loadTestsFromTestCase(GoogleSearch)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CheckOut)

masterTestSuite = unittest.TestSuite([tc1, tc2])
# Run testCases Suite
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)
