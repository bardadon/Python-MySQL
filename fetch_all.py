from connecting_to_mysql import connect

def fetchall(input_query):

    try:
        # Connect to MySQL
        conn = connect()
        cursor = conn.cursor()
        
        # Apply Query
        query = input_query
        cursor.execute(query)

        # Fetch Results
        results = cursor.fetchall()
        print(results)

    except Exception as e:
        print(e)

    finally:
        # Close connections
        print('Closing Connection')
        cursor.close()
        conn.close()


def main():
    fetchall('''
    select *
    from books;
    '''
    )

if __name__ == '__main__':
    main()