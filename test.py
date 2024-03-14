import time
from csv import writer
from datetime import datetime
from urllib.parse import unquote

from selenium import webdriver
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


"""
اسم
رقم تليفون
عنوان
ولوكيشن
والمنهج التعليمي
عدد فصول
الريت
ترتيبهم ف المملكة أبتدائي وإعدادي وثانوي ولا واحد من التلاته 
لو في صور
"""

def main():
    service = Service()

    # instance of Options class allows us to configure Chrome
    options = webdriver.ChromeOptions()

    options.add_argument('--headless')  # Uncomment to run without UI (Headless)
    # options.page_load_strategy = 'eager'  # Don't wait for the page tp fully load

    # initializing webdriver for Chrome with our options
    driver = webdriver.Chrome(service=service, options=options)

    ar_url = "https://yaschools.com/%D8%A7%D9%84%D9%85%D8%AF%D8%A7%D8%B1%D8%B3"  # AR starting URL
    en_url = "https://yaschools.com/en/schools"  # EN starting URL

    print("Opening Browser!")
    
    # Opening Main Page
    driver.get(ar_url)

    # Wait to Page Loader to finsih
    print("Waiting 20 Sec for Loader to Finsih!")
    time.sleep(20)

    # View 99 School per Page
    per_page_select = Select(driver.find_element(By.CSS_SELECTOR, "#itemCount"))
    per_page_select.select_by_value("99")

    # Wait for UI to update
    print("Waiting 10 Sec for Page UI to Update!")
    time.sleep(10)

    # Create CSV FIle to Save Data
    print("Creating CSV File!")
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"ar_datatest_{now}.csv", "w", newline="", encoding="utf-8") as f:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f)

        # Add CSV Header Row
        HEADERS = [
            "index",
            "name",
            "url",
        ]
        writer_object.writerow(HEADERS)

        # Get Next Page Button
        page = 1
        school_index = 1
        next_page_btn = False
        try:
            next_page_btn = driver.find_element(By.CSS_SELECTOR, ".SchoolPagination i.icon-next")
        except:
            next_page_btn = False


        # Looping Pages to the End Page
        while next_page_btn:

            # Get Schools Titles & URLs
            school_anchors = driver.find_elements(By.CSS_SELECTOR, ".school .top .body p a")

            print("=" * 20)

            # Looping Each School in the page
            for school_i, school in enumerate(school_anchors):
                print(
                    f"Getting School [{school_i+1} of {len(school_anchors)}] in Page[{page}]..."
                )

                # School Index
                row = [str(school_index)]
                school_index += 1

                # School Name
                try:
                    school_name = school.text.strip()
                    row.append(school_name)
                except:
                    row.append("")

                # School Page URL
                try:
                    school_url = school.get_attribute("href").strip()
                    row.append(unquote(school_url))  # URL Decoded
                except:
                    row.append("")
                
                writer_object.writerow(row)

            # Finding Next Page Button if still exists
            try:
                next_page_btn = driver.find_element(By.CSS_SELECTOR, ".SchoolPagination i.icon-next")
            except:
                next_page_btn = False

            # Navigating to next page
            if next_page_btn:
                try:
                    next_page_btn.click()
                except:
                    driver.execute_script("arguments[0].click();", next_page_btn)

                # Waiting for UI to Update
                time.sleep(10)

            page += 1
        # Close the file object
        f.close()

    print("*" * 20)
    print("Finished Scrapping!")
    print("*" * 20)

    # close Browser
    driver.quit()


main()
