class Building:
    def __init__(self, modifier):
        """
        :param modifier: how much affects player's resource gathering
        :return:

         Building objects will affect Player's resource / sec
        """
        self.modifier = modifier
