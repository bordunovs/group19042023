set1 = set()
print(set1)

set2 = {5, 5, 6, 6, 'jj', 'k', 5.5, 7., True}
print(set2)
print(len(set2))

citi = {'london','paris'}
unique_citi = set(citi)
print(unique_citi)

unique_citi.add('paris')
print(unique_citi)
#unique_citi.update('abc')
#print(unique_citi)
#unique_citi.remove('b')
#data = unique_citi.pop()
#print(data, unique_citi)


set1 = {1, 2, 3}
set2 = {4, 2, 3}

#new_set_common = set1.intersection(set2)
new_set_common_3_10 = set1 & set2

print(new_set_common_3_10)


#set1 = {1, 2, 3}
#set2 = {4, 2, 3}

#new_set_common = set1.intersection(set2)
#new_set_union_3_10 = set1 | set2

#print(new_set_union_3_10)

#set1 = {1, 2, 3}
#set2 = {4, 2, 3}

#new_set_common = set1.intersection(set2)
#new_set_dif_3_10 = set1 - set2

#print(new_set_dif_3_10)




