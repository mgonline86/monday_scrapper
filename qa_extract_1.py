import time
from csv import writer, DictReader
from datetime import datetime
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

ar_fees = {
    "ما قبل الروضة": "",
    "روضة": "",
    "تمهيدي": "",
    "الأول": "",
    "الثاني": "",
    "الثالث": "",
    "الرابع": "",
    "الخامس": "",
    "السادس": "",
    "السابع": "",
    "الثامن": "",
    "التاسع": "",
    "العاشر": "",
    "الحادي عشر": "",
    "الثاني عشر": "",
    "الثالث عشر": "",
}

en_fees = {
    "n": "",
    "k": "",
    "p": "",
    "1": "",
    "2": "",
    "3": "",
    "4": "",
    "5": "",
    "6": "",
    "7": "",
    "8": "",
    "9": "",
    "10": "",
    "11": "",
    "12": "",
    "13": "",
}


def extract_base():
    with open("edu_gov_qa_en.html", encoding="utf-8") as f:
        html_data = f.read()
        soup = BeautifulSoup(html_data, "html.parser")

        # Extract data from mapdataitem elements
        mapdata_items = soup.find_all("mapdataitem")

        base_url = "https://www.edu.gov.qa/"

        # Create CSV FIle to Save Data
        print("Creating CSV File!")
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f"qa_en_datatest_{now}.csv", "w", newline="", encoding="utf-8") as f2:
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f2)

            # Add CSV Header Row
            HEADERS = ["id", "name", "url", "latitude", "longitude", "flag_icon"]
            writer_object.writerow(HEADERS)

            for item in mapdata_items:
                name = item.get("title")
                flag_icon = base_url + item.get("icon")
                latitude = item.get("x")
                longitude = item.get("y")
                details = item.get("details")

                # You can further process the details using BeautifulSoup to extract information from the <a> tag
                details_soup = BeautifulSoup(details, "html.parser")

                school_link = details_soup.find("a")["href"]
                school_id = school_link[-36:]
                row = [school_id, name, school_link, latitude, longitude, flag_icon]
                writer_object.writerow(row)

            # Close the file object
            f2.close()


