from pprint import pprint


dir_ = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(0, 16)]

pprint(dir_)