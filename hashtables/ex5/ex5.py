import os


def finder(files, queries):
    cache = {}
    result = []

    for i in files:
        tail = os.path.split(i)[-1]
        # print(tail)
        if tail not in cache:
            cache[tail] = [i]
        else:
            cache[tail].append(i)
        # print(cache)

    for j in queries:
        if j in cache:
            # print(j)
            result += cache[j]

    print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
