import pandas as pd

def read_from_file(file_name: str) -> list:
    """
    # read data from csv file and create a list of objects
    # return list
    """
    
    try:
        df = pd.read_excel(file_name)
        print(f"The file was found.")
    except FileNotFoundError:
        print(f"The file was not found.")
        df = pd.DataFrame()  

    data_list = df.to_dict(orient='records')
    return data_list


