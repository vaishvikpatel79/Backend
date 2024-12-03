from Sales_pred_func import sales_prediction

item_categories = {
    'Electronics': 'Electronics',
    'Fashion': 'Clothes',
    'Office Supplies': 'Furniture',
    'Books': 'Books',
    'Home & Kitchen': 'Home Appliances',
    'Toys  & Games': 'Toys',
    'Health & Beauty': 'Beauty & Personal Care',
    'Sports & Outdoors': 'Groceries',
    'Automotive': 'Furniture',
    'Pet Supplies': 'Footwear',
    'Stationeries': 'Stationery',
}

item_sub = {
    'Smartphone': 'Smartphone',
    'Laptop': 'Laptop',
    'Smartwatch': 'Smartwatch',
    'Television': 'Smartphone',
    'Camera': 'Laptop',
    
    'Shirts': 'Shirts',
    'Pants': 'Pants',
    'Dresses': 'Dresses',
    'Jackets': 'Jackets',
    'Socks': 'Socks',

    'Pens': 'Pens',
    'Notebooks': 'Notebooks',
    'Markers': 'Markers',
    'Staplers': 'Staplers',
    'Folders': 'Folders',

    'Fiction': 'Fiction',
    'Non-fiction': 'Non-fiction',
    'Textbooks': 'Textbooks',
    'Magazines': 'Magazines',
    'Comics': 'Comics',

    'Cookware': 'Refrigerator',
    'Fuurniture': 'Microwave',
    'Home Decor': 'Washing Machine',
    'Storage': 'Air Conditioner',
    'Cleaning': 'Vacuum Cleaner',

    'Action Figures': 'Action Figures',
    'Puzzles': 'Puzzles',
    'Board Games': 'Board Games',
    'Dolls': 'Dolls',
    'Remote Control Cars': 'Remote Control Cars',

    'Skincare': 'Skincare',
    'Haircare': 'Haircare',
    'Makeup': 'Makeup',
    'Perfume': 'Perfume',
    'Body Lotion': 'Body Lotion',
}




# Get user inputs
state = input("Enter your state: ")
item_cat = input("Enter the item category: ")

if item_cat in item_categories:
    item_category = item_categories[item_cat]
else:
    item_category = item_cat
    
subcat = input("Enter the subcategory: ")
if subcat in item_sub:
    subcategory = item_sub[subcat]
else:
    subcategory = subcat
    
months = int(input("How many months of inventory (between 1 and 12)? "))
prev_sale = int(input("what was the previous sales of your shop in the same time period? "))

user_sales_prediction = sales_prediction(state, item_category, subcategory, months,prev_sale)

if(user_sales_prediction<0):
    user_sales_prediction=0

print(f"predicted sales for next {months} months is: {user_sales_prediction}")


