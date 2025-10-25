# 作業二:一對一服務設置

def func2( ss, start, end, criteria ):
    if not hasattr(func2, "schedule"):
        func2.schedule = {s["name"]:[] for s in ss}

    field, op, value = None, None, None
    for o in ["<=", ">=", "="]:
        if o in criteria:
            field, value = criteria.split(o)
            op = o
            field, value = field.strip(), value.strip()
            break

    available = []

    for s in ss:
        conflict = any(not(end <= st or start >= et) for st, et in func2.schedule[s["name"]])
        if conflict:
            continue

        if field == "name":
            if op == "=" and s["name"] == value:
                available.append(s)
            # match = (op == "=" and s["name"] == value)
        else:
            val = float(value)
            if op == ">=" and s[field] >= val:
                available.append(s)
            elif op == "<=" and s[field] <= val:
                available.append(s)
            elif op =="=" and s[field] == val:
                available.append(s)

    if not available:
        print("Sorry")
        return
        
    if field != "name":
        val = float(value)
        chosen = min(available, key=lambda x: abs(x[field] - val))
    else:
        chosen = available[0]

    func2.schedule[chosen["name"]].append((start, end))
    print(chosen["name"])



services=[
    {"name": "S1", "r": 4.5, "c": 1000},
    {"name": "S2", "r": 3, "c": 1200},
    {"name": "S3", "r": 3.8, "c": 800}
]


func2(services, 15, 17, "c>=800" )
func2(services, 11, 13, "r<=4" )
func2(services, 10, 12, "name=S3" )
func2(services, 15, 18, "r>=4.5" )
func2(services, 16, 18, "r>=4" )
func2(services, 13, 17, "name=S1" )
func2(services, 8, 9, "c<=1500" )