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

    def add_jump(self, number, altitude, aircraft, location, jump_type, parachute, jump_date, comment):

        jump_infos = (number, altitude, aircraft, location,jump_type, parachute, jump_date, comment)

        insert_jump = """ INSERT INTO jump (jump_number, id_altitude, id_aircraft, id_location,id_jump_type, 
                                            id_parachute, jump_date, comment) 
                                                VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"""

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

        req_sql = """SELECT id_location FROM location WHERE location_name = %s"""

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

    def get_aircraft_id(self, aircraft):

        req_sql = """SELECT id_aircraft FROM aircraft WHERE aircraft = %s"""

        connection = None
        try:
            # obtention de la connexion à la base de données

            connection = psycopg2.connect(host=self._host, database=self._database, user=self._user,
                                          password=self._password, port=self._port)
            # create a new cursor
            cursor = connection.cursor()

            # ENREGISTREMENT DU SAUT
            cursor.execute(req_sql,(aircraft,))

            id_aircraft = cursor.fetchone()

            # commit the changes to the database
            connection.commit()
            # close communication with the database
            cursor.close()

            return id_aircraft

        except (Exception, psycopg2.DatabaseError) as error:
            print("Erreur get_aircraft_id:")
            print(error)
        finally:
            if connection is not None:
                connection.close()
    def get_altitude_id(self, altitude):

        req_sql = """SELECT id_altitude FROM altitude WHERE altitude = %s"""

        connection = None
        try:
            # obtention de la connexion à la base de données

            connection = psycopg2.connect(host=self._host, database=self._database, user=self._user,
                                          password=self._password, port=self._port)
            # create a new cursor
            cursor = connection.cursor()

            # ENREGISTREMENT DU SAUT
            cursor.execute(req_sql,(altitude,))

            id_altitude = cursor.fetchone()

            # commit the changes to the database
            connection.commit()
            # close communication with the database
            cursor.close()

            return id_altitude

        except (Exception, psycopg2.DatabaseError) as error:
            print("Erreur get_altitude_id:")
            print(error)
        finally:
            if connection is not None:
                connection.close()

    def get_jump_type_id(self, jump_type):

        req_sql = """SELECT id_jump_type FROM jump_type WHERE type = %s"""

        connection = None
        try:
            # obtention de la connexion à la base de données

            connection = psycopg2.connect(host=self._host, database=self._database, user=self._user,
                                          password=self._password, port=self._port)
            # create a new cursor
            cursor = connection.cursor()

            # ENREGISTREMENT DU SAUT
            cursor.execute(req_sql,(jump_type,))

            id_jump_type = cursor.fetchone()

            # commit the changes to the database
            connection.commit()
            # close communication with the database
            cursor.close()

            return id_jump_type

        except (Exception, psycopg2.DatabaseError) as error:
            print("Erreur get_jump_type_id:")
            print(error)
        finally:
            if connection is not None:
                connection.close()

    def get_parachute_id(self, harness_name):

        req_sql = """SELECT id_parachute FROM parachute WHERE harness_name = %s"""

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

    def get_last_jump_number(self):

        req_sql = """SELECT jump.jump_number FROM jump ORDER BY jump_number DESC"""

        connection = None
        try:
            # obtention de la connexion à la base de données

            connection = psycopg2.connect(host=self._host, database=self._database, user=self._user,
                                          password=self._password, port=self._port)
            # create a new cursor
            cursor = connection.cursor()

            # ENREGISTREMENT DU SAUT
            cursor.execute(req_sql)

            last_jump_number = cursor.fetchone()[0]

            # commit the changes to the database
            connection.commit()
            # close communication with the database
            cursor.close()

            return last_jump_number

        except (Exception, psycopg2.DatabaseError) as error:
            print("Erreur get_last_jump_number:")
            print(error)
        finally:
            if connection is not None:
                connection.close()