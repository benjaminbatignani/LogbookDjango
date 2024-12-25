import psycopg2

class InsertLocationData:

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

    def add_data(self, data):

        insert_data = """ INSERT INTO jump_type (type) VALUES(%s);"""

        data_infos = (data, )

        connection = None
        try:
            # obtention de la connexion à la base de données

            connection = psycopg2.connect(host=self._host, database=self._database, user=self._user,
                                          password=self._password, port=self._port)
            # create a new cursor
            cursor = connection.cursor()

            # ENREGISTREMENT DU SAUT
            cursor.execute(insert_data, data_infos)

            # commit the changes to the database
            connection.commit()
            # close communication with the database
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Erreur add_location:")
            print(error)
        finally:
            if connection is not None:
                connection.close()