import pandas as pd
benign_url_data = pd.read_csv("/home/user/datasets/alexa_top1m/top-1m.csv", header=None, names=["SrNo","domain"])
print(benign_url_data.head())

benign_url_data['URL'] = 'http://' + benign_url_data['domain'].astype(str)
benign_url_data['status']='None'

print(benign_url_data.head())
benign_url_data = benign_url_data.iloc[761:]
print(benign_url_data.head())

print("start")
from pywebcopy import save_webpage
i=300
for index, row in benign_url_data.iterrows():
    print(index)
    try:
        print(row['URL'], row['domain'])
        print("processing ", index)
        url = row['URL']
        download_folder = '/home/user/datasets/processed/'
        kwargs = {'bypass_robots': True, 'project_name': 'benign-data', 'LOAD_CSS': False, 'LOAD_IMAGES': False,'OVER_WRITE': False, 'ALLOWED_FILE_EXT': ['.html','.js']}
        save_webpage(url, download_folder, **kwargs)
        benign_url_data.at[index, 'status']='success'
        if(index%50==0):
          benign_url_data.to_csv('/home/user/benign_data_processing.csv',encoding='utf-8',index=False)    
    except Exception as error:
        print(error)
        benign_url_data.at[index, 'status']='fail'
    print(benign_url_data.loc[index-2:index+2])

print("data capturing end")
