import disassembler
import simulator
import sim

mydis = disassembler.Disassembler()
output = {}
output = mydis.run()    #returns all dissasembler lists to output
mydis.print()           #prints dissasembler


mysimulator = simulator.Simulator(**output)   #passes all dissasembler return values to constructor of Simulator()
mysimulator.run()

mysim = sim.simClass(**output)
mysim.run()

