from utils.write_to_file import write_to_file
from classes.House import House
from classes.House import CRUD
from utils.read_from_file import read_from_file

def main():
    # create a dictionary with key being the id and value being the house object
    print(f"CREATING HOUSE DICTIONARY (KEY: ID, VALUE: HOUSE)")
    house_dict = CRUD()

    # read the data from excel and create house object, 
    # iterate through the file and add to dictionary
    file_name = "housing_price_predictor\dataset\data.xlsx"
    house_data = read_from_file(file_name)
    print(f'READING DATA FROM FILE...')
    for attr in house_data:
        house = House(
            id = attr['Id'],
            neighborhood = attr['Neighborhood'],
            house_style = attr['HouseStyle'],
            overall_condition = attr['OverallCond'],
            year_built = attr['YearBuilt'],
            roof_type = attr['RoofStyle'],
            roof_material = attr['RoofMatl'],
            foundation_material = attr['Foundation'],
            heating = attr['Heating'],
            central_air = attr['CentralAir'],
            electrical = attr['Electrical'],
            fireplace_num = attr['Fireplaces'],
            garage_area = attr['GarageArea'],
            date_sold = f"{attr['MoSold']}/{attr['YrSold']}"
            
        )
        house_dict.create_house(house)
    
    #house_dict.toString()
    print(f"HOUSES CREATED AND ADDED TO DICTIONARY")
        

    # call the methods on the house object
    #1. get the houses built in 2006 in the neighborhood Gilbert
    houses_to_update = house_dict.get_houses_by_year_and_neighborhood(2006, "Gilbert")

    print(f"HOUSES THAT ARE IN GILBERT AND BUILT IN 2006:")
    for house in houses_to_update:
        house.toString()

    
    #2. update those houses to have a new neighborhood as "Disneyland"
    print(f"UPDATING NEIGHBORHOOD GILBERT TO DISNEYLAND")
    for house in houses_to_update:
        house_dict.update_house(house.id, neighborhood="Disneyland")
        house.toString()
    print(f"NEIGHBORHOOD UPDATED")

    #3. delete those houses
    for house in houses_to_update:
        print(f"DELETING HOUSE {house.id} FROM LIST")
        house_dict.delete_house(house.id)
    print(f"ALL DISNEYLAND HOUSES DELETED FROM DICTIONARY")
    #house_dict.toString()
    print(f"UPDATED DICTIONARY")

    # write the updated data to the excel file
    new_file = "housing_price_predictor\\dataset\\update.xlsx"
    updated_data = [vars(house) for house in house_dict.houses.values()]
    print(f"WRITING UPDATED DICTIONARY TO A NEW EXCEL FILE")
    write_to_file(new_file, updated_data)



if __name__ == "__main__":
    main()
    
