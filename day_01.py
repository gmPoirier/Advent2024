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

def get_similarity(listA, listB):
    similarity = 0

    for num in listB:
        similarity += num * listA.count(num)

    return similarity

def main():
    listA = []
    listB = []

    infile = open(INPUT, 'r', encoding="utf-8")
    for line in infile:
        line = line.split()
        listA.append(int(line[0]))
        listB.append(int(line[1]))

    print("star 01: ", get_distance(listA, listB))
    print("star 02: ", get_similarity(listA, listB))
    return 0

if __name__ == "__main__":
    main()
