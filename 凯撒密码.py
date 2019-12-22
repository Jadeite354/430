def caesarCode(plainCode):
    sa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pa = 'MNOPQRSTUVWXYZABCDEFGHIJKL'
    pwCode=[]
    for p in plainCode:
        if ord("a") <= ord(p) <= ord("z") or ord("A") <= ord(p) <= ord("Z"):
            p = p.upper()
            i = sa.index(p)
            pwCode.append(pa[i])
        else:
            pwCode.append(p)
    return "".join(pwCode)


plainText = input("请输入明文：")
print("密文是：{}".format(caesarCode(plainText)))
