

import os

def main():
    print(">>>>>Always Running<<<<<")
    with open(os.path.join("rough","test.txt"),"w+") as f:
        f.write("This is a test file.")


if __name__=="__main__":
    main()