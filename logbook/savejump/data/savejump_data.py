import psycopg2

class SaveJumpData:

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

    def add_jump(self, number, date, location, parachute):

        jump_infos = (number, date, location, parachute)

        insert_jump = """ INSERT INTO jump (jump_number, jump_date, id_location, id_parachute) 
                                                VALUES(%s,%s,%s,%s);"""

        connection = None
        try:
            # obtention de la connexion à la base de données

            connection = psycopg2.connect(host=self._host, database=self._database, user=self._user,
                                          password=self._password, port=self._port)
            # create a new cursor
            cursor = connection.cursor()

            # ENREGISTREMENT DU SAUT
            cursor.execute(insert_jump, jump_infos)

            # commit the changes to the database
            connection.commit()
            # close communication with the database
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Erreur add_jump:")
            print(error)
        finally:
            if connection is not None:
                connection.close()

    def get_location_id(self, location):

        req_sql = """SELECT location.id_location FROM location WHERE location_name = %s"""

        connection = None
        try:
            # obtention de la connexion à la base de données

            connection = psycopg2.connect(host=self._host, database=self._database, user=self._user,
                                          password=self._password, port=self._port)
            # create a new cursor
            cursor = connection.cursor()

            # ENREGISTREMENT DU SAUT
            cursor.execute(req_sql,(location,))

            id_location = cursor.fetchone()

            # commit the changes to the database
            connection.commit()
            # close communication with the database
            cursor.close()

            return id_location

        except (Exception, psycopg2.DatabaseError) as error:
            print("Erreur get_location_id:")
            print(error)
        finally:
            if connection is not None:
                connection.close()

    def get_parachute_id(self, harness_name):

        req_sql = """SELECT parachute.id_parachute FROM parachute WHERE harness_name = %s"""

        connection = None
        try:
            # obtention de la connexion à la base de données

            connection = psycopg2.connect(host=self._host, database=self._database, user=self._user,
                                          password=self._password, port=self._port)
            # create a new cursor
            cursor = connection.cursor()

            # ENREGISTREMENT DU SAUT
            cursor.execute(req_sql,(harness_name,))

            id_parachute = cursor.fetchone()

            # commit the changes to the database
            connection.commit()
            # close communication with the database
            cursor.close()

            return id_parachute

        except (Exception, psycopg2.DatabaseError) as error:
            print("Erreur get_parachute_id:")
            print(error)
        finally:
            if connection is not None:
                connection.close()