import psycopg2
from psycopg2.errors import UniqueViolation


def start_table():

    conn = psycopg2.connect(host='localhost', database='anime_stock',
                            user="bruno", password="1234")
    cur = conn.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS animes(
                id BIGSERIAL PRIMARY KEY,
                anime VARCHAR(100) NOT NULL UNIQUE,
                released_date DATE NOT NULL,
                seasons INTEGER NOT NULL)
    """)

    conn.commit()
    cur.close()
    conn.close() 


def connect_to_db(commands: str, fetch_data: bool = False, data_entry: tuple = (), html_method : str = 'get'):
    conn = psycopg2.connect(host='localhost', database='anime_stock',
                            user="bruno", password="1234")
    cur = conn.cursor()
    
    try:
        cur.execute("""
            SELECT * FROM animes
        """)
        
    except Exception:

        start_table()

        if html_method == 'get' or html_method == 'patch':
            return "table doesn't exist"

    try:   
        cur.execute(commands, data_entry)


    except psycopg2.IntegrityError as e:
        assert isinstance(e, UniqueViolation)
        return "anime already exists"

    
    if fetch_data:
        getting_data = cur.fetchall()
        FIELDNAMES = ["id", "anime", "released_date", "seasons"]
        processed_data = [dict(zip(FIELDNAMES,row)) for row in getting_data]

        conn.commit()
        cur.close()
        conn.close()

        return processed_data
       
    conn.commit()
    cur.close()
    conn.close()

    pass

    
def get_all():

    command = """SELECT * FROM animes """

    return connect_to_db(command, True, (), 'get')


def post_one(data):

    data['anime'].title()
    
    command = """
            INSERT INTO animes
                ("id", "anime", "released_date", "seasons")
            VALUES
                (DEFAULT, %s, %s, %s);
        """
    
    data_entry = (data['anime'], (data['released_date']), (data['seasons'], ))

    return connect_to_db(command, False, data_entry, 'post')


def check_post_or_patch_entries(data : dict):
    
    request_needs = ["anime", "released_date", "seasons"]
    wrong_fields = {"available_keys" : ["anime", "released_date", "seasons"],
            "wrong_keys_sended" : []
    }
    data_keys = data.keys()
 
    for key in data_keys:
        if not key in request_needs:
            wrong_fields['wrong_keys_sended'].append(key)
    if len(wrong_fields['wrong_keys_sended']) == 0:
        return False
    return wrong_fields


def get_specific_id(id: int):

    command = """
    SELECT * FROM animes WHERE id=(%s)
    
    """

    data_entry = (id,)

    return connect_to_db(command, True, data_entry, 'get')


def patch_one(id : int, data: dict):

    keys = data.keys()
    
    try:
        anime_info = get_specific_id(id)[0]
    except IndexError:
        return 'Not Found'

    data_id = anime_info['id']

    del anime_info['id']

  
    for key in keys:
        anime_info[key] = data[key]

    command = """
    UPDATE animes 
    SET
        anime=(%s),
        released_date=(%s),
        seasons=(%s)
    
    WHERE
    id=(%s)
    
    """

    data_entry = (anime_info['anime'],anime_info['released_date'],anime_info['seasons'],id,)

    connect_to_db(command, False, data_entry, 'patch')

    anime_info['id'] = data_id

    return anime_info


def delete_one(id):

    teste_id = get_specific_id(id)

    if teste_id == []:
        return 'Not Found'

    command = """ 
    DELETE 
    FROM
        animes
    WHERE
        id=(%s)
    RETURNING *;
    
    """

    data_entry = (id,)

    connect_to_db(command, False, data_entry, 'delete')

    return ""