import os
import json
from block import Block

def sync():
    node_blocks = []
    #We're assuming that the folder and at least initial block exists
    chaindata_dir = 'chaindata'
    if os.path.exists(chaindata_dir):
        for filename in os.listdir(chaindata_dir):
            if filename.endswith('.json'): #.DS_Store sometimes screws things up
                filepath = '%s/%s' % (chaindata_dir, filename)
                with open(filepath, 'r') as block_file:
                    block_info = json.load(block_file)
                    block_object = Block(block_info) #since we can init a Block object with just a dict
                    node_blocks.append(block_object)
    return node_blocks