from csv import writer, DictReader
from ast import literal_eval

with open("en_accred_prices_2023-11-29_23-40-13.csv", "r", encoding="utf-8") as file:
    csv_reader = DictReader(file)
    data = [row for row in csv_reader]


def str_2_list(d):
    accreditation = []
    fees = []
    try:
        accreditation = literal_eval(d["accreditation"])
    except:
        pass
    try:
        fees = literal_eval(d["fees"])
    except:
        pass
    d.update(accreditation=accreditation, fees=fees)
    return d


data_refined = list(map(lambda x: str_2_list(x), data))

HEADERS = [
    "index",
    "origin_url",
    "name",
    "accreditation_1_title",
    "accreditation_1_img",
    "accreditation_2_title",
    "accreditation_2_img",
    "accreditation_3_title",
    "accreditation_3_img",
    "fees_1_title",
    "fees_1_boys_kg_1",
    "fees_1_boys_kg_2",
    "fees_1_boys_kg_3",
    "fees_1_boys_grade_1",
    "fees_1_boys_grade_2",
    "fees_1_boys_grade_3",
    "fees_1_boys_grade_4",
    "fees_1_boys_grade_5",
    "fees_1_boys_grade_6",
    "fees_1_boys_grade_7",
    "fees_1_boys_grade_8",
    "fees_1_boys_grade_9",
    "fees_1_boys_grade_10",
    "fees_1_boys_grade_11",
    "fees_1_boys_grade_12",
    "fees_1_girls_kg_1",
    "fees_1_girls_kg_2",
    "fees_1_girls_kg_3",
    "fees_1_girls_grade_1",
    "fees_1_girls_grade_2",
    "fees_1_girls_grade_3",
    "fees_1_girls_grade_4",
    "fees_1_girls_grade_5",
    "fees_1_girls_grade_6",
    "fees_1_girls_grade_7",
    "fees_1_girls_grade_8",
    "fees_1_girls_grade_9",
    "fees_1_girls_grade_10",
    "fees_1_girls_grade_11",
    "fees_1_girls_grade_12",
    "fees_2_title",
    "fees_2_boys_kg_1",
    "fees_2_boys_kg_2",
    "fees_2_boys_kg_3",
    "fees_2_boys_grade_1",
    "fees_2_boys_grade_2",
    "fees_2_boys_grade_3",
    "fees_2_boys_grade_4",
    "fees_2_boys_grade_5",
    "fees_2_boys_grade_6",
    "fees_2_boys_grade_7",
    "fees_2_boys_grade_8",
    "fees_2_boys_grade_9",
    "fees_2_boys_grade_10",
    "fees_2_boys_grade_11",
    "fees_2_boys_grade_12",
    "fees_2_girls_kg_1",
    "fees_2_girls_kg_2",
    "fees_2_girls_kg_3",
    "fees_2_girls_grade_1",
    "fees_2_girls_grade_2",
    "fees_2_girls_grade_3",
    "fees_2_girls_grade_4",
    "fees_2_girls_grade_5",
    "fees_2_girls_grade_6",
    "fees_2_girls_grade_7",
    "fees_2_girls_grade_8",
    "fees_2_girls_grade_9",
    "fees_2_girls_grade_10",
    "fees_2_girls_grade_11",
    "fees_2_girls_grade_12",
    "fees_3_title",
    "fees_3_boys_kg_1",
    "fees_3_boys_kg_2",
    "fees_3_boys_kg_3",
    "fees_3_boys_grade_1",
    "fees_3_boys_grade_2",
    "fees_3_boys_grade_3",
    "fees_3_boys_grade_4",
    "fees_3_boys_grade_5",
    "fees_3_boys_grade_6",
    "fees_3_boys_grade_7",
    "fees_3_boys_grade_8",
    "fees_3_boys_grade_9",
    "fees_3_boys_grade_10",
    "fees_3_boys_grade_11",
    "fees_3_boys_grade_12",
    "fees_3_girls_kg_1",
    "fees_3_girls_kg_2",
    "fees_3_girls_kg_3",
    "fees_3_girls_grade_1",
    "fees_3_girls_grade_2",
    "fees_3_girls_grade_3",
    "fees_3_girls_grade_4",
    "fees_3_girls_grade_5",
    "fees_3_girls_grade_6",
    "fees_3_girls_grade_7",
    "fees_3_girls_grade_8",
    "fees_3_girls_grade_9",
    "fees_3_girls_grade_10",
    "fees_3_girls_grade_11",
    "fees_3_girls_grade_12",
]


