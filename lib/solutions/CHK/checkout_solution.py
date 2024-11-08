

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    a = 50
    b = 30
    c = 20
    d = 15

    a_count = skus.count('A')
    b_count = skus.count('B')
    c_count = skus.count('C')
    d_count = skus.count('D')

    if b_count >= 2:
        q, mod = b_count // 2, b_count % 2
        b_sum = (q * 45) + (b * mod)
    else:
        b_sum = b
    
    if a_count >= 3:
        q, mod = a_count // 3, a_count % 3
        a_sum = (q * 130) + (a * mod)
    

