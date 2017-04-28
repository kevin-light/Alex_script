array = [[col for col in range(5)] for row in range(5)]  # 初始化一个4*4数组
# array=[[col for col in 'abcde'] for row in range(5)]

for row in array:  # 旋转前先看看数组长啥样
    print(row)

print('-------------')
for i, row in enumerate(array):

    for index in range(i, len(row)):
        tmp = array[index][i]  # get each rows' data by column's index
        array[index][i] = array[i][index]  #
        print
        tmp, array[i][index]  # = tmp
        array[i][index] = tmp
    for r in array: print(r)

    print('--one big loop --')