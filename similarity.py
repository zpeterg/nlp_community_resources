
def similarity(arr, syno_arr):
    rtn = 0
    for synos in syno_arr:
        for syno in synos:
            if syno in arr:
                rtn += 1
    return rtn

