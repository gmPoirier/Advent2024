# Advent of Code: Day 01

INPUT = "./.input/day_01.txt"

def get_distance(listA, listB):
    listA.sort()
    listB.sort()
    total_distance = 0

    for i in range(0, len(listA)):
        distance = abs(listA[i] - listB[i])
        total_distance += distance

    return total_distance

def main():
    listA = []
    listB = []

    infile = open(INPUT, 'r', encoding="utf-8")
    for line in infile:
        line = line.split()
        listA.append(int(line[0]))
        listB.append(int(line[1]))

    print(get_distance(listA, listB))
    return 0

if __name__ == "__main__":
    main()
