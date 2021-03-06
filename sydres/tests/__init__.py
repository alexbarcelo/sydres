import unittest


def main():
    from .test_signature import TestSydresClient
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSydresClient)
    runner = unittest.TextTestRunner(verbosity=1 + sys.argv.count('-v'))
    raise SystemExit(not runner.run(suite).wasSuccessful())


if __name__ == '__main__':
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    main()
