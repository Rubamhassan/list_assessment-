melon = 1 
#cost per melon

def payment_table_for_melons(data_sheet):
	#figure out who has underpaid for the melons 
	payment_file = open(data_sheet)

	for item in payment_file:
		each_order = item.split(" ")
		#this will split the lines
		customer = each_order(1)
		#this will get the customers name
		number_of_melons = each_order(2)
		#this will get the number of melons per customer
		total_paid_so_far = each_order(3)
		#this is the amount paid till now

		total_to_be_paid = number_of_melons * total_paid_so_far
		#this will figure out if whats paid is enough

		if total_to_be_paid == total_paid_so_far:
			print customer "has paid for his/her melons."
		elif total_to_be_paid < total_paid_so_far:
			print customer "has underpaid for his/her melons."
		elif total_to_be_paid > total_paid_so_far:
			print customer "has overpaid for his/her melons."

payment_table_for_melons("customer-orders.txt")