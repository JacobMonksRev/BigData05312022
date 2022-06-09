import collections
from collections import OrderedDict
from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import ChainMap

d = {"Name":"Jacob", "Degree":"Bachelor"}
d2 = {"Firstname":"Ross", "CollegeDegree":"Master"}

cm = ChainMap(d, d2)

# print(cm)

print(cm.maps)

# print(list(cm.keys()))
# print(list(cm.values()))

print(list(cm.keys()))
print(list(cm.values()))

for key, val in cm.items():
    print('{} = {}'.format(key, val))


