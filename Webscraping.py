# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Step 1: Fetch the webpage content
url = "https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks"
response = requests.get(url)
html_data = response.text

# Step 2: Print the specific segment for the quiz question
print(html_data[760:783])

# Step 3: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')

# Step 4: Extract data from the "By market capitalization" table
data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

# Locate the table and loop through each row
for row in soup.find_all('tbody')[2].find_all('tr'):
    col = row.find_all('td')
    if len(col) > 1:  # Avoid empty rows
        name = col[1].text.strip()
        market_cap = col[2].text.strip()
        data = data.append({"Name": name, "Market Cap (US$ Billion)": market_cap}, ignore_index=True)

# Step 5: Display the first five rows
print(data.head())

# Step 6: Save the DataFrame to a JSON file
data.to_json("bank_market_cap.json", orient="records", lines=True)
