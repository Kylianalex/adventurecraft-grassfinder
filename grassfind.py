#!/usr/bin/env python
import jnbt, os

if __name__ == "__main__":
    choice = input ("1 | generate file\n2 | check a generated file\nchoice : ")
    if choice == "1":
        path = input("save path : ")
        world = jnbt.World(path)
        overworld = world[jnbt.DIM_OVERWORLD]
        f = open(os.path.basename(os.path.normpath(path)) + ".txt", "w")
        f.write(path + "\n")
        for block in overworld.iterBlocks():
            #print(block.getID())
            if block.getID() == 31:
                f.write(str(block.x) + " " + str(block.y) + " " + str(block.z) + "\n")
        print("the coordinate of all grass blocks are in " + os.path.basename(os.path.normpath(path)) + ".txt")
    elif choice == "2":
        path = input("generated file path : ")
        f_ = open(path, "r")
        f = f_.read().split("\n")
        f_.close()
        world = jnbt.World(f[0])
        overworld = world[jnbt.DIM_OVERWORLD]
        blocks = f[1::]
        f = open(os.path.basename(os.path.normpath(path)), "w")
        f.write(path + "\n")
        for block in blocks:
            if block:
                x, y, z = block.split(" ")
                b = overworld.getBlock(int(x), int(y), int(z))
                if b.getID() == 31:
                    f.write(x + " " + y + " " + z + "\n")
        print("the coordinate of all grass blocks are in " + os.path.basename(os.path.normpath(path)))
