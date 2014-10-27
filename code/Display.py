import json


def Display(data):
    results = list()
    for i in data:
        d = json.loads(i)

        text = d['text'].encode("utf-8")
        lang = d['lang'].encode("utf-8")
        created_time = d['created_at'].encode("utf-8")
        place = 'None'
        if d['place'] != None:
            place = d['place']['full_name'].encode("utf-8")

        # results.append('%s\n' % text)
        results.append('text: %s\nlang: %s\ncreated_time: %s\nplace: %s\n===\n' \
                       % (text, lang, created_time, place))

    return '\n\n'.join(results)
    

if __name__ == '__main__':
    pass
