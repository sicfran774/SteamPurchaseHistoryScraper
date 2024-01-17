# Steam Purchase History Scraper

This Python script will give you information on your Steam Purchase History. You can query by name to see specific rows.\
Note: This uses ChromeDriver with Selenium. You may need to install Google Chrome to run this script.

## How to use

1. Create and activate a Python virtual environment and install the necessary packages (BeautifulSoup4, Selenium for ChromeDriver)

```
python -m pip install bs4 selenium
```

2. Run the script (ChromeDriver will open)
```
python scrape.py [data.txt]
```
*[data.txt] is an optional parameter, keep reading below for more information. "dummydata.txt" is provided for testing*

3. Sign into your Steam account
![image](https://github.com/sicfran774/SteamPurchaseHistoryScraper/assets/1214993/d9d10c23-914e-456e-8f3d-6f1e83899429)

4. Press Enter in console when done. You can decide to save the data into a .txt file within the same directory, which can be used as an optional parameter when you run the script.

5. Data!\
![image](https://github.com/sicfran774/SteamPurchaseHistoryScraper/assets/1214993/e7aa7757-6a4b-462e-a0af-8148b9e63a3a)

7. You can query by name to see how many instances are present and how much they were in total
![image](https://github.com/sicfran774/SteamPurchaseHistoryScraper/assets/1214993/347cce60-9cf4-455c-8b9e-87187e8b0935)
