"""
Ghép 2 dict, mỗi item bằng tổng value của 2 item cùng key trong các dict còn lại.
"""

dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

# dict3 = {'a': 400, 'b': 400, 'c': 300, 'd': 400}
dict3 = dict1 | dict2

print(dict3)

for item in dict3:
    try: 
        dict3[item] = dict1[item] + dict2[item]
    except:
        try:
            dict3[item] = dict1[item]
        except:
            dict3[item] = dict2[item]

print(dict3)