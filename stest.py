import time
import re
from csv import writer, DictReader
from datetime import datetime
from urllib.parse import unquote

from selenium import webdriver
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


"""
اسم
رقم
تليفون
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

    options.add_argument("--headless")  # Uncomment to run without UI (Headless)
    # options.page_load_strategy = 'eager'  # Don't wait for the page tp fully load
    options.add_argument("--log-level=3")  # Decrease Console Messages

    # initializing webdriver for Chrome with our options
    driver = webdriver.Chrome(service=service, options=options)

    ar_csv_file = "ar_datatest_2023-11-22_13-19-55.csv"
    en_csv_file = "en_datatest_2023-11-22_13-25-45.csv"

    with open(en_csv_file, "r", encoding="utf-8") as f:
        dict_reader = DictReader(f)

        list_of_schools = list(dict_reader)

    print(f"Found {len(list_of_schools)} Schools in the CSV")

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"en_accred_prices_{now}.csv", "w", newline="", encoding="utf-8") as f:
        # with open(f"ar_sample.csv", "w", newline="", encoding="utf-8") as f:
        # Create CSV FIle to Save Data
        print("Creating CSV File!")
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f)

        # Add CSV Header Row
        HEADERS = [
            "index",
            "origin_url",
            "name",
            "accreditation",
            "fees",
            # "logo_img",
            # "description",
            # "type",
            # "curriculum",
            # "stages",
            # "genders",
            # "phones",
            # "address",
            # "location",
            # "email",
            # "website",
            # "working_hours",
            # "facebook",
            # "youtube",
            # "instgram",
            # "whatsapp",
            # "twitter",
            # "rating_of_5",
            # "rating_count",
            # "images",
        ]
        writer_object.writerow(HEADERS)

        for school_indx, school in enumerate(list_of_schools):
            school_index = school["index"]
            school_name = school["name"]
            school_url = school["url"]

            print(f"Opening URl[{school_indx + 1}] => {school_url}")

            # Opening Main Page
            driver.get(school_url)

            # Wait to Page Loader to finsih
            print("Waiting 10 Sec for Loader to Finish!")
            time.sleep(10)

            print("=" * 20)

            # School Index
            row = [school_index, school_url, school_name]

            # # School Logo Image
            # print("Getting School Logo Image...")
            # try:
            #     school_logo_image = driver.find_element(
            #         By.CSS_SELECTOR, ".header-section .school-info-section-xl img"
            #     )
            #     row.append(school_logo_image.get_attribute("data-src").strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Description
            # print("Getting School Description...")
            # try:
            #     school_description = driver.find_element(
            #         By.CSS_SELECTOR, "#pills-about"
            #     )
            #     row.append(school_description.text.strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Type
            # print("Getting School Type...")
            # try:
            #     school_type = driver.find_element(
            #         By.CSS_SELECTOR, "#schoolMainData>div>div>div:nth-child(1)>b"
            #     )
            #     row.append(school_type.text.strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Curriculum
            # print("Getting School Curriculum...")
            # try:
            #     school_curriculum = driver.find_element(
            #         By.CSS_SELECTOR, "#schoolMainData>div>div>div:nth-child(2)>b"
            #     )
            #     row.append(school_curriculum.text.strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Stages
            # print("Getting School Stages...")
            # try:
            #     school_stages = driver.find_element(
            #         By.CSS_SELECTOR, "#schoolMainData>div>div>div:nth-child(3)>b"
            #     )
            #     row.append(school_stages.text.strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Genders
            # print("Getting School Genders...")
            # try:
            #     school_genders = driver.find_element(
            #         By.CSS_SELECTOR, "#schoolMainData>div>div>div:nth-child(4)>b"
            #     )
            #     row.append(school_genders.text.strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Phones
            # print("Getting School Phones...")
            # try:
            #     school_phones_list = driver.find_elements(
            #         By.CSS_SELECTOR, ".school-contact a[href^='tel:']:not(.mb-2)"
            #     )
            #     school_phones = list(
            #         map(
            #             lambda ph: ph.get_attribute("href")[4:].strip(),
            #             school_phones_list,
            #         )
            #     )
            #     school_phones_nums = ", ".join(school_phones)
            #     row.append(school_phones_nums)
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Address
            # print("Getting School Address...")
            # try:
            #     school_address = driver.find_element(
            #         By.CSS_SELECTOR, ".school-contact p[itemprop='addressLocality']"
            #     )
            #     row.append(school_address.get_attribute("innerText").strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Location
            # print("Getting School Location...")
            # try:
            #     school_location = driver.find_element(
            #         By.CSS_SELECTOR, "#school_map>iframe"
            #     )
            #     row.append(
            #         school_location.get_attribute("src")
            #         .replace("embed/v1/", "")
            #         .strip()
            #     )
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Email
            # print("Getting School Email...")
            # try:
            #     school_email = driver.find_element(
            #         By.CSS_SELECTOR, ".school-contact a[href^='mailto:']:not(.mb-2)"
            #     )
            #     row.append(school_email.get_attribute("innerText").strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Website
            # print("Getting School Website...")
            # try:
            #     school_website = driver.find_element(
            #         By.CSS_SELECTOR, ".school-contact i.fa-globe-africa + a"
            #     )
            #     row.append(unquote(school_website.get_attribute("href").strip()))
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Working Hours
            # print("Getting School Working Hours...")
            # try:
            #     school_working_hours_icon = driver.find_element(
            #         By.CSS_SELECTOR, ".school-contact i.fa-clock:not(.mb-2)"
            #     )
            #     school_working_hours = driver.execute_script(
            #         "return arguments[0].parentNode;", school_working_hours_icon
            #     )

            #     row.append(school_working_hours.get_attribute("innerText").strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Facebook
            # print("Getting School Facebook...")
            # try:
            #     school_facebook_icon = driver.find_element(
            #         By.CSS_SELECTOR, ".school-contact i.fa-facebook"
            #     )
            #     school_facebook = driver.execute_script(
            #         "return arguments[0].parentNode;", school_facebook_icon
            #     )
            #     row.append(school_facebook.get_attribute("href").strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Youtube
            # print("Getting School Youtube...")
            # try:
            #     school_youtube_icon = driver.find_element(
            #         By.CSS_SELECTOR, ".school-contact i.fa-youtube"
            #     )
            #     school_youtube = driver.execute_script(
            #         "return arguments[0].parentNode;", school_youtube_icon
            #     )
            #     row.append(school_youtube.get_attribute("href").strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Instagram
            # print("Getting School Instagram...")
            # try:
            #     school_instagram_icon = driver.find_element(
            #         By.CSS_SELECTOR, ".school-contact i.fa-instagram"
            #     )
            #     school_instagram = driver.execute_script(
            #         "return arguments[0].parentNode;", school_instagram_icon
            #     )
            #     row.append(school_instagram.get_attribute("href").strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Whatsapp
            # print("Getting School Whatsapp...")
            # try:
            #     school_whatsapp_icon = driver.find_element(
            #         By.CSS_SELECTOR, ".school-contact i.fa-whatsapp"
            #     )
            #     school_whatsapp = driver.execute_script(
            #         "return arguments[0].parentNode;", school_whatsapp_icon
            #     )
            #     row.append(school_whatsapp.get_attribute("href").strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Twitter
            # print("Getting School Twitter...")
            # try:
            #     school_twitter_icon = driver.find_element(
            #         By.CSS_SELECTOR, ".school-contact i.fa-twitter"
            #     )
            #     school_twitter = driver.execute_script(
            #         "return arguments[0].parentNode;", school_twitter_icon
            #     )
            #     row.append(school_twitter.get_attribute("href").strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Rating
            # print("Getting School Rating...")
            # try:
            #     school_rating = driver.find_element(
            #         By.CSS_SELECTOR, ".ratebadge span:not(.d-none)"
            #     )
            #     row.append(school_rating.get_attribute("innerText").strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School Rating Count
            # print("Getting School Rating Count...")
            # try:
            #     school_rating_count = driver.find_element(
            #         By.CSS_SELECTOR, "span[itemprop='ratingCount']"
            #     )
            #     row.append(school_rating_count.get_attribute("innerText").strip())
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # # School images
            # print("Getting School images...")
            # try:
            #     school_images_list = driver.find_elements(
            #         By.CSS_SELECTOR, "#schoolGallerySlider .img-container"
            #     )
            #     school_images = ", ".join(
            #         list(
            #             map(
            #                 lambda x: re.split(
            #                     "[()]", x.value_of_css_property("background-image")
            #                 )[1]
            #                 .replace('"', "")
            #                 .strip(),
            #                 school_images_list,
            #             )
            #         )
            #     )
            #     row.append(school_images)
            # except Exception as err:
            #     print(err)
            #     row.append("")

            # School Accreditation
            print("Getting School Accreditation...")
            try:
                school_accreditation_tab_btn = driver.find_element(
                    By.CSS_SELECTOR, "#pills-accreditation-tab"
                )

                driver.execute_script(
                    "arguments[0].click();", school_accreditation_tab_btn
                )

                time.sleep(5)  # waiting for accreditation to load
                print("Waiting 5 Sec for Accreditation to Load!")

                school_accreditation_tab = driver.find_element(
                    By.CSS_SELECTOR, "#pills-accreditation"
                )
                school_accreditation_cards = school_accreditation_tab.find_elements(
                    By.CSS_SELECTOR, ".col-12 .col-md-3"
                )
                accreditations = []
                for card in school_accreditation_cards:
                    accreditation = []

                    # get accreditation title if exists
                    try:
                        title = card.find_element(By.CSS_SELECTOR, ".card-title")
                        accreditation.append(title.text.strip())
                    except Exception as err:
                        accreditation.append("")
                        print(err)

                    # get accreditation image if exists
                    try:
                        img_src = card.find_element(
                            By.CSS_SELECTOR, "img"
                        ).get_attribute("src")
                        accreditation.append(img_src.strip())
                    except Exception as err:
                        accreditation.append("")
                        print(err)
                    accreditations.append(accreditation)

                row.append(accreditations)
            except Exception as err:
                print(err)
                row.append("")

            # School Fees
            print("Getting School Fees...")
            try:
                school_fees_btns = driver.find_elements(
                    By.CSS_SELECTOR, "#fees-tab li button"
                )
                fees = []

                for btn in school_fees_btns:
                    fee = []
                    classrooms = {
                        "KG1": ("", ""),
                        "KG2": ("", ""),
                        "KG3": ("", ""),
                        "GRADE 1": ("", ""),
                        "GRADE 2": ("", ""),
                        "GRADE 3": ("", ""),
                        "GRADE 4": ("", ""),
                        "GRADE 5": ("", ""),
                        "GRADE 6": ("", ""),
                        "GRADE 7": ("", ""),
                        "GRADE 8": ("", ""),
                        "GRADE 9": ("", ""),
                        "GRADE 10": ("", ""),
                        "GRADE 11": ("", ""),
                        "GRADE 12": ("", ""),
                    }

                    # Get Fee Title
                    try:
                        fee_title = btn.text
                        fee.append(fee_title.strip())
                    except Exception as err:
                        print(err)
                        fee.append("")

                    # Get Fee data
                    try:
                        fee_table_id = btn.get_attribute("data-bs-target").strip()
                        rows_selector = fee_table_id + " tr"
                        fee_table_rows = driver.find_elements(
                            By.CSS_SELECTOR, rows_selector
                        )
                        school_genders = "both"
                        fee_table_headers = fee_table_rows[0].find_elements(
                            By.CSS_SELECTOR, "th"
                        )
                        fee_table_headers_len = len(fee_table_headers)
                        if fee_table_headers_len == 3:
                            school_genders = (
                                "boys"
                                if "boys" in fee_table_headers[1].text.lower()
                                else "girls"
                            )
                        for table_row in fee_table_rows[1:]:
                            try:
                                cells = table_row.find_elements(By.CSS_SELECTOR, "td")
                                if school_genders == "both":
                                    classroom, b_fee, g_fee, _ = [
                                        cell.get_attribute("innerText").strip()
                                        for cell in cells
                                    ]
                                    classrooms[classroom.upper()] = (b_fee, g_fee)
                                if school_genders == "boys":
                                    classroom, b_fee, _ = [
                                        cell.get_attribute("innerText").strip()
                                        for cell in cells
                                    ]
                                    classrooms[classroom.upper()] = (b_fee, "")
                                if school_genders == "girls":
                                    classroom, g_fee, _ = [
                                        cell.get_attribute("innerText").strip()
                                        for cell in cells
                                    ]
                                    classrooms[classroom.upper()] = ("", g_fee)
                            except Exception as err:
                                print(err)
                        fee.append([list(t) for t in zip(*classrooms.values())])

                    except Exception as err:
                        print(err)
                        fee.append([])

                    fees.append(fee)

                row.append(fees)
            except Exception as err:
                print(err)
                row.append([])

            writer_object.writerow(row)

    print("*" * 20)
    print("Finished Scrapping!")
    print("*" * 20)

    # close Browser
    driver.quit()

main()
