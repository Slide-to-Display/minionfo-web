import json


def Display(data):
    results = list()
    for i in data:
        d = json.loads(i)
        content = d['text'].encode("utf-8")
        place = 'None'
        if d['place'] != None:
            place = d['place']['full_name'].encode("utf-8")
        results.append('%s\n%s\n' % (content, place))

    return '\n\n'.join(results)
    

if __name__ == '__main__':
    pass
