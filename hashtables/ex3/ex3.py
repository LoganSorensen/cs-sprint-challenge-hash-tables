def intersection(arrays):
    cache={}
    result=[]
    # print(arrays)
    for array in arrays:
        # print(i)
        for i in array:
            if i not in cache:
                cache[i] = i
            elif i not in result:
                result.append(i)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
