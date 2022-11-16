from connecting_to_mysql import connect

def update_title(new_title, isbn):

    try:
        # Connect to MySQL
        conn = connect()
        cursor = conn.cursor()
        
        # Apply Query
        query = """ UPDATE books
                SET title = %s
                WHERE id = %s """
        args = (new_title, isbn)

        cursor.execute(query, args)

        conn.commit()

        print('Update Successful')

    except Exception as e:
        print(e)

    finally:
        # Close connections
        print('Closing Connection')
        cursor.close()
        conn.close()


def main():

    update_title(
            "The Giant on the Hill","37"
    )

if __name__ == '__main__':
    main()