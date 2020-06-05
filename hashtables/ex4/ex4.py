def has_negatives(a):
    positives=[]
    cache={}
    result=[]
    for num in a:
        if num > 0:
            positives.append(num)
        else:
            cache[-num] = -num
    # print(cache)

    for i in positives:
        if i in cache:
            # print(i)
            result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
