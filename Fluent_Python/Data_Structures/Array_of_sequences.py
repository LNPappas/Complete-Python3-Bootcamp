import array
import os

# Container Sequences: holds items of different types
# Flat Sequences: store value of each item in it's own memory space
# Flat Sequences are more compact, but limited to primitive values

# Mutiple Sequence: Can be changed (list, array, dict)
# Immutable Sequence: Cannot be changed (tuple, bytes, string, int)
# ex. string can be added together to create a new string, 
# you can access substrings, but you can't actually alter the string itself.

# List Comprehension and Readability
# Build a list of Unicode codepoints from a string
symbols = '$¢£¥€₹'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# Same list, different format
code = [ord(symbol) for symbol in symbols]
print(code)
print('\n')

# ord(): an integer representing the Unicode code point of the character when the argument is a unicode object

# List Comps vs Map Filters
# list compL
a = [ord(s) for s in symbols if ord(s) > 127]
# map and filter with lambda
b = list(filter(lambda c: c> 127, map(ord, symbols)))
print(a)
print(b)
print('\n')

# cartesian products with tuples
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# order by color
tshirts = [(color, size) for color in colors for size in sizes]
# order by sizes
tshirts2 = [(color, size) for size in sizes for color in colors]
print(tshirts)
print(tshirts2)
print('\n')

# Generator Expressions : save memory by yeilding items one by one 
# using iterator protocol instead of a whole list
# GenExps us same syntax as listcomps, but parenthese instead of brackets

# genExps in a tuple()
a = tuple(ord(symbol) for symbol in symbols)
# import array, string and gen exps in array
b = array.array('I', (ord(symbol) for symbol in symbols))
print(a)
print(b)
# Caresian product in a genexp
# genexp prints one by one, not creating a list. 
for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
    print(tshirt)
# producing an outpus that is not stored in memory. 
print('\n')

# Tuples as records: each item holds data in one field and 
# position of item gives it's meaning
# therefore order is vital and sorting would distroy the information

# lat and long
coord = (33.9525, -118.408056)
# data bout Tokyo
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# (country code, passport)
traveler = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# % formating treates each item of tuple as seperate field
for passport in sorted(traveler):
    print('%s/%s' % passport)
print('\n')
# for loop retrieves item of tupples seperately also
for country, _ in traveler:
    print(country)
print('\n')

# Tuple unpacking:
# assigning variable to tuples while created (Tokoyo info)
# also asigning % operator for each item

# parallel assignement:
lat, lon = coord
print(lat)
print(lon)
print('\n')

# can swap without using temp variable:
lat, lon = lon, lat
print(lat)
print(lon)
print('\n')

# fix argument with * while unpacking:
print(divmod(20,8))
t = (20,8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient)
print(remainder)
print('\n')

# os.path.split() builds tuple (path, last_part) from filesystem path
_,filename = os.path.split('/home/luciano/.ssh/idresa.pub')
print(filename)
print('\n')

# using * to grap excess items
# note * prefix can occur anywhere, but only once
a, *b, c, d = range(5)
print(a,b,c,d)
# range must be >= number variables - *variable
# so 4 total variable - 1 *variable = 3
# since there can only be one star variable
# range >= total # variables - 1
a, *b, c, d = range(3)
print(a,b,c,d)
print('\n')

# nested tuple unpacking
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.34221432,129.343)),
    ('Delhi','IN', 21.935, (28, 77.3423)),
    ('Mexico','MX', 30.142, (19.3, -99.111))
]
fmt = '{:15} | {:9.4f} | {:9.4f}'
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
for name, cc, pop, (lat, long) in metro_areas:
    print(fmt.format(name, lat, long))
print('\n')

# Named Tuples
