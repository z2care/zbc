import datetime as date
import hashlib
import json
import os

class Block(object):
    def __init__(self, dictionary):
        '''
            We're looking for index, timestamp, data, prev_hash, nonce
        '''
        for k, v in dictionary.items():
            setattr(self, k, v)
        if not hasattr(self, 'hash'): #in creating the first block, needs to be removed in future
            self.hash = self.create_self_hash()

    def __dict__(self):
        info = {}
        info['index'] = str(self.index)
        info['timestamp'] = str(self.timestamp)
        info['prev_hash'] = str(self.prev_hash)
        info['hash'] = str(self.hash)
        info['data'] = str(self.data)
        return info

    def __str__(self):
        return "Block<prev_hash: %s,hash: %s>" % (self.prev_hash, self.hash)

    def header_string(self):
        return str(self.index) + self.prev_hash + self.data + str(self.timestamp) + str(self.nonce)

    def create_self_hash(self):
        sha = hashlib.sha256()
        sha.update(self.header_string())
        return sha.hexdigest()

    def self_save(self):
        chaindata_dir = 'chaindata'
        index_string = str(self.index).zfill(6) #front of zeros so they stay in numerical order
        filename = '%s/%s.json' % (chaindata_dir, index_string)
        with open(filename, 'w') as block_file:
            json.dump(self.__dict__(), block_file)


def create_first_block():
    # index zero and arbitrary previous hash
    block_data = {}
    block_data['index'] = 0
    block_data['timestamp'] = date.datetime.now()
    block_data['data'] = 'First block data'
    block_data['prev_hash'] = None
    block = Block(block_data)
    return block

#check if chaindata folder exists.
chaindata_dir = 'chaindata'
if not os.path.exists(chaindata_dir):
    #make chaindata dir
    os.mkdir(chaindata_dir)
    #check if dir is empty from just creation, or empty before
if os.listdir(chaindata_dir) == []:
    #create first block
    first_block = create_first_block()
    first_block.self_save()
