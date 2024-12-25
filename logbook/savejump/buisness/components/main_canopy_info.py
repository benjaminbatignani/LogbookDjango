import random
import datetime


class MainCanopyInfo:

    def __init__(self):

        # VOILE PRINCIPALE
        self._serial_number = random.randint(0, 1000)
        self._name = self.random_name()

        self._manufacturer  = self.random_manufacturer()
        self._dom = self.random_main_date()

        self._size = self.random_size()

    def random_name(self):

        container_list = ["Icarus", "TX-2", "Leia", "Navigator", "Sabre3", "Crossfire2", "JVX"]
        suppl_list = ["Jaune", "Rouge/Bleu", "Nico", "Rouge", "Orange", "Vert", "Multicolore", "Noire", "Blanche"]

        container_index = random.randint(0, len(container_list) - 1)
        suppl_index = random.randint(0, len(suppl_list) - 1)

        return container_list[container_index] + " " + suppl_list[suppl_index]

    def random_manufacturer(self):

        manufacturer_list = ["Icarus World", "Jyro", "Parachutes de France", "Basik Air Concept", "Performances Designs"]
        manufacturer_index = random.randint(0, len(manufacturer_list) - 1)

        return manufacturer_list[manufacturer_index]

    def random_main_date(self):
        start_date = datetime.date(2000, 1, 1)
        end_date = datetime.date.today()

        my_date = start_date + (end_date - start_date) * random.random()
        my_date = my_date.strftime("%m/%d/%Y")

        return my_date

    def random_size(self):

        size_list = ["72", "99", "120", "240", "280", "330", "364", "400"]
        size_index = random.randint(0, len(size_list) - 1)

        return size_list[size_index]