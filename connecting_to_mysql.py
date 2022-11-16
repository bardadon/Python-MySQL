import configparser
import pymysql

# Set a config parser object and read values from pipeline.conf
parser = configparser.ConfigParser()
parser.read('pipeline.conf')

# Grabing the values from the config file
hostname = parser.get("mysql_config", "hostname")
port = parser.get("mysql_config", "port")
username = parser.get("mysql_config", "username")
dbname = parser.get("mysql_config", "database")
password = parser.get("mysql_config", "password")



def connect():

    """ Connect to MySQL database """
    conn = None

    try:
        conn = pymysql.connect(host=hostname,
        user=username,
        password=password,
        db=dbname,
        port=int(port))

    except Exception as e:
        print(e)

    finally:
        if conn.open:
            print('Connected to MySQL database')
            return conn
        

if __name__ == '__main__':
    conn = connect()