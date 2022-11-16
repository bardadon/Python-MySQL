from connecting_to_mysql import connect

def insert_book(title, isbn):

    try:
        # Connect to MySQL
        conn = connect()
        cursor = conn.cursor()
        
        # Apply Query
        query = '''
        insert into books(title, isbn)
        values(%s, %s)
        '''
        args = (title, isbn)

        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()

    except Exception as e:
        print(e)

    finally:
        # Close connections
        print('Closing Connection')
        cursor.close()
        conn.close()


def main():

    insert_book(
            'Harry Potter 5','9781439187319'
    )

if __name__ == '__main__':
    main()