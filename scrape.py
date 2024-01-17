from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import sys
import re
import ast

def run():
    args = sys.argv[1:]
    results = []
    purchases = []
    if args:
        try:
            with open(args[0]) as f:
                for line in f:
                    array = ast.literal_eval(line)
                    purchases.append(array)
        except:
            print("Invalid file. Exiting")
            exit()

    else:
        URL = "https://store.steampowered.com/account/history/"
        driver = webdriver.Chrome()
        # options = webdriver.ChromeOptions()
        # userdatadir = 'C:/Users/sicf/AppData/Local/Google/Chrome/User Data'
        # options.add_argument(f"--user-data-dir={userdatadir}")

        driver.get(URL)
        input("Login to Steam and expand all data. Enter to continue")

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        results = soup.find_all("tr")
        name = soup.find("h2", class_="pageheader")
        for row in results:
            temp = []
            temp.append(row.find("td", class_="wht_date"))
            temp.append(row.find("td", class_="wht_items"))
            temp.append(row.find("td", class_="wht_type"))
            temp.append(row.find("td", class_="wht_total"))
            if any(x is None for x in temp):
                continue
            else:
                for i in range(len(temp)):
                    temp[i] = temp[i].text.strip()
                    temp[i] = re.sub('[\t\n]', '', temp[i])
            purchases.append(temp)

        save = input("Save this information for later? (Y or N)")
        if save.lower() == 'y':
            name = name.text.strip()
            data = open(f"{name}.txt", "w")
            for i in purchases:
                data.write(f"{i}\n")
            data.close()

    for i in purchases:
        print(i)

    # Purchases indicies: 
    # 0 - Date
    # 1 - Name
    # 2 - Type of purchase
    # 3 - Price

    totalSpent = 0
    for i in purchases:
        amount = i[3] # The price is at index 3
        # Strip dollar sign
        amount = re.sub('[$,Credit]', '', amount)
        if amount and "Wallet" not in i[1] and "Refund" not in i[1]: # 1 --> name
            totalSpent += float(amount)
            

    print(f"Total spent: ${round(totalSpent, 2)}")

    print("Type -1 to quit")
    while(True):
        query = input("Query: ")
        if query == "-1":
            break
        else:
            count = 0
            priceOfThat = 0
            items = []
            for i in purchases:
                if query.lower() in i[1].lower():
                    count += 1
                    items.append(i)
                    amount = float(re.sub('[$,Credit]', '', i[3]))
                    if("Refund" in i[1]):
                        priceOfThat -= amount
                    else:
                        priceOfThat += amount
            for i in items:
                print(i)
            print(f"There were {count} instances of {query}")
            print(f"In total, it was ${round(priceOfThat, 2)}")

if __name__ == "__main__":
    run()