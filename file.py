import argparse 
from fileReader.check import *

def main():
    # Initializing Parser 
    parser = argparse.ArgumentParser(description ='file based') 
    # Adding Argument
    parser.add_argument("-l", "--fileWithLocation", type= str, nargs = 1, 
                        metavar = "location", default = '', help = "file location")
    args = parser.parse_args()
    var = fileReader(args.fileWithLocation[0])
if __name__ == "__main__":
    main()