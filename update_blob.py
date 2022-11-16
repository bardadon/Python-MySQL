from connecting_to_mysql import connect

# Saving a Photo in a column of type: BLOB
def update_blob(author_id, filename):

    def read_file(filename):
        with open(filename, 'rb') as f:
            photo = f.read()
        return photo

    try:
        # Connect to MySQL
        conn = connect()
        cursor = conn.cursor()   

        data = read_file(filename)  

        query = '''
        update authors
        set photo = %s
        where id = %s
        '''
        args = (data,author_id)

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

    update_blob(1, 'Bar.jpg')

if __name__ == '__main__':
    main()