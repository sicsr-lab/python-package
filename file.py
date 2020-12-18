import argparse 
from .extract import *

def main():
    # Initializing Parser 
    parser = argparse.ArgumentParser(description ='file based') 
    # Adding Argument
    parser.add_argument("-l", "--fileWithLocation", type= str, nargs = 1, 
                        metavar = "location", default = '', help = "file location")
    parser.add_argument("-p", "--punctuation", type= str, nargs = 1, 
                        metavar = "punctuation", default = 'n', help = "punctuation")
    args = parser.parse_args()
    if (args.punctuation[0].upper() == 'Y') or (args.punctuation[0].upper() == 'YES'):
        var = punctuation(args.fileWithLocation[0])
    else:
        var = fileReader(args.fileWithLocation[0])

if __name__ == "__main__":
    main()
