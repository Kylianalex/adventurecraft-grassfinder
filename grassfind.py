#!/usr/bin/env python
import jnbt, os

def create_file(path):
    world = jnbt.World(path)
    overworld = world[jnbt.DIM_OVERWORLD]
    f = open(os.path.basename(os.path.normpath(path)) + ".txt", "w")
    f.write(path + "\n")
    i = 0
    for block in overworld.iterBlocks():
        #print(block.getID())
        if block.getID() == 31:
            f.write(str(block.x) + " " + str(block.y) + " " + str(block.z) + "\n")
            i += 1
    return i

def verify_file(path):
    f_ = open(path, "r")
    f = f_.read().split("\n")
    path = f[0]
    f_.close()
    world = jnbt.World(path)
    overworld = world[jnbt.DIM_OVERWORLD]
    blocks = f[1::]
    f = open(os.path.basename(os.path.normpath(path)) + ".txt", "w")
    f.write(path + "\n")
    i = 0
    for block in blocks:
        if block:
            x, y, z = block.split(" ")
            b = overworld.getBlock(int(x), int(y), int(z))
            if b.getID() == 31:
                f.write(x + " " + y + " " + z + "\n")
                i += 1
    return len(blocks) - 1, i

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Find grass in a minecraft world.')
    parser.add_argument('-o', '--option', choices=['create','verify'], help="Choose the option")
    parser.add_argument('-f', '--file', help="Choose the folder of the map or the file to be verified")
    args = parser.parse_args()
    choice = False
    path = False
    if args.option == "create":
        choice = "1"
    elif args.option == "verify":
        choice = "2"
    if args.file:
        path = args.file
    if not choice:
        choice = input("1 | generate file\n2 | check a generated file\nchoice : ")
    if choice == "1":
        if not path:
            path = input("save path : ")
        num = create_file(path)
        print("found", num, "grass")
    elif choice == "2":
        if not path:
            path = input("generated file path : ")
        oldnum, newnum = verify_file(path)
        print("found", newnum, "grass.", (oldnum - newnum), "grass removed from file")
