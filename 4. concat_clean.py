import os
import pandas as pd
import numpy as np
import re

comparemap = 'C:\\Users\\matde\\Documents\\Projects\\Vacancy_Analytics\\compared_csv_test'
totaldf_location = 'C:\\Users\\matde\\Documents\\Projects\\Vacancy_Analytics\\total_df.csv'
totalexcel_location = 'C:\\Users\\matde\\Documents\\Projects\\Vacancy_Analytics\\total_df.xlsx'

framelist = [os.path.join(comparemap,x) for x in os.listdir(comparemap)]

total_df = pd.concat([pd.read_csv(x) for x in framelist], ignore_index = True, sort = False)

def clean_string(string):
    string = re.sub(r'\s+', ' ', string)
    string = string.strip()
    string = re.sub(r'\n', ' ', string)
    string = string.strip()

    return string

total_df['vacaturetekst'] = total_df['vacaturetekst'].apply(lambda x: clean_string(str(x)))
total_df['bedrijfskey'] = total_df['spiderkey'].replace("spider", "")

total_df.to_csv(totaldf_location, index = False)
total_df.to_excel(totalexcel_location, index = False)
