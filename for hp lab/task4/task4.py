filename = input("Введите путь к файлу: ")
nums = []
file_in = open(filename, "r")
for line in file_in:
    nums.append(int(line.rstrip("\n")))
file_in.close()

def EQ(nums):
    nums.sort()
    med = int(nums[len(nums) // 2])
    moves = sum(abs(n - med) for n in nums)
    return moves

print(EQ(nums))