
np_orders = pd_orders.to_numpy()
alpha_ones = []
smallest = 999999
largest = 0
for order in np_orders:
    m = re.search('\D', order[1])
    if m and m.group(0):
        alpha_ones.append(order[1])
        
    if str(order[1]).isnumeric() and int(order[1]) < int(smallest):
        smallest = order[1]
        
    if str(order[1]).isnumeric() and int(order[1]) > int(largest):
        largest = order[1]   
        
print(len(alpha_ones))
print("smallest is " + str(smallest))
print("largest is " + str(largest))
