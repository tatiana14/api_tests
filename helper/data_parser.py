from collections import namedtuple

def parse_to_list(json):
    res = list()
    if 'fields' not in json:
        return res
    header = json['fields']
    data = json['data']
    for d in data:
        dict = {}
        for i, f in enumerate(d):
            key = header[i]
            dict[key] = d[i]
        d_named = namedtuple("AsteroidsData", dict.keys())(*dict.values())
        res.append(d_named)
    return res