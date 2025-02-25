from collections import Counter
test_list=[{1,3},{3,44,2},{2,42,5},{3,44,2},{1,2,3},{4,3},{1,3},{1,2,3}]
print("Original list:\n"+str(test_list))
freqs=Counter(frozenset(sub) for sub in test_list)
if len(freqs)>0:
    for key,val in freqs.items():
        if val>1:
            print(key)
    
