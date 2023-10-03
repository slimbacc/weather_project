import ast
import tempfile
from datetime import datetime

import pandas as pd
import pyrebase
from swagger_client.rest import ApiException

from ..config.config import app_config
from weather_pipeline.process.functions import flatten_dict

api_instance, q, firebaseConfig= (
    app_config.api_instance,
    app_config.q,
    app_config.firebaseConfig
)

def get_data(api_instance, q) -> pd.DataFrame:
    try:
        # Realtime API
        api_response = api_instance.realtime_weather(q, lang="en")
        print("Data acquired successfully")

    except ApiException as e:

        print("Exception when calling APIsApi->realtime_weather: %s\n" % e)
        return None
    
    data_dict = ast.literal_eval(str(api_response))
    # Flatten the nested dictionary
    flat_data = flatten_dict(data_dict)
    df = pd.DataFrame([flat_data])
    return df

def upload_to_firebase(firebaseConfig: dict, df: pd.DataFrame, cloud_path: str) -> None:
    firebase = pyrebase.initialize_app(firebaseConfig)

    storage = firebase.storage()

    # Create a temporary directory to store the CSV file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Construct the local file path for the CSV file
        local_path = f"{temp_dir}/temp.csv"
        # Save the DataFrame as a CSV file in the temporary directory
        df.to_csv(local_path, index=False)
        # Upload the CSV file to Firebase Storage
        storage.child(cloud_path).put(local_path)

    
def main():
    df_csv = get_data(api_instance, q)
    # Get the current date and time in the "hh:mm" format
    current_time = datetime.now().strftime("%d-%m-%Y/%H:%M")
    cloud_path = f'raw_data/{current_time}.csv'
    upload_to_firebase(firebaseConfig, df_csv, cloud_path)

if __name__ == "__main__":
    main()
