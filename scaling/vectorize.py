
from yass.batch import vectorize_parameter

@vectorize_parameter('a')
def add(a, b, c):
    return a + b + c


class Object(object):

    @vectorize_parameter('a')
    def add(self, a, b, c):
        return a + b + c


add([0, 1, 2, 3, 4], 1, 0)

o = Object()
o.add([0, 1, 2, 3, 4], 1, 0)



@vectorize_parameter('a')
def add(a, b, c):
    return sum(a) + b + c


add([[1, 1, 1]], 1, 1)

d = dict(a=[0, 10, 20], b=[1, 11, 21], c=1)
to_pop = ['a', 'b']

from copy import copy


def split_parameters(params, to_split):
    """
    """
    params = copy(params)

    def multi_pop(d, to_pop):
        dic = {}
        for key in to_pop:
            dic[key] = d.pop(key)
        return dic

    params_to_split = multi_pop(params, to_split)

    keys = params_to_split.keys()
    values_tuples = zip(*params_to_split.values())

    distributed = [{k: v for k, v in zip(keys, values)} for values
                   in values_tuples]

    return [merge_dicts(dist, params) for dist in distributed]

split_parameters(d, ['a', 'b'])
split_parameters(d, ['a'])
    