#! /usr/bin/env python
'''
Tests wrapping module
'''

from dolfin import *
import numpy as np
from tests import double_sin_3d_test, \
                  double_sin_reaction_test, \
                  double_sin_test


def run_tests():
    print "Begining the tests:"
    print "Testing over sin..."
    double_sin_test.run()
    print "Testing over sin reaction..."
    double_sin_reaction_test.run()
    print "Testing over sin 3D..."
    double_sin_3d_test.run()
    print "Done."

if __name__ == "__main__":
    run()
