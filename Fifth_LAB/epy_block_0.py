"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy
from gnuradio import gr

class Compara(gr.sync_block):
    """
    docstring for block Compara
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="Compara",
            in_sig=[numpy.float32, numpy.float32],
            out_sig=[numpy.float32, ])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out = output_items[0]
        # <+signal processing here+>
        for i in range(len(in0)):
                if in0[i] > in1[i]:
                        out[i] = 1
                else:
                        out[i] = 0
        return len(output_items[0])
