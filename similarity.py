
def similarity(arr, synoArr):
    rtn = 0
    for synos in synoArr:
        for syno in synos:
            if syno in arr:
                rtn += 1
    return rtn

