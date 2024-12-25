import random
import datetime


class ReserveCanopyInfo:

    def __init__(self):

        # VOILE DE SECOURS
        self._serial_number = random.randint(0, 1000)
        self._name = self.random_name()

        self._manufacturer  = self.random_manufacturer()
        self._dom = self.random_reserve_date()

        self._size = self.random_size()

    def random_name(self):

        reserve_list = ["VR-360", "Optimum", "PD-R", "Techno", "Secours", "Smart"]
        suppl_list = ["Sigma", "Rouge/Bleu", "Nico", "Vector", "Blanche"]

        reserve_index = random.randint(0, len(reserve_list) - 1)
        suppl_index = random.randint(0, len(suppl_list) - 1)

        return reserve_list[reserve_index] + " " + suppl_list[suppl_index]

    def random_manufacturer(self):

        manufacturer_list = ["Icarus World", "Jyro", "Parachutes de France", "Basik Air Concept", "Performances Designs"]
        manufacturer_index = random.randint(0, len(manufacturer_list) - 1)

        return manufacturer_list[manufacturer_index]

    def random_reserve_date(self):
        start_date = datetime.date(2000, 1, 1)
        end_date = datetime.date.today()

        my_date = start_date + (end_date - start_date) * random.random()
        my_date = my_date.strftime("%m/%d/%Y")

        return my_date

    def random_size(self):

        size_list = ["98", "115", "126", "140", "193", "240", "360"]
        size_index = random.randint(0, len(size_list) - 1)

        return size_list[size_index]