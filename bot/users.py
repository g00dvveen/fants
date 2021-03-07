import db, env, logs


def get_users():
    users = []
    db_conn = db.pg_connect(env.db_host, env.db_port, env.db_user, env.db_pass, env.db_name)
    if db_conn != -1:
        cursor = db_conn.cursor()
        cursor.execute("""SELECT id, name, type, connstr, username, password, itil_code, token, dn, sla FROM services_service""")
        rows = cursor.fetchall()
        for row in rows:
            user = {
                'id': row[0],
                'name': row[1],
                'type': row[2],
                'conn_str': row[3],
                'username': row[4],
                'password': row[5],
                'code': row[6],
                'token': row[7],
                'dn': row[8],
                'sla': row[9]
            }
            users.append(user)
            user = None
        cursor.close()
        db.disconnect(db_conn)
    else:
        logs.logging.error('Connection to database failed')
    return users
