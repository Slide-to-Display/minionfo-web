# return a list of US stetes

def GetStateList():
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    f = open(path + '/state_list', 'r')
    result = list()
    for line in f:
        nline = line.split('\t')
        result.append((nline[0].lower(), nline[0]))
    return result


if __name__ == "__main__":
    print GetStateList()
