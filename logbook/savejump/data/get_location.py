import psycopg2

class GetLocationData:

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

    def get_location(self):

        req_sql = """ SELECT location.id_location FROM location;"""

        connection = None
        try:
            # obtention de la connexion à la base de données

            connection = psycopg2.connect(host=self._host, database=self._database, user=self._user,
                                          password=self._password, port=self._port)
            # create a new cursor
            cursor = connection.cursor()

            # ENREGISTREMENT DU SAUT
            cursor.execute(req_sql)

            locations = cursor.fetchall()

            # commit the changes to the database
            connection.commit()
            # close communication with the database
            cursor.close()

            return locations

        except (Exception, psycopg2.DatabaseError) as error:
            print("Erreur add_location:")
            print(error)
        finally:
            if connection is not None:
                connection.close()