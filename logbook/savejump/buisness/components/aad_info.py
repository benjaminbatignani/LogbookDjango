import random
import datetime


class AadInfo:

    def __init__(self):

        # SYSTEME DE SECURITE
        self._serial_number = random.randint(0, 1000)
        self._name = self.random_name()

        self._manufacturer  = self.random_manufacturer()
        self._dom = self.random_aad_date()


    def random_name(self):

        reserve_list = ["VR-360", "Optimum", "PD-R", "Techno", "Secours", "Smart"]
        suppl_list = ["Sigma", "Rouge/Bleu", "Nico", "Vector", "Blanche"]

        reserve_index = random.randint(0, len(reserve_list) - 1)
        suppl_index = random.randint(0, len(suppl_list) - 1)

        return reserve_list[reserve_index] + " " + suppl_list[suppl_index]

    def random_manufacturer(self):

        aad_list = ["Airtec", "AAD"]
        aad_index = random.randint(0, len(aad_list) - 1)

        return aad_list[aad_index]

    def random_aad_date(self):
        start_date = datetime.date(2000, 1, 1)
        end_date = datetime.date.today()

        my_date = start_date + (end_date - start_date) * random.random()
        my_date = my_date.strftime("%m/%d/%Y")

        return my_date

