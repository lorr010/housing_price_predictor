class House():
    # initialize house object which should all these properties:

    def __init__():
        pass

    
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