from statzcw.stats import readDataSets, readDataFile
from sys import argv
import statzcw.stats





if __name__ == "__main__":
    z = readDataSets(argv[1:])
    print(z)
