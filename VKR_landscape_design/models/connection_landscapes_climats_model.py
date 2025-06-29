import pandas as pd

def get_connections_landscapes_climats(conn):
    return pd.read_sql('''
        SELECT connection_id, landscape_id, climat_id
        FROM connections_landscapes_climats
    ''', conn)

def get_one_connection_landscapes_climats(conn, user_connection_id):
    return pd.read_sql(f'''
        SELECT connection_id, landscape_id, climat_id
        FROM connections_landscapes_climats
        WHERE connection_id = {user_connection_id}
    ''', conn)

def insert_connection_landscapes_climats(conn, user_landscape_id, user_climat_id):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO connections_landscapes_climats(landscape_id, climat_id)
        VALUES (:userlandscapeid, :userclimatid)
    ''', {
        "userlandscapeid": user_landscape_id,
        "userclimatid": user_climat_id
    })
    conn.commit()

def delete_connection_landscapes_climats(conn, user_connection_id):
    cur = conn.cursor()
    cur.execute('''
        DELETE FROM connections_landscapes_climats
        WHERE connection_id = :connectionid
    ''', {"connectionid": user_connection_id})
    conn.commit()

def update_connection_landscapes_climats(conn, user_connection_id, user_landscape_id, user_climat_id):
    cur = conn.cursor()
    cur.execute('''
        UPDATE connections_landscapes_climats
        SET
            landscape_id = :userlandscapeid,
            climat_id = :userclimatid
        WHERE connection_id = :userconnectionid
    ''', {
        "userconnectionid": user_connection_id,
        "userlandscapeid": user_landscape_id,
        "userclimatid": user_climat_id
    })
    conn.commit()
