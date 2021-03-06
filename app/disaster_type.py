from urllib.request import urlopen
import json
import pandas as pd
import selenium
pd.set_option('display.max_columns', None)

def get_fema_json(state):
    try:
        url = "https://www.fema.gov/api/open/v1/DisasterDeclarationsSummaries?$orderby=declarationDate%20desc,%20declaredCountyArea&$format=json"
        response = urlopen(url)
        json_data = response.read().decode('utf-8', 'replace')
        d = json.loads(json_data)
        df = pd.DataFrame(d['DisasterDeclarationsSummaries'])
        df = df.drop_duplicates()
        df = df.drop(columns=['id', 'lastRefresh', 'hash', 'fyDeclared', 'disasterCloseOutDate', 'placeCode'])
        df = df[df['incidentEndDate'].isin([None])]
        df = df[df['state'].isin([state])]
        df = df.to_json(orient='records')
        return df
    except Exception as e:
        return e
    
def get_fema_dataframe(state):
    try:
        url = "https://www.fema.gov/api/open/v1/DisasterDeclarationsSummaries?$orderby=declarationDate%20desc,%20declaredCountyArea&$format=json"
        response = urlopen(url)
        json_data = response.read().decode('utf-8', 'replace')
        d = json.loads(json_data)
        df = pd.DataFrame(d['DisasterDeclarationsSummaries'])
        df = df.drop_duplicates()
        df = df.drop(columns=['id', 'lastRefresh', 'hash', 'fyDeclared', 'disasterCloseOutDate', 'placeCode'])
        df = df[df['incidentEndDate'].isin([None])]
        df = df[df['state'].isin([state])]
        return df
    except Exception as e:
        return e