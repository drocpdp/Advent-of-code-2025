import base

sum_invalid_ids = 0


def is_invalid_id(id):
    if len(id) == 1:
        return False
    if len(id) == 2:
        if id[0] == id[1]:
            return True
        return False
    for i in range(1, len(id) // 2 + 1):
        vals = set()
        for ii in range(0, len(id), i):
            vals.add(id[ii:ii+i])
        if len(vals) == 1:
            return True
    return False
    
    

            

for ln in base.get_data("day2_data"):
    for num_range in ln.split(','):
        (L, R) = num_range.split('-')
        for num in range(int(L), int(R)+1):
            if is_invalid_id(str(num)):
                sum_invalid_ids += num

print(sum_invalid_ids)