SQL_DIALECT = 'postgresql'
DRIVER = 'psycopg2'
USER = 'example'
PASSWORD = 'example'
SERVER = 'postgres'
HOST = 'localhost'
DATABASE = 'example'
PORT = '5432'
CONNECTION_URL = f'{SQL_DIALECT}+{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'