def main():
    service = Service()

    # instance of Options class allows us to configure Chrome
    options = webdriver.ChromeOptions()

    options.add_argument("--headless")  # Uncomment to run without UI (Headless)
    # options.page_load_strategy = 'eager'  # Don't wait for the page tp fully load
    options.add_argument("--log-level=3")  # Decrease Console Messages

    # initializing webdriver for Chrome with our options
    driver = webdriver.Chrome(service=service, options=options)

    ar_csv_file = "qa_ar_datatest_2023-12-16_20-02-28.csv"
    en_csv_file = "qa_en_datatest_2023-12-16_20-07-37.csv"

    with open(ar_csv_file, "r", encoding="utf-8") as base_f:
        dict_reader = DictReader(base_f)

        list_of_schools = list(dict_reader)
        base_f.close()

    print(f"Found {len(list_of_schools)} Schools in the CSV")

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"edu_gov_qa_full_ar_{now}.csv", "w", newline="", encoding="utf-8") as f:
        # with open(f"ar_sample.csv", "w", newline="", encoding="utf-8") as f:
        # Create CSV FIle to Save Data
        print("Creating CSV File!")
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f)

        # Add CSV Header Row
        HEADERS = [
            "id",
            "name",
            "origin_url",
            "latitude",
            "longitude",
            "flag_icon",
            "address",
            "gender",
            "website",
            "email",
            "phone",
            "img",
            "manager",
            "curriculum",
            "years",
            "accreditation",
            "offers",
            "students_count",
            "available_places",
            "fees_pre_kg",
            "fees_kg",
            "fees_pre_grade",
            "fees_grade_1",
            "fees_grade_2",
            "fees_grade_3",
            "fees_grade_4",
            "fees_grade_5",
            "fees_grade_6",
            "fees_grade_7",
            "fees_grade_8",
            "fees_grade_9",
            "fees_grade_10",
            "fees_grade_11",
            "fees_grade_12",
            "fees_grade_13",
            "vision",
            "mission",
        ]
        writer_object.writerow(HEADERS)

        empty_schools = [
            "6a64a646-9f8f-eb11-ba73-005056b39b72",
            "8e86ac40-9f8f-eb11-ba73-005056b39b72",
            "63ed7b64-b8f8-ea11-ba6c-005056b3f1dc",
            "8fd76560-3567-e311-93f9-00155d283a04",
            "56df865e-9f8f-eb11-ba73-005056b39b72",
            "1106c731-79f5-e511-80cd-74867aecd238",
            "f743b03e-a1b1-ed11-ba9f-005056b3f1dc",
            "d75097b2-0e82-e511-80c9-f8db88109e1b",
            "1cf1a62c-2a51-e911-80f2-00155d651024",
            "72fec2b3-3267-e311-93f9-00155d283a04",
            "533ab772-ce90-e911-80f4-00155da54a91",
            "ecda6560-3567-e311-93f9-00155d283a04",
            "de1c5e66-3567-e311-93f9-00155d283a04",
            "1a5ffaae-61cd-e911-ba54-005056b3f1dc",
            "72383cf5-1a2f-e711-80cf-00155d66132f",
            "0365822b-9918-e911-80f1-00155db0a48e",
            "8b44bbb9-3267-e311-93f9-00155d283a04",
            "b4d804cc-6cf0-ec11-ba8a-005056b3f1dc",
            "ad54b3c1-3d68-e311-93f9-00155d283a04",
            "3bfac2b3-3267-e311-93f9-00155d283a04",
            "4d46151c-28fa-e911-ba55-005056b3f1dc",
            "e5deadb5-3d68-e311-93f9-00155d283a04",
            "ccde9b2b-6530-e611-80ca-74867aecf65a",
            "7fc863ae-53d8-e911-ba54-005056b3f1dc",
            "79032b44-4024-ed11-ba8f-005056b3f1dc",
            "02d39e4c-9f8f-eb11-ba73-005056b39b72",
            "d6379652-9f8f-eb11-ba73-005056b39b72",
            "01c28964-9f8f-eb11-ba73-005056b39b72",
            "a6408d58-9f8f-eb11-ba73-005056b39b72",
            "d3e1b53a-9f8f-eb11-ba73-005056b39b72",
            "23b6bb34-9f8f-eb11-ba73-005056b39b72",
            "0ed29e4c-9f8f-eb11-ba73-005056b39b72",
            "921e836a-9f8f-eb11-ba73-005056b39b72",
        ]
        for school_indx, school in enumerate(list_of_schools):
            school_id = school["id"]
            school_url = school["url"]
            if not (school_id in empty_schools):
                print(f"Skipping URl[{school_indx + 1}] => {school_url}")
                continue
            school_latitude = school["latitude"]
            school_longitude = school["longitude"]
            school_flag_icon = school["flag_icon"]

            print(f"Opening URl[{school_indx + 1}] => {school_url}")

            # Opening Main Page
            driver.get(school_url)

            time.sleep(10)

            print("=" * 20)

            # School Index
            row = [school_id]

            page_html = driver.page_source
            soup = BeautifulSoup(page_html, "html.parser")

            # Extract data from school page elements
            # Getting school_name
            try:
                school_name = soup.select_one("span[id*='SchoolName']").text.strip()
            except:
                school_name = ""
            row.append(school_name)

            row.append(school_url)
            row.append(school_latitude)
            row.append(school_longitude)
            row.append(school_flag_icon)

            # Getting school_address
            try:
                school_address = soup.select_one(
                    "span[id*='SchoolAddress']"
                ).text.strip()
            except:
                school_address = ""
            row.append(school_address)

            # Getting school_gender
            try:
                school_gender = soup.select_one("span[id*='SchoolGender']").text.strip()
            except:
                school_gender = ""
            row.append(school_gender)

            # Getting school_website
            try:
                school_website = (
                    soup.select_one("a[id*='SchoolWebSite']").attrs["href"].strip()
                )
            except:
                school_website = ""
            row.append(school_website)

            # Getting school_email
            try:
                school_email = (
                    soup.select_one("a[id*='SchoolEmail']").attrs["href"][7:].strip()
                )
            except:
                school_email = ""
            row.append(school_email)

            # Getting school_phone
            try:
                school_phone = soup.select_one("span[id*='SchoolPhone']").text.strip()
            except:
                school_phone = ""
            row.append(school_phone)

            # Getting school_img
            try:
                school_img = (
                    soup.select_one("img[id*='SchoolImg']").attrs["src"].strip()
                )
            except:
                school_img = ""
            row.append(school_img)

            # Getting school_manager
            try:
                school_manager = soup.select_one(
                    "span[id*='ManagerNameResult']"
                ).text.strip()
            except:
                school_manager = ""
            row.append(school_manager)

            # Getting school_curriculum
            try:
                school_curriculum = soup.select_one(
                    "span[id*='EducationalCurriculumResult']"
                ).text.strip()
            except:
                school_curriculum = ""
            row.append(school_curriculum)

            # Getting school_years
            try:
                school_years = soup.select_one(
                    "span[id*='SchoolYearsResult']"
                ).text.strip()
            except:
                school_years = ""
            row.append(school_years)

            # Getting school_accreditation
            try:
                school_accreditation = soup.select_one(
                    "span[id*='AccreditationResult']"
                ).text.strip()
            except:
                school_accreditation = ""
            row.append(school_accreditation)

            # Getting school_offers
            try:
                school_offers = soup.select_one("span[id*='OffersResult']").text.strip()
            except:
                school_offers = ""
            row.append(school_offers)

            # Getting school_students_count
            try:
                school_students_count = soup.select_one(
                    "span[id*='StudentsNumbersResult']"
                ).text.strip()
            except:
                school_students_count = ""
            row.append(school_students_count)

            # Getting school_available_places
            try:
                school_available_places = soup.select_one(
                    "span[id*='PlacesResult']"
                ).text.strip()
            except:
                school_available_places = ""
            row.append(school_available_places)

            # Getting school_fees
            fees_dict = ar_fees.copy()
            # fees_dict = en_fees.copy()
            try:
                school_fees_table = soup.select_one("table[id*='SchoolFees']")
                school_fees_cells = school_fees_table.select("td")

                fees_dict_keys = fees_dict.keys()
                for cell in school_fees_cells:
                    try:
                        title, value = cell.select("span")
                        title = title.text.strip().lower()
                        value = value.text.strip()
                        if title in fees_dict_keys:
                            fees_dict[title] = value
                    except:
                        continue
            except:
                pass

            # AR Version
            row.append(fees_dict["ما قبل الروضة"])
            row.append(fees_dict["روضة"])
            row.append(fees_dict["تمهيدي"])
            row.append(fees_dict["الأول"])
            row.append(fees_dict["الثاني"])
            row.append(fees_dict["الثالث"])
            row.append(fees_dict["الرابع"])
            row.append(fees_dict["الخامس"])
            row.append(fees_dict["السادس"])
            row.append(fees_dict["السابع"])
            row.append(fees_dict["الثامن"])
            row.append(fees_dict["التاسع"])
            row.append(fees_dict["العاشر"])
            row.append(fees_dict["الحادي عشر"])
            row.append(fees_dict["الثاني عشر"])
            row.append(fees_dict["الثالث عشر"])

            # En Version
            # row.append(fees_dict["n"])
            # row.append(fees_dict["k"])
            # row.append(fees_dict["p"])
            # row.append(fees_dict["1"])
            # row.append(fees_dict["2"])
            # row.append(fees_dict["3"])
            # row.append(fees_dict["4"])
            # row.append(fees_dict["5"])
            # row.append(fees_dict["6"])
            # row.append(fees_dict["7"])
            # row.append(fees_dict["8"])
            # row.append(fees_dict["9"])
            # row.append(fees_dict["10"])
            # row.append(fees_dict["11"])
            # row.append(fees_dict["12"])
            # row.append(fees_dict["13"])

            # Getting school_vision_page_url
            try:
                school_vision_url = (
                    soup.select_one("a[id*='SchoolVision']").attrs["href"].strip()
                )
            except:
                school_vision_url = ""

            if school_vision_url != "":
                driver.get(school_vision_url)
                time.sleep(10)
                school_vision_page = driver.page_source
                school_vision_soup = BeautifulSoup(school_vision_page, "html.parser")

                # Getting school_vision
                try:
                    school_vision = school_vision_soup.select_one(
                        "span[id$='SchoolVision']"
                    ).text.strip()
                except:
                    school_vision = ""
                row.append(school_vision)

                # Getting school_mission
                try:
                    school_mission = school_vision_soup.select_one(
                        "span[id$='SchoolMission']"
                    ).text.strip()
                except:
                    school_mission = ""
                row.append(school_mission)
            else:
                row.append("")
                row.append("")

            writer_object.writerow(row)

    print("*" * 20)
    print("Finished Scrapping!")
    print("*" * 20)

    # close Browser
    driver.quit()


main()

# extract_single_page()
