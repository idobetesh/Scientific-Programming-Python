dic = {"d": 2, "e": 6, "a": 13}
tmpDic = {}
for k in sorted(dic.keys()):
    tmpDic[k] = dic[k]
print(tmpDic)
