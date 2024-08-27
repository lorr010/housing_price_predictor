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
        s = f"House(id={self.id}, neighborhood={self.neighborhood}, year_built={self.year_built})"
        print(s)
        return s



s = "success"
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
    

    def create_house(self, house: House):
        self.houses[house.id] = house
        return house.id

    def read_house_id(self, house, id):
        return self.houses.get(house.id, id)

    def delete_house_by_id(self, id):
        if id in self.houses:
            del self.houses[id]
            return id

    def toString(self):
        for id, house in self.houses.items():
            house.toString()
        

