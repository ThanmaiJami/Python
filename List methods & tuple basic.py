"""mix_l = ['Hello',-34,'hai',True]
print("1.",mix_l[-1])
print(mix_l)
mix_l[1]="Hi"
print("2.",mix_l)
mix_t = (1,2,3,4,5)
print("3.",mix_t)"""
list = [12,78,374,90]
for i in list[:3]:
    print(i)
list1 = list.copy()
print(list1)
list.append(12) #append
list.remove(12) #remove method
list.remove(374)
print(list)
list.insert(1,34556) #insert
print(list)
list[2] = 45 #assignment
print(list)
