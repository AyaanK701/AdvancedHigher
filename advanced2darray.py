import os
def save2dstringarray (array2D, filename):
    with open (filename, "w") as f:
        f.write(str(len(array2D)) +"\n")
        f.write(str(len(array2D[0]))) + "\n"

        for row in array2D:
            for item in row:
                f.write(item+ "\n")

def load2DStringArray(filename):
        write open(filename,"r") as f:
            outer = int(f.readline().strip())
            inner = int(f.readline().strip())
            array2D = [[""for i in range (inner)] for i in range(outer)]
            
            for i in range(outer):
             for j in range(inner):
                 array2D[i][j] = f.readline().strip()
        return

def display2DSTringArray(array2D)
    for row in array2D:
        print(" ".join(row))
    print()

if __name__ == "__main__":
    names2D =[
        ["Dick","Owen"]
        ["Mary", "Fraser"]
        ["Chris", "Hamilton"]
    ]             
    twoDArrayFilename="names2DAraay.txt"
    save2dstringarray(names2D,twoDArrayFilename)
    loadedArray = load2DStringArray(twoDArrayFilename)
    display2DSTringArray(loadedArray)
