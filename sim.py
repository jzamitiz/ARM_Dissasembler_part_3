from helpers import SetUp
import cache
import writeBack
import issue
import alu
import memory
import fetch

global_cycle = 0

class simClass:
    def __init__(self, opcode, dataval, address, numInstructs, arg1, arg2, arg3, opcodeStr, arg1Str, arg2Str,
                 arg3Str, destReg, src1Reg, src2Reg):
        #self.instruction = instructions
        self.opcode = opcode
        self.opcodeStr = opcodeStr
        self.dataval = dataval
        self.address = address
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str
        self.numInstructs = numInstructs
        self.destReg = destReg
        self.src1Reg = src1Reg
        self.src2Reg = src2Reg
        self.PC = 96
        self.cycle = 1
        self.cycleList = [0]
        self.R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.postMemBuff = [-1, -1]     # first number is value, second is index
        self.postALUBuff = [-1, -1]     # first number is value, second is index
        self.preMemBuff = [-1, -1]      # first number is index, second is index
        self.preALUBuff = [-1, -1]      # first number is index, second is index
        self.preIssueBuff = [-1, -1, -1, -1]

        "functional units"
        #self.WB = writeBack.WriteBack(self.R, self.postMemBuff, self.postALUBuff, destReg)
        #self.cache = cache.Cache(numInstructions, instructions, dataval, address)
        self.ALU = alu.ALU(self.R, self.preALUBuff, self.postALUBuff, opcodeStr, arg1, arg2, arg3)
        #self.MEM = memory.Memory(self.R, self.postMemBuff, self.preMemBuff, opcodeStr, arg1, arg2, arg3, dataval,
        #                         address, self.numInstructions, self.cache, self.cycleList)
        #self.issue = issue.Issue(instructions, opcodeStr, dataval, address, arg1, arg2, arg3, self.numInstructions,
        #                        destReg, src1Reg, src2Reg, self.R, self.preIssueBuff, self.preMemBuff,
        #                        self.postMemBuff,
        #                         self.preALUBuff, self.postALUBuff)
        #self.fetch = fetch.Fetch(instructions, opcodeStr, dataval, address, arg1, arg2, arg3, self.numInstructions,
        #                        destReg, src1Reg, src2Reg, self.R, self.preIssueBuff, self.preMemBuff,
        #                         self.postMemBuff,
        #                         self.preALUBuff, self.postALUBuff, self.PC, self.cache)

        #self.outputFileName = SetUp.get_output_filename()

    def run(self):
        for i in range(self.numInstructs):
            self.preALUBuff[0] = i
            self.ALU.run()

class sim:

    def __init__(self, opcode, dataval, address, arg1, arg2, arg3, numInstructs, opcodeStr, arg1Str, arg2Str, arg3Str, destReg, src1Reg, src2Reg):
        self.opcode = opcode
        self.dataval = dataval
        self.address = address
        self.numInstructs = numInstructs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.opcodeStr = opcodeStr
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str
        self.destReg = destReg
        self.src1Reg = src1Reg
        self.src2Reg = src2Reg


    def run(self):
        simi = simClass(self.opcode, self.dataval, self.address, self.arg1, self.arg2, self.arg3, self.numInstructs, self.opcodeStr, self.arg1Str, self.arg2Str, self.arg3Str, self.destReg, self.src1Reg, self.src2Reg)
