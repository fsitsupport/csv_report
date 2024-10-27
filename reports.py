# reports.py
# Reports as modules to import to main.py
# Perform math on cells of the draft and print analyses
# (C) copyright: Fabian Sterzik - 2024
import time
# empty list for items to perform logic and math on
item = []
item_prices = []
top3_prices = []

# Module - List Fastsellers. Which item is sold by how much percent at the time of the report was created?
def reportStatusSold(df):
    print('Listing sales from fast to slow:')
    time.sleep(2)
    # calculate percentage sold of total amount in stock, handle devion by 0 and NaN Pandas output with 'replace()'
    df['inStock_by_ordered'] = df['Amount in Stock'] / df['Amount ordered'].replace(0, 1)
    # format float for better readability
    devision_formatted = round(df['inStock_by_ordered'] * 100)    
    # show how much percent are sold at the time the table was created
    df['percentsold'] = 100 - devision_formatted    
    # sort dataframe by 'percentsold' descending
    df_sorted = df.sort_values(by='percentsold', ascending=False)
    # loop through the items to get a list sorted by percentage sold
    for index, row in df_sorted.iterrows():
        # Output analyses of module for each item
        print(f"{row['ProductName']}: {row['percentsold']:.2f} % sold at {row['Price']:.2f} $")
        # append value to list of item_prices for mean calculation
        item_prices.append(row['Price'])
    # Output Price Mean
    # build sum of all item-prices of all items of the whole draft
    sum_prices = sum(map(int, item_prices))
    # build price-mean of <-
    mean_prices = sum_prices / len(item_prices)
    # print price-mean
    print(f"\ntotal price-mean: {mean_prices:.2f} $\n----------------------------")
    # clear lists to reuse in other modules
    item.clear()
    item_prices.clear()

# Module - List Topsellers. Which item is sold the fastest at the highest price?
def reportTop3(df):
    print('Listing Top3 sales:')
    time.sleep(2)
    # fill list first to get mean value to compare with total mean of all product prices
    for index, row in df.iterrows():
        item.append(row['ProductName'])
        item_prices.append(row['Price'])
        # calculate price-mean 
        sum_prices = sum(map(int, item_prices))
        mean_prices = sum_prices / len(item_prices)
        # print top3 sales by comparing each product price with total mean of all products
        if row['Price'] > mean_prices and row['Amount in Stock'] <= row['marked rare']:
            print(f"{row['ProductName']} - Price: {row['Price']:.2f} $")
            # fill this list to get price mean of the top3 items
            top3_prices.append(row['Price'])
        else:
            continue
    # calculate price-mean of top 3
    sum_top3_prices = sum(map(int, top3_prices))
    mean_top3_prices = sum_top3_prices / len(top3_prices)
    print(f"\nTop 3 price-mean: {mean_top3_prices:.2f} $\n----------------------------")
    # clear lists
    item.clear()
    item_prices.clear()
    top3_prices.clear()

# Module - List items shortly to become rare.
def reportRare(df):
    print('\nListing items that are rare:')
    time.sleep(2)
    # Check if entry for row 'Amount in Stock' is less than entry in row 'marked rare'
    for index, row in df.iterrows():
        if row['Amount in Stock'] < row['marked rare'] and row['Amount in Stock'] > 0:
            item.append(row['ProductName'])
            item_prices.append(row['Price'])
        else:   
            continue
        # list items that are rare and give the sum in one line
        print(f"{row['ProductName']} - Price: {row['Price']:.2f} $")
    # print amount of rare items
    print('\ntotal:', len(item))
    # price-mean and output
    sum_prices = sum(map(int, item_prices))
    mean_prices = sum_prices / len(item_prices)
    print(f"price-mean: {mean_prices:.2f} $\n----------------------------")
    item.clear()
    item_prices.clear()

# Module - List items out of stock.
def reportOutofstock(df):
    print('\nListing items that are out of stock:')
    time.sleep(2)
    # Check In Stock Status
    for index, row in df.iterrows():
        # if entry for row 'Amount in Stock' = 0, do. Else continue in loop.
        if row['Amount in Stock'] == 0:
            # append item of row 'ProductName' to list 'item' and row 'Price' to list 'item_prices'
            item.append(row['ProductName'])  
            item_prices.append(row['Price'])
        else:   
            continue
        # list items that are out of stock and give the sum in one line
        print(f"{row['ProductName']} - Price: {row['Price']:.2f} $")
    # print total amount of items out of stock
    print('\ntotal:', len(item))
    # Output Price Mean:
    # build sum of all item-prices that have value 0 in row 'Amount in Stock'
    sum_prices = sum(map(int, item_prices))
    # calculate mean of all items out of stock
    mean_prices = sum_prices / len(item_prices)
    # print what was just calculated with 2 digits after zero
    print(f"price-mean: {mean_prices:.2f} $\n----------------------------")
    # clear lists to be used again in next module
    item.clear()
    item_prices.clear()


# Module - List Flopsellers. Which item sells slowest and might be reduced in price?
# def reportFlop3(df):    