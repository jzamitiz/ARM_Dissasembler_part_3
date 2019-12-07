# Slide 44
# The ALU takes in lists from disassembler to use as reference for choosing which operations to perform


class ALU:

    def __init__(self, R, preALUBuff, postALUBuff, opcodeStr, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.opcodeStr = opcodeStr
        self.postALUBuff = postALUBuff
        self.R = R
        self.preALUBuff = preALUBuff  # formatted as [InstrIndex, InstrIndex]

    def run(self):
        if self.preALUBuff[0] != -1:

            i = self.preALUBuff[0]  # Sets i to 1st instruction index

            # print("opcodeStr: " + self.opcodeStr[i] + "\t" + "Instruction Index: " + str(i))
            # print("Before -> preALUBuff: [" + str(self.preALUBuff[0]) + ", " + str(self.preALUBuff[1]) + "]")

            # R-TYPE
            if self.opcodeStr[i] == "ADD":
                self.postALUBuff = [self.R[self.arg1[i]] + self.R[self.arg2[i]], i]

            elif self.opcodeStr[i] == "SUB":
                self.postALUBuff = [self.R[self.arg1[i]] - self.R[self.arg2[i]], i]

            elif self.opcodeStr[i] == "AND":
                self.postALUBuff = [self.R[self.arg1[i]] & self.R[self.arg2[i]], i]

            elif self.opcodeStr[i] == "ORR":
                self.postALUBuff = [self.R[self.arg1[i]] | self.R[self.arg2[i]], i]

            elif self.opcodeStr[i] == "LSR":
                self.postALUBuff = [self.R[self.arg1[i]] % (1 << 32) >> self.R[self.arg2[i]], i]

            elif self.opcodeStr[i] == "LSL":
                self.postALUBuff = [self.R[self.arg1[i]] << self.R[self.arg2[i]], i]

            elif self.opcodeStr[i] == "ASR":
                self.postALUBuff = [self.R[self.arg1[i]] >> self.R[self.arg2[i]], i]

            elif self.opcodeStr == "EOR":
                self.postALUBuff = [self.R[self.arg1[i]] ^ self.R[self.arg2[i]], i]

            elif self.opcodeStr == "ADDI":
                self.postALUBuff = [self.R[self.arg1[i]] + self.arg3, i]

            elif self.opcodeStr == "SUBI":
                self.postALUBuff = [self.R[self.arg1[i]] - self.arg3, i]

            self.preALUBuff[0] = -1

        if self.preALUBuff[1] != -1:
            self.preALUBuff[0] = self.preALUBuff[1]
            self.preALUBuff[1] = -1

        # print("postALUBuffer: " + str(self.postALUBuff))
        # print("After -> preALUBuff: [" + str(self.preALUBuff[0]) + ", " + str(self.preALUBuff[1]) + "]")
        # print("\n")
