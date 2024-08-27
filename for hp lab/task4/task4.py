import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('name1', nargs='?')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    filename1 = namespace.name1

    nums = []
    file_in = open(filename1, "r")
    for line in file_in:
        nums.append(int(line.rstrip("\n")))
    file_in.close()

    def EQ(nums):
        nums.sort()
        med = int(nums[len(nums) // 2])
        moves = sum(abs(n - med) for n in nums)
        return moves

    print(EQ(nums))
