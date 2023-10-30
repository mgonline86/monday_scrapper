import time
from csv import writer
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def main():
    service = Service()

    # instance of Options class allows us to configure Chrome
    options = webdriver.ChromeOptions()

    # options.add_argument('--headless')  # Uncomment to run without UI (Headless)
    options.page_load_strategy = 'eager'  # Don't wait for the page tp fully load

    # initializing webdriver for Chrome with our options
    driver = webdriver.Chrome(service=service, options=options)

    url = "https://monday.com/marketplace"  # starting URL

    print("Opening Browser!")
    driver.get(url)


    WebDriverWait(driver, timeout=60).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, ".app-store-menu-categories-section:nth-child(2) .app-store-menu-categories-menu-item"))
    )

    # Get Sidebar categories by Css Selector
    cats_btns = driver.find_elements(
        By.CSS_SELECTOR,
        ".app-store-menu-categories-section:nth-child(2) .app-store-menu-categories-menu-item"
    )

    print("cats_count:", len(cats_btns))
    
    # Create CSV FIle to Save Data
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"datatest_{now}.csv", "w", newline="", encoding="utf-8") as f:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f)

        # Add CSV Header Row
        HEADERS = [
            "category",
            "name",
            "developer",
            "description",
            "image",
            "tag",
            "rating",
            "rating_count",
            "install_count",
        ]
        writer_object.writerow(HEADERS)

        # Looping Categories
        for cat_i, cat in enumerate(cats_btns):
            print("=" * 20)
            print(f"Getting Category [{cat_i+1} of {len(cats_btns)}]...")
            print("=" * 20)
            cat_title = cat.text.strip()
            if cat_title == "":
                cat_title = driver.execute_script('return arguments[0].innerText', cat)
            
            # clicking each category button
            try:
                cat.click()
            except:
                driver.execute_script("arguments[0].click();", cat)
            
            time.sleep(0.5)  # wait 0.5 sec

            # Get Apps Cards
            cards = driver.find_elements(By.CSS_SELECTOR, ".ZXpi3")
            print("app cards count:", len(cards))
            # Looping App Cards
            for card_i, card in enumerate(cards):
                print(
                    f"Getting App [{card_i+1} of {len(cards)}] in Category[{cat_i+1} of {len(cats_btns)}]..."
                )
                row = [cat_title]

                # App Name
                try:
                    name = card.find_element(
                        By.CSS_SELECTOR, "div[class*='AppName']"
                    ).text.strip()
                    row.append(name)
                except:
                    row.append("")

                # App Developer
                try:
                    developer = card.find_element(
                        By.CSS_SELECTOR, "div[class*='FeaturedCardSubHeader']"
                    ).text.strip()
                    developer = developer.replace("By ", "")  # Removing Prefix Phrase
                    row.append(developer)
                except:
                    row.append("")

                # App Description
                try:
                    description = card.find_element(
                        By.CSS_SELECTOR, "div[class*='FeaturedCardContent']"
                    ).text.strip()
                    row.append(description)
                except:
                    row.append("")

                # App Image
                try:
                    image = card.find_element(
                        By.CSS_SELECTOR, ".app-icon__photo"
                    ).get_attribute("src")
                    row.append(image)
                except:
                    row.append("")

                # App Tag
                try:
                    tag = card.find_element(
                        By.CSS_SELECTOR, "div[data-testid='chip']"
                    ).text.strip()
                    row.append(tag)
                except:
                    row.append("")

                # App Rating
                try:
                    rating = card.find_element(
                        By.CSS_SELECTOR, "div[class*='appAvgRating']"
                    ).text.strip()
                    row.append(rating)
                except:
                    row.append("")

                # App Rating Count
                try:
                    rating_count = card.find_element(
                        By.CSS_SELECTOR,
                        "div[class*='appsStoreAppRatingScore']>div:nth-child(3)",
                    ).text.strip()

                    rating_count = rating_count.replace("(", "").replace(
                        ")", ""
                    )  # remove Brackets
                    row.append(rating_count)
                except:
                    row.append("")

                # App Install Count
                try:
                    install_count = card.find_element(
                        By.CSS_SELECTOR, "div[class*='AppInstallCount']"
                    ).text.strip()

                    row.append(install_count)
                except:
                    row.append("")

                # Save App Data to CSV File
                writer_object.writerow(row)

        # Close the file object
        f.close()


    print("*"*20)
    print("Finished Scrapping!")
    print("*"*20)

    # close Browser
    driver.quit()


main()
