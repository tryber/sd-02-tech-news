array = [1, 2, 3, 4, 5]
pair = [2, 4, 6]


def mult_by_2(num):
    return num * 2


# result = array.map()
result = list(map(mult_by_2, array))
print(result)

# array.every()  // all
# array.some(item => item % 2 === 0)  // any

# "", {}, set(), [], frozenset(), tuple(), None, ==> falsy
def is_pair(num):
    return num % 2 == 0


print(all([is_pair(num) for num in pair]))


# array.fiter()
print([num for num in array if num >= 3])


for i in range(len(array)):
    print(array[i])


for item, index in enumerate(array):
    print(item, index)


print({str(num): num**2 for num in array if num > 3})


dic = {
  "banana": 1,
  "maca": 2
}

# keys, values , items
print(list(dic.items()))