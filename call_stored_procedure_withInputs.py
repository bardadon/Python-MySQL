from connecting_to_mysql import connect

def call_procedure_withInputs():

    try:
        # Connect to MySQL
        conn = connect()
        cursor = conn.cursor()

        # Call Procedure
        cursor.execute('call find_by_isbn(1234404543724, @title)')
        cursor.execute('select @title as title;')
        results = cursor.fetchone()[0]

        # Print Results
        print(results)

    except Exception as e:
        print(e)

    finally:
        # Close connections
        print('Closing Connection')
        cursor.close()
        conn.close()


def main():

    call_procedure_withInputs()

if __name__ == '__main__':
    main()