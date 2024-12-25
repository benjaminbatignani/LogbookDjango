import os


if __name__ == '__main__':


    HOST = "localhost"
    DATABASE = "save_jump_db"
    USER = "benjaminbatignani"
    PASSWORD = "dev"
    PORT = 5432
    SCRIPTS_DIRECTORY = "/Users/benjaminbatignani/Documents/Code/LogbookDjango/"
    POSTGRESQL_BIN = "/Library/PostgreSQL/13/bin/psql"

    fichier_script = "creation_tables.sql"

    print("Execution de: {0}".format(fichier_script))

    command = "PGPASSWORD={0} {1} {2} -h {3} -p {4} -d {5} -f {6}".format(PASSWORD, POSTGRESQL_BIN, USER, HOST, PORT, DATABASE, SCRIPTS_DIRECTORY + fichier_script)

    os.system(command)