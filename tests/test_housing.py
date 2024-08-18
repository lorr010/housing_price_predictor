import pytest
from src.utils.write_to_file import write_to_file
from src.classes.House import House
from src.classes.House import CRUD
from src.utils.read_from_file import read_from_file
 
file_read =  "C:\\Users\\leban\\OneDrive\\Desktop\\Git-Folder\\housing_price_predictor\\housing_price_predictor\\dataset\\data.xlsx"
file_write = "C:\\Users\\leban\\OneDrive\\Desktop\\Git-Folder\\housing_price_predictor\\housing_price_predictor\\dataset\\update.xlsx"

house = House(id = "1", neighborhood = "Gilbert", house_style = "Condo", overall_condition = "Good", year_built = "2017",
                 roof_type = "Solar panels", roof_material = "Titanium", foundation_material = "titanium", heating = "Chill", central_air = "True",
                 electrical = "very", fireplace_num = "20", garage_area = "125 sqft", date_sold = "2078")
crud = CRUD()
id = house.id

def test_read_from_file():

    r = read_from_file(file_read)
    for d in r:
        assert type(d) is dict


def test_write_to_file():
    
    content = ["Are", "You", "Working", "?"]
    w = write_to_file(file_write, content)
    assert w == "Write to file success"

def test_House_string():
    string = house.toString()
    assert "Gilbert" in string

def test_CRUD_create():
    create = crud.create_house(house)
    assert create == id


def test_CRUD_delete():
    delete = crud.delete_house_by_id(house.id)
    assert delete == id

def test_CRUD_read():
    read = crud.read_house_id(house, id)
    assert read == id

def test_CRUD_update():
    update = crud.update_house_by_id(house.id, new_heating = "Hot")


def test_CRUD_filters():
    filters = {
        "fireplace_num": 20, 
        "year_built": 2017
        }
    filter_house = crud.get_houses_by_filters(filters)
    for h in filter_house:
         a = print(h.toString())
    
         


    