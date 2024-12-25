import random
import datetime


class HarnessInfo:

    def __init__(self):

        # SAC HARNAIS
        self._serial_number = random.randint(0, 100)
        self._name = self.random_name()

        self._manufacturer  = self.random_manufacturer()
        self._dom = self.random_harness_date()

    def random_name(self):

        container_list = ["Vector", "Advance", "Micro Sigma", "Atom", "Curv", "Icon", "Javelin"]
        suppl_list = ["02", "Bleu", "Nico", "Rouge", "Ecole", "Vert", "Benji", "12", "21"]

        container_index = random.randint(0, len(container_list) - 1)
        suppl_index = random.randint(0, len(suppl_list) - 1)

        return container_list[container_index] + " " + suppl_list[suppl_index]

    def random_manufacturer(self):

        self.manufacturer_list = ["UPT", "Sun Path", "Parachutes de France", "Basik Air Concept", "Rigging Innovations"]
        self._manufacturer_index = random.randint(0, len(self.manufacturer_list) - 1)

        return self.manufacturer_list[self._manufacturer_index]

    def random_harness_date(self):
        start_date = datetime.date(2000, 1, 1)
        end_date = datetime.date.today()

        my_date = start_date + (end_date - start_date) * random.random()
        my_date = my_date.strftime("%m/%d/%Y")

        return my_date
