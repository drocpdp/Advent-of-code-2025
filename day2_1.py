import base

sum_invalid_ids = 0

def is_invalid_id(id):
    l, r = 0, len(id)//2
    for _ in range(len(id) // 2):
        if id[l] != id[r]:
            return False
        l, r = l+1, r+1
    return True

for ln in base.get_data("day2_data"):
    for num_range in ln.split(','):
        (L, R) = num_range.split('-')
        for num in range(int(L), int(R)+1):
            if not(len(str(num)) % 2):
                if is_invalid_id(str(num)):
                    sum_invalid_ids += num

print(sum_invalid_ids)
        
        


