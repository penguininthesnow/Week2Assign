# 作業四:列車問題

def func4(sp, stat, n):
    candidates=[]

    for i, (s, st) in enumerate(zip(sp, stat)):
         if st == '0': # 只看可服務的車廂
            candidates.append((i, s))  
    if not candidates:
        return None

    # 能完全容納乘客的車廂
    enough=[(i, s) for i, s in candidates if s>= n]
    if enough:
        #   選座位數最小的那一個
        idx= min(enough, key=lambda x: x[1])[0]
    else:
        #  選座位數最小的那一個(剛好夠)
        idx = max(candidates, key=lambda x:x[1])[0]

    return idx
    

print (func4([3, 1, 5, 4, 3, 2], "101000", 2))
print (func4([1, 0, 5, 1, 3], "10100", 2))
print (func4([4, 6, 5, 8], "1000", 4))