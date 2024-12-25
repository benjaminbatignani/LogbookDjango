from logbook.savejump.presentation import affichage_menu
from logbook.savejump.data import savejump_data, insert_data, insert_parachute
from logbook.savejump.buisness.components.jump_infos import JumpInfos
from logbook.savejump.buisness.components import harness_info, main_canopy_info, reserve_canopy_info, aad_info
import random

if __name__ == '__main__':

    menu = affichage_menu.Affichage_menu()
    choix = menu.afficher_menu_principal()

    while choix != "q":

        if choix == "1":

            for i in range(10):
                jump_infos = JumpInfos()

                jump_number = jump_infos._jump_number
                date = jump_infos._jump_date
                location = jump_infos._jump_location

                data = savejump_data.SaveJumpData()
                data.add_jump(jump_number, date, location)

            choix = menu.afficher_menu_principal()

        elif choix == "2":

            data_infos = ('Tandem', 'Tandem Vidéo', 'Tandem Vidéo Photo', 'Vidéo Tandem', 'PAC', 'Reprise PAC',
                          '1er Niveau PAC', 'Init VR', 'Init Freefly', 'Suivi B', 'Loisir', 'Freefly', 'VR',
                          'Wingsuit')

            data = insert_data.InsertLocationData()

            for item in data_infos:
                data.add_data(item)

            choix = menu.afficher_menu_principal()

        # ENREGISTREMENT D UN PARACHUTE EN BD
        elif choix == "3":

            for i in range(100):

                harness = harness_info.HarnessInfo()
                main_canopy = main_canopy_info.MainCanopyInfo()
                reserve_canopy = reserve_canopy_info.ReserveCanopyInfo()
                aad = aad_info.AadInfo()


                data = insert_parachute.InsertParachuteData()
                data.add_parachute(harness._dom, harness._manufacturer, harness._name, harness._serial_number,
                                   main_canopy._dom, main_canopy._manufacturer, main_canopy._name, main_canopy._serial_number,
                                   main_canopy._size,
                                   reserve_canopy._dom, reserve_canopy._manufacturer, reserve_canopy._name,
                                   reserve_canopy._serial_number, reserve_canopy._size,
                                   aad._dom, aad._manufacturer, aad._serial_number)

            choix = menu.afficher_menu_principal()

