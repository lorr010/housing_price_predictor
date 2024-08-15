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

    def update_house_by_id(self, id, **kwargs):
            house = self.houses.get(id)
            if house:
                for key, value in kwargs.items():
                    if hasattr(house, key):
                        setattr(house, key, value)
                return house
            return None
    
    def get_houses_by_filters(self, filters: dict) -> list:
        
        matching_houses = []
        for house in self.houses.values():
        # Assume all filters match initially
            match = True
            for key, value in filters.items():
                # Check if the house has the attribute and if it matches the filter
                if hasattr(house, key):
                    if getattr(house, key) != value:
                        match = False
                        break
                else:
                    match = False
                    break
            # If all filters match, add the house to the result list
            if match:
                matching_houses.append(house)
    
        return matching_houses
        
        # for house in self.houses.values():
        #     for key, value in filters.items():
        #         if hasattr(house, key):
        #             if house:
        #                 matching_houses.append(house)
            
        # return matching_houses

    def create_house(self, house: House):
        self.houses[house.id] = house

    def read_house(self, id):
        return self.houses.get(id, None)

    

    def delete_house_by_id(self, id):
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