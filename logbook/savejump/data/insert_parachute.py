import psycopg2

class InsertParachuteData:

    # ------------------------------
    # constructeur
    # ------------------------------
    def __init__(self):

        # constantes pour les connexions à la base de données
        self._host = "localhost"
        self._database = "django_logbook_db"
        self._user = "benjaminbatignani"
        self._password = "dev"
        self._port = 5432

    def add_parachute(self, harness_manufacturer, harness_name, harness_serial_number, harness_dom,
                      main_canopy_dom, main_canopy_manufacturer, main_canopy_name, main_canopy_serial_number, main_canopy_size,
                      reserve_canopy_dom, reserve_canopy_manufacturer, reserve_canopy_name,
                      reserve_canopy_serial_number, reserve_canopy_size,
                      aad_dom, aad_manufacturer, aad_serial_number):

        parachute_infos = (harness_manufacturer, harness_name, harness_serial_number, harness_dom,
                           main_canopy_dom, main_canopy_manufacturer, main_canopy_name, main_canopy_serial_number,
                           main_canopy_size,
                           reserve_canopy_dom, reserve_canopy_manufacturer, reserve_canopy_name,
                           reserve_canopy_serial_number, reserve_canopy_size,
                           aad_dom, aad_manufacturer, aad_serial_number
                           )

        insert_parachute = """ INSERT INTO parachute (harness_dom, harness_manufacturer, harness_name, harness_serial_number,
                                        main_canopy_dom, main_canopy_manufacturer, main_canopy_name, main_canopy_serial_number,
                                        main_canopy_size,
                                        reserve_canopy_dom, reserve_canopy_manufacturer, reserve_canopy_name,
                                        reserve_canopy_serial_number, reserve_canopy_size,
                                        aad_dom, aad_manufacturer, aad_serial_number) 
                                                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""

        connection = None
        try:
            # obtention de la connexion à la base de données

            connection = psycopg2.connect(host=self._host, database=self._database, user=self._user,
                                          password=self._password, port=self._port)
            # create a new cursor
            cursor = connection.cursor()

            # ENREGISTREMENT DU SAUT
            cursor.execute(insert_parachute, parachute_infos)

            # commit the changes to the database
            connection.commit()
            # close communication with the database
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Erreur add_parachute:")
            print(error)
        finally:
            if connection is not None:
                connection.close()