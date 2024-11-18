# main.py
# use pandas to handle csv files and the created custom modules to analyse them
# and prompt a report
# (C) copyright: Fabian Sterzik - 2024
# Import modules to build report from excel-draft
# import sys # not used at this point
# import os # not used at this point
import pandas as pd
import time
from reports import reportOutofstock, reportRare, reportStatusSold, reportTop3

def main():
    # handling KeyboardInterrupt by user
    try:
        while True:
            filepath = './Inventory_2024-10-01-12-00-00.csv' 
            print('Starting report...')
            time.sleep(2)
            # Read excel file
            draft = pd.read_csv(filepath)
            # set DataFrame for draft to call and use excel cells/items to process with pandas
            # optional which colums are used
            df = pd.DataFrame(draft,    
                            columns=['ProductName', 'ProductID', 'Category', 'Price', 'First in Store', 
                                     'In stock', 'Amount ordered', 'Amount in Stock', 'marked rare'])
            print(f"Draft: {filepath} \nSheet: Table1\n----------------------------")
            # call function with pointer to pd.DataFrame as arg of function
            # Module - List Fastsellers. (df) is pointer / zeiger
            time.sleep(2)
            reportStatusSold(df)
            # Module - List Topsellers.
            time.sleep(2)
            reportTop3(df)
            # Module - List items shortly to become rare.
            time.sleep(2)
            reportRare(df)
            # Module - List items out of stock.
            time.sleep(2)
            reportOutofstock(df)
            break
            # Module - List Flopsellers. T.B.C.
    # handling KeyboardInterrupt 
    except KeyboardInterrupt:
        print('Report canceled by user.')
        
# makes sure, that main() will only be executed, if it is executed as itself, not as a
# imported script.    
if __name__ == "__main__":
    main()
