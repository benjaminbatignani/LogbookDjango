import random, datetime
from logbook.savejump.data import get_location

class JumpInfos:

    def __init__(self):

        self._jump_number = random.randint(0, 1000)
        self._jump_date = self.random_date()
        self._jump_location = self.random_location()
        self._jump_parachute = self.random_parachute()

    def random_date(self):

        start_date = datetime.date(2024, 1, 1)
        end_date = datetime.date.today()

        my_date = start_date + (end_date - start_date) * random.random()
        return my_date

    def random_parachute(self):

        parachute_list = ["Micro Sigma 1", "Vector", "Atom Bleu", "Advance E03", "Antigua", "Saint Martin"]
        parachute_index = random.randint(0, len(parachute_list) - 1)

        return parachute_list[parachute_index]

    def random_location(self):

        locations = get_location.GetLocationData().get_location()

        location_index = random.randint(0, len(locations) - 1)

        return locations[location_index]