def flatten(dct):
    try:
        index = dct["index"]
    except:
        index = ""
    try:
        origin_url = dct["origin_url"]
    except:
        origin_url = ""
    try:
        name = dct["name"]
    except:
        name = ""
    try:
        accreditation_1_title = dct["accreditation"][0][0]
    except:
        accreditation_1_title = ""
    try:
        accreditation_1_img = dct["accreditation"][0][1]
    except:
        accreditation_1_img = ""
    try:
        accreditation_2_title = dct["accreditation"][1][0]
    except:
        accreditation_2_title = ""
    try:
        accreditation_2_img = dct["accreditation"][1][1]
    except:
        accreditation_2_img = ""
    try:
        accreditation_3_title = dct["accreditation"][2][0]
    except:
        accreditation_3_title = ""
    try:
        accreditation_3_img = dct["accreditation"][2][1]
    except:
        accreditation_3_img = ""
    try:
        fees_1_title = dct["fees"][0][0]
    except:
        fees_1_title = ""
    try:
        fees_1_boys_kg_1 = dct["fees"][0][1][0][0]
    except:
        fees_1_boys_kg_1 = ""
    try:
        fees_1_boys_kg_2 = dct["fees"][0][1][0][1]
    except:
        fees_1_boys_kg_2 = ""
    try:
        fees_1_boys_kg_3 = dct["fees"][0][1][0][2]
    except:
        fees_1_boys_kg_3 = ""
    try:
        fees_1_boys_grade_1 = dct["fees"][0][1][0][3]
    except:
        fees_1_boys_grade_1 = ""
    try:
        fees_1_boys_grade_2 = dct["fees"][0][1][0][4]
    except:
        fees_1_boys_grade_2 = ""
    try:
        fees_1_boys_grade_3 = dct["fees"][0][1][0][5]
    except:
        fees_1_boys_grade_3 = ""
    try:
        fees_1_boys_grade_4 = dct["fees"][0][1][0][6]
    except:
        fees_1_boys_grade_4 = ""
    try:
        fees_1_boys_grade_5 = dct["fees"][0][1][0][7]
    except:
        fees_1_boys_grade_5 = ""
    try:
        fees_1_boys_grade_6 = dct["fees"][0][1][0][8]
    except:
        fees_1_boys_grade_6 = ""
    try:
        fees_1_boys_grade_7 = dct["fees"][0][1][0][9]
    except:
        fees_1_boys_grade_7 = ""
    try:
        fees_1_boys_grade_8 = dct["fees"][0][1][0][10]
    except:
        fees_1_boys_grade_8 = ""
    try:
        fees_1_boys_grade_9 = dct["fees"][0][1][0][11]
    except:
        fees_1_boys_grade_9 = ""
    try:
        fees_1_boys_grade_10 = dct["fees"][0][1][0][12]
    except:
        fees_1_boys_grade_10 = ""
    try:
        fees_1_boys_grade_11 = dct["fees"][0][1][0][13]
    except:
        fees_1_boys_grade_11 = ""
    try:
        fees_1_boys_grade_12 = dct["fees"][0][1][0][14]
    except:
        fees_1_boys_grade_12 = ""
    try:
        fees_1_girls_kg_1 = dct["fees"][0][1][1][0]
    except:
        fees_1_girls_kg_1 = ""
    try:
        fees_1_girls_kg_2 = dct["fees"][0][1][1][1]
    except:
        fees_1_girls_kg_2 = ""
    try:
        fees_1_girls_kg_3 = dct["fees"][0][1][1][2]
    except:
        fees_1_girls_kg_3 = ""
    try:
        fees_1_girls_grade_1 = dct["fees"][0][1][1][3]
    except:
        fees_1_girls_grade_1 = ""
    try:
        fees_1_girls_grade_2 = dct["fees"][0][1][1][4]
    except:
        fees_1_girls_grade_2 = ""
    try:
        fees_1_girls_grade_3 = dct["fees"][0][1][1][5]
    except:
        fees_1_girls_grade_3 = ""
    try:
        fees_1_girls_grade_4 = dct["fees"][0][1][1][6]
    except:
        fees_1_girls_grade_4 = ""
    try:
        fees_1_girls_grade_5 = dct["fees"][0][1][1][7]
    except:
        fees_1_girls_grade_5 = ""
    try:
        fees_1_girls_grade_6 = dct["fees"][0][1][1][8]
    except:
        fees_1_girls_grade_6 = ""
    try:
        fees_1_girls_grade_7 = dct["fees"][0][1][1][9]
    except:
        fees_1_girls_grade_7 = ""
    try:
        fees_1_girls_grade_8 = dct["fees"][0][1][1][10]
    except:
        fees_1_girls_grade_8 = ""
    try:
        fees_1_girls_grade_9 = dct["fees"][0][1][1][11]
    except:
        fees_1_girls_grade_9 = ""
    try:
        fees_1_girls_grade_10 = dct["fees"][0][1][1][12]
    except:
        fees_1_girls_grade_10 = ""
    try:
        fees_1_girls_grade_11 = dct["fees"][0][1][1][13]
    except:
        fees_1_girls_grade_11 = ""
    try:
        fees_1_girls_grade_12 = dct["fees"][0][1][1][14]
    except:
        fees_1_girls_grade_12 = ""
    try:
        fees_2_title = dct["fees"][1][0]
    except:
        fees_2_title = ""
    try:
        fees_2_boys_kg_1 = dct["fees"][1][1][0][0]
    except:
        fees_2_boys_kg_1 = ""
    try:
        fees_2_boys_kg_2 = dct["fees"][1][1][0][1]
    except:
        fees_2_boys_kg_2 = ""
    try:
        fees_2_boys_kg_3 = dct["fees"][1][1][0][2]
    except:
        fees_2_boys_kg_3 = ""
    try:
        fees_2_boys_grade_1 = dct["fees"][1][1][0][3]
    except:
        fees_2_boys_grade_1 = ""
    try:
        fees_2_boys_grade_2 = dct["fees"][1][1][0][4]
    except:
        fees_2_boys_grade_2 = ""
    try:
        fees_2_boys_grade_3 = dct["fees"][1][1][0][5]
    except:
        fees_2_boys_grade_3 = ""
    try:
        fees_2_boys_grade_4 = dct["fees"][1][1][0][6]
    except:
        fees_2_boys_grade_4 = ""
    try:
        fees_2_boys_grade_5 = dct["fees"][1][1][0][7]
    except:
        fees_2_boys_grade_5 = ""
    try:
        fees_2_boys_grade_6 = dct["fees"][1][1][0][8]
    except:
        fees_2_boys_grade_6 = ""
    try:
        fees_2_boys_grade_7 = dct["fees"][1][1][0][9]
    except:
        fees_2_boys_grade_7 = ""
    try:
        fees_2_boys_grade_8 = dct["fees"][1][1][0][10]
    except:
        fees_2_boys_grade_8 = ""
    try:
        fees_2_boys_grade_9 = dct["fees"][1][1][0][11]
    except:
        fees_2_boys_grade_9 = ""
    try:
        fees_2_boys_grade_10 = dct["fees"][1][1][0][12]
    except:
        fees_2_boys_grade_10 = ""
    try:
        fees_2_boys_grade_11 = dct["fees"][1][1][0][13]
    except:
        fees_2_boys_grade_11 = ""
    try:
        fees_2_boys_grade_12 = dct["fees"][1][1][0][14]
    except:
        fees_2_boys_grade_12 = ""
    try:
        fees_2_girls_kg_1 = dct["fees"][1][1][1][0]
    except:
        fees_2_girls_kg_1 = ""
    try:
        fees_2_girls_kg_2 = dct["fees"][1][1][1][1]
    except:
        fees_2_girls_kg_2 = ""
    try:
        fees_2_girls_kg_3 = dct["fees"][1][1][1][2]
    except:
        fees_2_girls_kg_3 = ""
    try:
        fees_2_girls_grade_1 = dct["fees"][1][1][1][3]
    except:
        fees_2_girls_grade_1 = ""
    try:
        fees_2_girls_grade_2 = dct["fees"][1][1][1][4]
    except:
        fees_2_girls_grade_2 = ""
    try:
        fees_2_girls_grade_3 = dct["fees"][1][1][1][5]
    except:
        fees_2_girls_grade_3 = ""
    try:
        fees_2_girls_grade_4 = dct["fees"][1][1][1][6]
    except:
        fees_2_girls_grade_4 = ""
    try:
        fees_2_girls_grade_5 = dct["fees"][1][1][1][7]
    except:
        fees_2_girls_grade_5 = ""
    try:
        fees_2_girls_grade_6 = dct["fees"][1][1][1][8]
    except:
        fees_2_girls_grade_6 = ""
    try:
        fees_2_girls_grade_7 = dct["fees"][1][1][1][9]
    except:
        fees_2_girls_grade_7 = ""
    try:
        fees_2_girls_grade_8 = dct["fees"][1][1][1][10]
    except:
        fees_2_girls_grade_8 = ""
    try:
        fees_2_girls_grade_9 = dct["fees"][1][1][1][11]
    except:
        fees_2_girls_grade_9 = ""
    try:
        fees_2_girls_grade_10 = dct["fees"][1][1][1][12]
    except:
        fees_2_girls_grade_10 = ""
    try:
        fees_2_girls_grade_11 = dct["fees"][1][1][1][13]
    except:
        fees_2_girls_grade_11 = ""
    try:
        fees_2_girls_grade_12 = dct["fees"][1][1][1][14]
    except:
        fees_2_girls_grade_12 = ""
    try:
        fees_3_title = dct["fees"][2][0]
    except:
        fees_3_title = ""
    try:
        fees_3_boys_kg_1 = dct["fees"][2][1][0][0]
    except:
        fees_3_boys_kg_1 = ""
    try:
        fees_3_boys_kg_2 = dct["fees"][2][1][0][1]
    except:
        fees_3_boys_kg_2 = ""
    try:
        fees_3_boys_kg_3 = dct["fees"][2][1][0][2]
    except:
        fees_3_boys_kg_3 = ""
    try:
        fees_3_boys_grade_1 = dct["fees"][2][1][0][3]
    except:
        fees_3_boys_grade_1 = ""
    try:
        fees_3_boys_grade_2 = dct["fees"][2][1][0][4]
    except:
        fees_3_boys_grade_2 = ""
    try:
        fees_3_boys_grade_3 = dct["fees"][2][1][0][5]
    except:
        fees_3_boys_grade_3 = ""
    try:
        fees_3_boys_grade_4 = dct["fees"][2][1][0][6]
    except:
        fees_3_boys_grade_4 = ""
    try:
        fees_3_boys_grade_5 = dct["fees"][2][1][0][7]
    except:
        fees_3_boys_grade_5 = ""
    try:
        fees_3_boys_grade_6 = dct["fees"][2][1][0][8]
    except:
        fees_3_boys_grade_6 = ""
    try:
        fees_3_boys_grade_7 = dct["fees"][2][1][0][9]
    except:
        fees_3_boys_grade_7 = ""
    try:
        fees_3_boys_grade_8 = dct["fees"][2][1][0][10]
    except:
        fees_3_boys_grade_8 = ""
    try:
        fees_3_boys_grade_9 = dct["fees"][2][1][0][11]
    except:
        fees_3_boys_grade_9 = ""
    try:
        fees_3_boys_grade_10 = dct["fees"][2][1][0][12]
    except:
        fees_3_boys_grade_10 = ""
    try:
        fees_3_boys_grade_11 = dct["fees"][2][1][0][13]
    except:
        fees_3_boys_grade_11 = ""
    try:
        fees_3_boys_grade_12 = dct["fees"][2][1][0][14]
    except:
        fees_3_boys_grade_12 = ""
    try:
        fees_3_girls_kg_1 = dct["fees"][2][1][1][0]
    except:
        fees_3_girls_kg_1 = ""
    try:
        fees_3_girls_kg_2 = dct["fees"][2][1][1][1]
    except:
        fees_3_girls_kg_2 = ""
    try:
        fees_3_girls_kg_3 = dct["fees"][2][1][1][2]
    except:
        fees_3_girls_kg_3 = ""
    try:
        fees_3_girls_grade_1 = dct["fees"][2][1][1][3]
    except:
        fees_3_girls_grade_1 = ""
    try:
        fees_3_girls_grade_2 = dct["fees"][2][1][1][4]
    except:
        fees_3_girls_grade_2 = ""
    try:
        fees_3_girls_grade_3 = dct["fees"][2][1][1][5]
    except:
        fees_3_girls_grade_3 = ""
    try:
        fees_3_girls_grade_4 = dct["fees"][2][1][1][6]
    except:
        fees_3_girls_grade_4 = ""
    try:
        fees_3_girls_grade_5 = dct["fees"][2][1][1][7]
    except:
        fees_3_girls_grade_5 = ""
    try:
        fees_3_girls_grade_6 = dct["fees"][2][1][1][8]
    except:
        fees_3_girls_grade_6 = ""
    try:
        fees_3_girls_grade_7 = dct["fees"][2][1][1][9]
    except:
        fees_3_girls_grade_7 = ""
    try:
        fees_3_girls_grade_8 = dct["fees"][2][1][1][10]
    except:
        fees_3_girls_grade_8 = ""
    try:
        fees_3_girls_grade_9 = dct["fees"][2][1][1][11]
    except:
        fees_3_girls_grade_9 = ""
    try:
        fees_3_girls_grade_10 = dct["fees"][2][1][1][12]
    except:
        fees_3_girls_grade_10 = ""
    try:
        fees_3_girls_grade_11 = dct["fees"][2][1][1][13]
    except:
        fees_3_girls_grade_11 = ""
    try:
        fees_3_girls_grade_12 = dct["fees"][2][1][1][14]
    except:
        fees_3_girls_grade_12 = ""

    output = [
        index,
        origin_url,
        name,
        accreditation_1_title,
        accreditation_1_img,
        accreditation_2_title,
        accreditation_2_img,
        accreditation_3_title,
        accreditation_3_img,
        fees_1_title,
        fees_1_boys_kg_1,
        fees_1_boys_kg_2,
        fees_1_boys_kg_3,
        fees_1_boys_grade_1,
        fees_1_boys_grade_2,
        fees_1_boys_grade_3,
        fees_1_boys_grade_4,
        fees_1_boys_grade_5,
        fees_1_boys_grade_6,
        fees_1_boys_grade_7,
        fees_1_boys_grade_8,
        fees_1_boys_grade_9,
        fees_1_boys_grade_10,
        fees_1_boys_grade_11,
        fees_1_boys_grade_12,
        fees_1_girls_kg_1,
        fees_1_girls_kg_2,
        fees_1_girls_kg_3,
        fees_1_girls_grade_1,
        fees_1_girls_grade_2,
        fees_1_girls_grade_3,
        fees_1_girls_grade_4,
        fees_1_girls_grade_5,
        fees_1_girls_grade_6,
        fees_1_girls_grade_7,
        fees_1_girls_grade_8,
        fees_1_girls_grade_9,
        fees_1_girls_grade_10,
        fees_1_girls_grade_11,
        fees_1_girls_grade_12,
        fees_2_title,
        fees_2_boys_kg_1,
        fees_2_boys_kg_2,
        fees_2_boys_kg_3,
        fees_2_boys_grade_1,
        fees_2_boys_grade_2,
        fees_2_boys_grade_3,
        fees_2_boys_grade_4,
        fees_2_boys_grade_5,
        fees_2_boys_grade_6,
        fees_2_boys_grade_7,
        fees_2_boys_grade_8,
        fees_2_boys_grade_9,
        fees_2_boys_grade_10,
        fees_2_boys_grade_11,
        fees_2_boys_grade_12,
        fees_2_girls_kg_1,
        fees_2_girls_kg_2,
        fees_2_girls_kg_3,
        fees_2_girls_grade_1,
        fees_2_girls_grade_2,
        fees_2_girls_grade_3,
        fees_2_girls_grade_4,
        fees_2_girls_grade_5,
        fees_2_girls_grade_6,
        fees_2_girls_grade_7,
        fees_2_girls_grade_8,
        fees_2_girls_grade_9,
        fees_2_girls_grade_10,
        fees_2_girls_grade_11,
        fees_2_girls_grade_12,
        fees_3_title,
        fees_3_boys_kg_1,
        fees_3_boys_kg_2,
        fees_3_boys_kg_3,
        fees_3_boys_grade_1,
        fees_3_boys_grade_2,
        fees_3_boys_grade_3,
        fees_3_boys_grade_4,
        fees_3_boys_grade_5,
        fees_3_boys_grade_6,
        fees_3_boys_grade_7,
        fees_3_boys_grade_8,
        fees_3_boys_grade_9,
        fees_3_boys_grade_10,
        fees_3_boys_grade_11,
        fees_3_boys_grade_12,
        fees_3_girls_kg_1,
        fees_3_girls_kg_2,
        fees_3_girls_kg_3,
        fees_3_girls_grade_1,
        fees_3_girls_grade_2,
        fees_3_girls_grade_3,
        fees_3_girls_grade_4,
        fees_3_girls_grade_5,
        fees_3_girls_grade_6,
        fees_3_girls_grade_7,
        fees_3_girls_grade_8,
        fees_3_girls_grade_9,
        fees_3_girls_grade_10,
        fees_3_girls_grade_11,
        fees_3_girls_grade_12,
    ]

    return output


# print(flatten(data_refined[0]))

with open(f"en_accred_prices_processed_2023-11-29_23-40-13.csv", "w", newline="", encoding="utf-8") as f:
    writer_object = writer(f)

    # Add CSV Header Row
    writer_object.writerow(HEADERS)

    for itm in data_refined:
        row = flatten(itm)
        writer_object.writerow(row)
