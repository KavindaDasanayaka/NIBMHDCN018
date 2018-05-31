item_list=[]
price_list=[]
def tot(t):
	sum=0
	for i in t:
		sum=float(i)
		return sum
	no=int (raw_input("no of items :"))
	for i in range(no):
		item=str(raw_input("name of the item "+str(i+1)+":"))
		price=float(raw_input("price of the item "+str(i+1)+":"))
		item_list.append(item)
		price_list.append(price)
		discount=float(raw_input("\n\n enterthe discount :"))
		toatl=float(tot(price_list))
		dis=total*discount/100.0
		net_price=toale-dis
		print("net price" ,net_price)
