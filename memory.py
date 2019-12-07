from helpers import SetUp

class Memory:

    def __init__(self, R, postMemBuff, preMemBuff, opcodeStr, arg1, arg2, arg3, dataval, address, numInstructions, cache,
                 cycleList):
        self.R = R
        self.postMemBuff = postMemBuff
        self.preMemBuff = preMemBuff
        self.opcodeStr = opcodeStr
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.dataval = dataval
        self.address = address
        self.numInstructions = numInstructions
        self.cache = cache
        self.cycleList = cycleList

    def run(self):

        if self.preALUBuff[0] != -1:

            i = self.preALUBuff[0]

            isSW = 0





            if self.opcodeStr[i] == "LDUR":
                pass
                #TODO

            elif self.opcodeStr[i] == "STUR":
                pass
                #TODO