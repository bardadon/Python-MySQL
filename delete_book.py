from connecting_to_mysql import connect

def delete_book(title):

    try:
        # Connect to MySQL
        conn = connect()
        cursor = conn.cursor()
        
        # Apply Query
        query = """ delete from books
                where  title = %s
                """
        args = (title)

        cursor.execute(query, args)

        conn.commit()

        print('Delete Successful')

    except Exception as e:
        print(e)

    finally:
        # Close connections
        print('Closing Connection')
        cursor.close()
        conn.close()


def main():

    delete_book(
            "The Giant on the Hill"
    )

if __name__ == '__main__':
    main()