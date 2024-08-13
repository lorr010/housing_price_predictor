import pandas as pd
class Read():
        
    def read_from_file(file_name: str) -> list:
        """
        # read data from csv file and create a list of objects
        # return list
        """

        try:
            df = pd.read_excel(file_name)
            print(f"The file {file_name} was found.")
        except FileNotFoundError:
            print(f"The file {file_name} was not found.")
            df = pd.DataFrame()  

        data_list = df.to_dict(orient='list')
        print(data_list)

        return data_list

file_name = "housing_price_predictor\dataset\data.xlsx"

Read.read_from_file(file_name)

