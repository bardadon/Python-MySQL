from connecting_to_mysql import connect

def call_procedure():

    try:
        # Connect to MySQL
        conn = connect()
        cursor = conn.cursor()

        # Call Procedure
        results = cursor.callproc('find_all')

        # Print Results
        print(cursor.fetchall())

    except Exception as e:
        print(e)

    finally:
        # Close connections
        print('Closing Connection')
        cursor.close()
        conn.close()


def main():

    call_procedure()

if __name__ == '__main__':
    main()