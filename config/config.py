"""imports"""
from dataclasses import dataclass

import swagger_client

configuration = swagger_client.Configuration()
configuration.api_key['key'] = '47561d97834143c6b9483402232109'

@dataclass
class Config:
    """contains paths of input and output dfs"""
    q: str
    local_path: str
    api_instance: object
    firebaseConfig: dict
    cloud_path: str

app_config = Config(
    q = '196.179.217.130',
    api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration)),
    local_path="local_path",
    cloud_path="cloud_path",
    firebaseConfig = {
        "apiKey": "AIzaSyCC8YCSL2cKJW_6zd9nC5wni_f3zSc8mzE",
        "authDomain": "crested-archive-397616.firebaseapp.com",
        "projectId": "crested-archive-397616",
        "storageBucket": "crested-archive-397616.appspot.com",
        "messagingSenderId": "180332915614",
        "appId": "1:180332915614:web:f653dbd193d129c5f7448f",
        "measurementId": "G-0WV80JD40C",
        "databaseURL": "https://console.firebase.google.com/u/0/project/crested-archive-397616/storage/crested-archive-397616.appspot.com/files"
    }
)