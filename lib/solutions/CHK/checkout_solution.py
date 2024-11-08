

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    skus = skus.upper()

    a, b, c, d = 80, 30, 50, 45

    a_count = skus.count('A')
    b_count = skus.count('B')
    c_count = skus.count('C')
    d_count = skus.count('D')

    for i in list(skus):
        if i not in ['A', 'B', 'C', 'D']:
            return -1
        
    if a_count >= 3:
        q, mod = a_count // 3, a_count % 3
        a_sum = (q * 160) + (a * mod)
    else:
        a_sum = a * a_count

    if b_count >= 2:
        q, mod = b_count // 2, b_count % 2
        b_sum = (q * 45) + (b * mod)
    else:
        b_sum = b * b_count

    if skus:
        return a_sum + b_sum + (c * c_count) + (d * d_count)
    else:
        return b
    

