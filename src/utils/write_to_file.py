import pandas as pd

def write_to_file(file_name: str, content: list) -> str:
    """
    # write the content to the file
    # return nothing
    """

    df = pd.DataFrame(content)
    try:
        df.to_excel(file_name, index=False)
        success = "Write to file success"
        
    except Exception as e:
        print(f"Write to file failure")
        return str(e)

    
    return success

#file_name = "housing_price_predictor\dataset\data.xlsx"
#content = {"neighborhood":"Gilbert"}

#write_to_file(file_name, content)