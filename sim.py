from helpers import SetUp
import cache
import writeBack
import issue
import alu
import memory
import fetch

global_cycle = 0


class simClass:
    def __init__(self, instructions, opcodes, opcodeStr, dataval, address, arg1, arg2, arg3, arg1Str, arg2Str,
                 arg3Str, numInstructions, destReg, src1Reg, src2Reg):
        self.instruction = instructions
        self.opcode = opcodes
        self.opcodeStr = opcodeStr
        self.dataval = dataval
        self.address = address
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str
        self.numInstructions = numInstructions
        self.destReg = destReg
        self.src1Reg = src1Reg
        self.src2Reg = src2Reg
        self.PC = 96
        self.cycle = 1
        self.cycleList = [0]
        self.R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.postMemBuff = [-1, -1]  # first number is value, second is index
        self.postALUBuff = [-1, -1]
        self.preMemBuff = [-1, -1]
        self.preALUBuff = [-1, -1]
        self.preIssueBuff = [-1, -1, -1, -1]

        "functional units"
        self.WB = writeBack.WriteBack(self.R, self.postMemBuff, self.postALUBuff, destReg)
        self.cache = cache.Cache(numInstructions, instructions, dataval, address)
        self.ALU = alu.ALU(self.R, self.postALUBuff, opcodeStr, arg1, arg2, arg3)
        self.MEM = memory.Memory(self.R, self.postMemBuff, self.preMemBuff, opcodeStr, arg1, arg2, arg3, dataval,
                                 address, self.numInstructions, self.cache, self.cycleList)
        self.issue = issue.Issue(instructions, opcodeStr, dataval, address, arg1, arg2, arg3, self.numInstructions,
                                 destReg, src1Reg, src2Reg, self.R, self.preIssueBuff, self.preMemBuff,
                                 self.postMemBuff,
                                 self.preALUBuff, self.postALUBuff)
        self.fetch = fetch.Fetch(instructions, opcodeStr, dataval, address, arg1, arg2, arg3, self.numInstructions,
                                 destReg, src1Reg, src2Reg, self.R, self.preIssueBuff, self.preMemBuff,
                                 self.postMemBuff,
                                 self.preALUBuff, self.postALUBuff, self.PC, self.cache)

        self.outputFileName = SetUp.get_output_filename()