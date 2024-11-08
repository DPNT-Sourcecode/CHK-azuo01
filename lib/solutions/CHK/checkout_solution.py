

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    a, b, c, d, e = 50, 30, 20, 15, 40

    a_count = skus.count('A')
    b_count = skus.count('B')
    c_count = skus.count('C')
    d_count = skus.count('D')
    e_count = skus.count('E')

    for i in list(skus):
        if i not in ['A', 'B', 'C', 'D', 'E']:
            return -1
        
    if a_count >= 5:
        q, mod = a_count // 5, a_count % 5
        if mod < 3:
            a_sum = (q * 200) + (a * mod)
        elif mod == 3:
            a_sum = (q * 200) + 130 
        else:
            a_sum = (q * 200) + 180
    
    if a_count >= 3 and a_count < 5:
        q, mod = a_count // 3, a_count % 3
        a_sum = (q * 130) + (a * mod)
    else:
        a_sum = a * a_count

    if b_count >= 2:
        q, mod = b_count // 2, b_count % 2
        b_sum = (q * 45) + (b * mod)
    else:
        b_sum = b * b_count

    if e_count >= 2:
        q, mod = e_count // 2, e_count % 2
        if q >= 1 and b_sum >= 30:
            b_sum -= q * 30

    if skus:
        return a_sum + b_sum + (c * c_count) + (d * d_count)
    else:
        return 0



