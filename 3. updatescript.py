import os
import pandas as pd
# import numpy as np
# import path
import datetime

webmap = 'C:\\Users\\matde\\documents\\projects\\vacancy_analytics\\output_test'
comparemap = 'C:\\Users\\matde\\documents\\projects\\vacancy_analytics\\compared_csv_test'

def check_for_new(dfnew, dfold):
    for key in dfnew['compositekey']:

        if key not in dfold['compositekey'].values:

            dfnew['new'][dfnew['compositekey'] == key] = 1
            dfold = dfold.append(dfnew[dfnew['compositekey'] == key])

            dfold.reset_index(drop = True, inplace = True)

    # dfnewappended = dfold

    return dfold

def check_for_expired(dfnew, dfold):

    for key in dfold['compositekey']:

        if key not in dfnew['compositekey'].values:

            dfold['expired'][dfold['compositekey'] == key] = 1
            dfold['active'][dfold['compositekey'] == key] = 0

            dfold['expiredate'][dfold['compositekey'] == key] = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    return dfold

def check_for_active(dfnew, dfold):

    for key in dfnew['compositekey']:
        if key in dfold['compositekey'].values:

            dfold['active'][dfold['compositekey'] == key] = 1

    return dfold

def check_existing_new_status(dfold,dfnew):

    dfold['new'][dfold['createdate'] != datetime.datetime.today().strftime('%Y-%m-%d')] = 0

    return dfold

def compare_dataframe_pair(dfweb,dfcompared):

    df_newchecked = check_for_new(dfweb,dfcompared)

    df_expiredchecked = check_for_expired(dfweb,df_newchecked)

    df_activechecked = check_for_active(dfweb, df_expiredchecked)

    df_statusupdated = check_existing_new_status(df_activechecked,dfweb)
#     df_statusupdated = df_statusupdated[['compositekey', 'Bedrijfskey', 'createdate','Updatetime', 'Vacaturetitel', 'Link', 'active', 'new',
#        'expired', 'expiredate', 'Jobdescriptionfull']]
    return df_statusupdated

def get_comparedict(webmap = None,
                 comparemap = None):

    weblijst = []
    [weblijst.append(x) for x in os.listdir(webmap) if x.endswith('.csv')]

    comparelijst = []
    [comparelijst.append(x) for x in os.listdir(comparemap) if x.endswith('.csv')]

    comparedict = {}
    for frame_to_compare in comparelijst:
        if frame_to_compare.replace("_compared.csv", "") in list(map(lambda x: x.replace("_web.csv", ""), weblijst)):

            weblist_filename = frame_to_compare.replace("_compared.csv", "_web.csv")

            index_of_file_in_weblist = weblijst.index(weblist_filename)

            webframe_location = (os.path.join(webmap,(weblijst[index_of_file_in_weblist])))
            compareframe_location = os.path.join(comparemap, frame_to_compare)

            comparedict.update({webframe_location:compareframe_location})

    return comparedict

def compare_maps(webmap = None,
                     comparemap = None):

    for webframe_location,frame_to_compare_location in get_comparedict(webmap=webmap,comparemap=comparemap).items():

        df_web = pd.read_csv(webframe_location)
        df_to_compare = pd.read_csv(frame_to_compare_location)

        compared_dataframe = compare_dataframe_pair(dfweb = df_web, dfcompared=df_to_compare)

        compared_dataframe.to_csv(frame_to_compare_location, index = False)
        print('SUCCES: compared ' + str(webframe_location) + ' and ' + str(frame_to_compare_location))

compare_maps(webmap=webmap,comparemap=comparemap)
