# ruturn latitude and longitude of each location

def GetLatiLongi():
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    f = open(path + '/latitude_longitude', 'r')
    results = dict()
    for line in f:
        nline = line.strip().split('\t')
        results[nline[0]] = map(int, nline[1].split(','))
    return results

if __name__ == "__main__":
    print GetLatiLongi()
