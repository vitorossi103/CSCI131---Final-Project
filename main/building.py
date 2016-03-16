class Building:
    def __init__(self, modifier, cost):
        """
        :param modifier: how much affects player's resource gathering
        :return:

         Building objects will affect Player's resource / sec
        """
        self.__modifier = modifier
        self.__cost = cost
        self.__amount = 0

    def get_modifier(self):
        return self.__modifier

    def get_cost(self):
        return self.__cost

    def get_amount(self):
        return self.__amount

    def modify_amount(self, amt):
        self.__amount += amt
