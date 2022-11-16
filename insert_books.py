from connecting_to_mysql import connect

def insert_books(books):

    try:
        # Connect to MySQL
        conn = connect()
        cursor = conn.cursor()
        
        # Apply Query
        query = '''
        insert into books(title, isbn)
        values(%s, %s)
        '''

        cursor.executemany(query, books)

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

    books = [('Harry Potter 15','975434397319'),('Harry Potter 16','9781233987318'),('Harry Potter 17','1781479183119')]
    insert_books(books)

if __name__ == '__main__':
    main()