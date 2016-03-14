class Player:
    def __init__(self, resource_amt, resource_sec):
        """
        :param resource_amt: total resources
        :param resource_sec: resources per second
        :return: None
        """

        self.__resource_amt = resource_amt
        self.__resource_sec = resource_sec
        self.__building_list = [[]]  # will be a list of lists
