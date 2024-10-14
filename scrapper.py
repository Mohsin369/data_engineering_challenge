from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import calendar  # To get the month names
import re  # For extracting year and month from href

def wait_for_downloads(download_path):
    """
    Function to wait until there are no more files with the extension '.crdownload' in the download folder.
    """
    while any(filename.endswith('.crdownload') for filename in os.listdir(download_path)):
        time.sleep(1)  # Wait 1 second before checking again

# Function to set up download folder hierarchy
def create_download_folder(base_path, year, month):
    """
    Creates a folder structure like 'base_path/year/month' if it doesn't exist.
    """
    month_name = calendar.month_name[month]  # Get the name of the month
    folder_path = os.path.join(base_path, str(year), month_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Create folder if it doesn't exist
    return folder_path

# Set the base path to the 'data' folder inside your Downloads directory. Can change the path according to need
base_download_path = os.path.join(os.path.expanduser("~"), "Downloads", "Data Engineering Task", "Scrapping Work", "data")

# Configure Chrome WebDriver options
options = webdriver.ChromeOptions()

# Update the preferences for the WebDriver once
prefs = {
    "download.prompt_for_download": False,  # Disable download prompt
    "safebrowsing.enabled": True  # Disable the 'safe browsing' warnings
}
options.add_experimental_option("prefs", prefs)

# Initialize a single WebDriver instance
driver = webdriver.Chrome(options=options)

# Navigate to the website containing the links
driver.get('https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page')  # Replace with the actual URL

# Loop through each year from 2019 to 2024
for year in range(2019, 2025):
    # Dynamically create the XPath based on the year
    xpath = f"//div[@id='faq{year}']//a"
    # Find all the hrefs within the div for the current year
    links = driver.find_elements(By.XPATH, xpath)

    # Loop through each link
    for link in links:
        href = link.get_attribute("href")
        
        # Extract the year and month from the href (e.g., 2019-01)
        match = re.search(r'(\d{4})-(\d{2})', href)
        if match:
            year_str, month_str = match.groups()
            year = int(year_str)
            month = int(month_str)

            # Print debugging information
            print(f"base_download_path --> {base_download_path}")
            print(f"xpath --> {xpath}")
            print(f"link --> {link}")
            print(f"href --> {href}")
            
            # Create the download folder hierarchy based on extracted year and month
            download_folder = create_download_folder(base_download_path, year, month)
            
            # Update the default download directory in the current WebDriver session
            driver.execute_cdp_cmd('Page.setDownloadBehavior', {
                'behavior': 'allow',
                'downloadPath': download_folder
            })
            
            # Open the download link
            driver.get(href)
            time.sleep(2)  # Give the download a chance to start

            # Wait for the file to finish downloading before continuing
            wait_for_downloads(download_folder)

# Close the WebDriver session
driver.quit()
