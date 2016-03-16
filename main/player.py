class Player:
    def __init__(self):
        # resource_sec = resources / second, resource_click = resources / click
        self.__resource_amt, self.__resource_sec, self.__resources_click = 0, 0, 1

    def modify_resources(self, amt):
        self.__resource_amt += amt

    def get_total_resources(self):
        return self.__resource_amt

    def modify_resource_sec(self, amt):
        self.__resource_sec += amt

    def get_resource_sec(self):
        return self.__resource_sec

    def modify_resources_click(self, amt):
        self.__resources_click += amt

    def get_resources_click(self):
        return self.__resources_click
