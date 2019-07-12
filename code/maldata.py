import pandas as pd
mal_url_data = pd.read_csv("/home/user/datasets/phishtankurl.csv")
#mal_url_data.set_index('phish_id')
print(mal_url_data.head())
mal_url_data['status']='None'
print(mal_url_data.head())
mal_url_data.reset_index()

#benign_url_data['URL'] = 'http://' + benign_url_data['domain'].astype(str)
#benign_url_data.head()
mal_url_data = mal_url_data.iloc[1942:]
print(mal_url_data.head())

from pywebcopy import save_webpage
for index, row in mal_url_data.iterrows():
   # phish_id = row['phish_id']
    print(index)
    try:
        print("processing row", index)
       	#print(row['url'], row['phish_id'])
        url=row['url']
        print(url)
        download_folder = '/home/user/datasets/processed/'
        kwargs = {'bypass_robots': False, 'project_name': 'mal-data', 'LOAD_CSS': False, 'LOAD_IMAGES': False,'OVER_WRITE': False, 'ALLOWED_FILE_EXT': ['.html','.js']}
        save_webpage(url, download_folder, **kwargs)
        mal_url_data.at[index, 'status']='success'
        if(index%50==0):
         mal_url_data.to_csv('/home/user/mal_data_processing.csv',encoding='utf-8',index=False)
    except Exception as error:
        print(error)
        mal_url_data.at[index, 'status']='fail'
    print(mal_url_data.loc[index-2:index+2])


print("Data Capturing Done");

