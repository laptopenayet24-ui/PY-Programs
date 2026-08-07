'''input=["racecar","carrace","eat","tea","oillamp"]
output=[["racecar","carrace"],["eat","tea"],["oillamp"]]'''


def grouped_ana(strings):
    hash={}
    for i in strings:
        sort_str="".join(sorted(i))
        if sort_str in hash:
            hash[sort_str]+=[i,]
        else:
            hash[sort_str]=[i]
    return list(hash.values())
input1=["racecar","carrace","eat","tea","oillamp"]
print(grouped_ana(input1))
