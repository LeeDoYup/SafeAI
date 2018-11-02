from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath('../safeai')))

import tensorflow as tf
from safeai.models.matmul import matmul_example

def main():
    test = tf.ones((2,2))
    halloween = matmul_example(test, test, name='halloween')
    with tf.Session() as sess:
        print(sess.run(halloween))
        print(halloween.name)

if __name__ == '__main__':
    main()