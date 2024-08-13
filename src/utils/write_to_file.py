import pandas as pd

class Write():

    def write_to_file(file_name: str, content: str) -> None:
        """
        # write the content to the file
        # return nothing
        """

        df = pd.DataFrame(content.items())
        try:
            #df.to_excel(file_name, index=False)
            print(f"all good")
        except Exception as e:
            print(f"an error has occured")


file_name = "housing_price_predictor\dataset\data.xlsx"
content = {"neighborhood":"Gilbert"}

Write.write_to_file(file_name, content)