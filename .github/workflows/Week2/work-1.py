# 作業一:位置座標判斷

positions = {
    "悟空":(0, 0),
    "丁滿":(-1, 4),
    "辛巴":(-3, 3),
    "貝吉塔":(-4, -1),
    "弗利沙":(4, -1),
    "特南克斯":(1, -2),

}

# 斜線 假設 y=-x+2
LINE_A, LINE_B, LINE_C = 1.0, 1.0, -2.0

# # 設定邊界
# X_MIN, X_MAX = -4, 4
# Y_MIN, Y_MAX = -2, 4

def same_side(p1, p2, a, b, c):
    v1=a+p1[0]+b*p1[1]+c
    v2=a+p2[0]+b*p2[1]+c
    if v1==0 or v2==0:
        return True
    return v1*v2>0 #同號表示在同一側

def cross_line(p1, p2, a, b, c, cheat=2):
    dx= abs(p1[0] - p2[0])
    dy= abs(p2[0] - p2[0])
    cor = dx + dy # 同側則回傳 cor
    if same_side:
        return cor
    else:
        return cor + cheat # 不同側代表有跨越 要+2(cheat)


def func1(name):
    if name not in positions:
        print("角色不存在")
        return
    

    target = positions[name]
    dists = {}

    for other, pos in positions.items():
        if other == name:
            continue
        d = cross_line(target, pos, LINE_A, LINE_B, LINE_C , cheat=2)
        dists[ other ] = d

    min_d = min(dists.values())
    max_d = max(dists.values())

    nearest = sorted([n for n, d in dists.items() if d == min_d])
    farthest = sorted([n for n, d in dists.items() if d == max_d])

    print(f"{name} -> 最遠( 距離{max_d} ): {', '.join(farthest)} ;最近 (距離{min_d}):{', '.join(nearest)} ")

func1("辛巴")
func1("悟空")
func1("弗利沙")
func1("特南克斯")
