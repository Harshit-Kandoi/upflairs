# tuple  
# stored in () instead of [] like lists
# tuples are immutable in nature

# tp = (14, 20, 43.5, 'raor')
# print(tp)
# print(type(tp))
# print(tp[2:6])    #accessing is allowed
# tp[2] = "DONE"        # changes are not possible
# print(tp)
# del tp[2]
# print (tp)

# deletion and insertion are not allowed

# set   = # multiple , duplicate values are not allowed
# uses curly bracket for set {}
# set is also immutable
# st = {20,23,23,24,25}
# print(st)
# # print(type(st))
# print(st[2:3])      # sets are orderless so accessing is not avaliable
# st[2] = "done"
# print(st)  # changes bhi nhi hote h
# st.add(100)   #insertion is allowed
# print(st)
# st.discard(100)  #discard function is same as remove
# st. discard(65)  #don't throw a error if a element is not possible
# st.remove(100)  #deletion is also possible
# print(st)

# st1 = {11,34,23,45,56, True}
# st2 = {34,45,23,46,56,65}
# st1.update(st2)
# print(st1)

# Dictionary
#mutable 
# accessing allow by the key
# deletion and insertion
dt = {"a":10, "B":20}
# dt.pop("a")
# dt["a"] = 40
dt["c"] = 20
print(dt)
# print(type(dt))
# print(dt["a"])
# print(dt.keys())
# print(dt.values())

dt1 = {"A":23, "B": 25, "C" :35}
dt2 = {"D" = }