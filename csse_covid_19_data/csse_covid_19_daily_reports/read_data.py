from glob import glob
import pandas as pd

def clean_data():
    """ Reads the dataframes and returns a clean df """
    
    filenames = glob('*.csv')
    dataframes = [pd.read_csv(f) for f in filenames]

    # need to unified the columns names
    for i in range(0,len(dataframes)):
        dataframes[i].columns = [label.replace(' ','_') for label in dataframes[i].columns]
        dataframes[i].columns = [label.replace('/','_') for label in dataframes[i].columns]
        dataframes[i] = dataframes[i][['Province_State', 'Country_Region', 'Last_Update', "Confirmed", 'Deaths', 'Recovered']]

    df = pd.concat(dataframes, ignore_index=True)
    df['Last_Update'] = pd.to_datetime(df['Last_Update'])
    df['Date'] = df['Last_Update'].dt.date
    df.drop('Last_Update',axis=1, inplace =True)
    return df

df = clean_data()
