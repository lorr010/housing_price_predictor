class House():
    # initialize house object which should all these properties:

   
    def __init__(self, id, neighborhood, house_style, overall_condition, year_built,
                 roof_type, roof_material, foundation_material, heating, central_air,
                 electrical, fireplace_num, garage_area, date_sold):
        self.id = id
        self.neighborhood = neighborhood
        self.house_style = house_style
        self.overall_condition = overall_condition
        self.year_built = year_built
        self.roof_type = roof_type
        self.roof_material = roof_material
        self.foundation_material = foundation_material
        self.heating = heating
        self.central_air = central_air
        self.electrical = electrical
        self.fireplace_num = fireplace_num
        self.garage_area = garage_area
        self.date_sold = date_sold

    def toString(self):
        print(f"House(id={self.id}, neighborhood={self.neighborhood}, "
                f"year_built={self.year_built})")


class CRUD():
    def __init__(self):
        self.houses = {}
        # houses from the dataset that contain the key value pairs: id and house object

    def get_houses_by_year_and_neighborhood(self, year_built, neighborhood):
        
        matching_houses = []

        for house in self.houses.values():
            if house.year_built == year_built and house.neighborhood == neighborhood:
                matching_houses.append(house)
        
        return matching_houses

    def create_house(self, house: House):
        self.houses[house.id] = house

    def read_house(self, id):
        return self.houses.get(id, None)

    def update_house(self, id, **kwargs):
        house = self.houses.get(id)
        if house:
            for key, value in kwargs.items():
                if hasattr(house, key):
                    setattr(house, key, value)
            return house
        return None

    def delete_house(self, id):
        if id in self.houses:
            del self.houses[id]

    def toString(self):
        for id, house in self.houses.items():
            house.toString()
        













"""
# TASK 4
    def update_house(self, updated_data):
        # update the house by id
        # example: id =1 and updated_data = {"neighborhood": "gilbert"}
        # this should update the neighborhood of the house with id 1 to gilbert
        pass

    #house = House()#..attributes
    #house.update_house({"neighborhood": "Gilbert"})

    @classmethod
    def update_house_by_id(cls, id, house_data, updated_data):
        pass
    #House.update_house_by_id( 1, house_data, {"neighborhood": "Gilbert"})

    def delete_house(self):
        # delete house by id
        pass

    @classmethod
    def get_house_by_filter(self, house_data, filters):
        # example: filters = {"id": 1, "neighborhood": "gilbert"}
        # this should return the house with id 1 in the neighborhood gilbert
        pass
"""