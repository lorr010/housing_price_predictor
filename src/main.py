from utils.write_to_file import write_to_file
from classes.House import House
from classes.House import CRUD
from utils.read_from_file import read_from_file

def main():
    # create a dictionary with key being the id and value being the house object
    house_dict = CRUD()

    # read the data from excel and create house object, 
    # iterate through the file and add to dictionary
    file_name = "housing_price_predictor\dataset\data.xlsx"
    house_data = read_from_file(file_name)
    print(f'working?')
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
        print(house.toString())
        house_dict.create_house(house)
    
    house_dict.toString()

        

    # call the methods on the house object
    #1. get the houses built in 2006 in the neighborhood Gilbert
    
    
    houses_to_update = house_dict.get_houses_by_year_and_neighborhood(2006, "Gilbert")

    print("working?")
    for house in houses_to_update:
        house.toString()

    
    #2. update those houses to have anew neighborhood as "Disneyland"
    
    for house in houses_to_update:
         house_dict.update_house(house.id, neighborhood="Disneyland")

    #3. delete those houses

    for house in houses_to_update:
         house_dict.delete_house(house.id)

    # write the updated data to the csv file

    updated_data = [vars(house) for house in house_dict.houses.values()]
   # write_to_file(file_name, updated_data)


if __name__ == "__main__":
    main()
    
