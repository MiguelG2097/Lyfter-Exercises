my_list = ['string','loop','float','char']


if len(my_list) >=1:
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
    print(my_list)

#----- Old version --------
#deleted_item = my_list.pop(0)
#my_list.insert(3,deleted_item)
##deleted_item2 = my_list.pop(2)
#my_list.insert(0,deleted_item2)
#print(my_list)
