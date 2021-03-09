import db, env, logs


def get_users():
    users = []
    db_conn = db.pg_connect(env.db_host, env.db_port, env.db_user, env.db_pass, env.db_name)
    if db_conn != -1:
        cursor = db_conn.cursor()
        cursor.execute("""SELECT id, name, sex, partner_name, level, current_task  FROM play_telegramusers""")
        rows = cursor.fetchall()
        for row in rows:
            user = User(id=row[0], name=row[1], sex=row[2], partner_name=row[3], level=row[4], current_task=row[5])
            users.append(user)
            user = None
        cursor.close()
        db.disconnect(db_conn)
    else:
        logs.logging.error('Connection to database failed')
    return users


def get_name(user_id, users):
    for user in users:
        if user['id'] == user_id:
            return user['name']
            break


def get_user(user_id):
    db_conn = db.pg_connect(env.db_host, env.db_port, env.db_user, env.db_pass, env.db_name)
    if db_conn != -1:
        cursor = db_conn.cursor()
        cursor.execute("""SELECT id, name, sex, partner_name, level, current_task FROM play_telegramusers WHERE id = %s;""", (user_id,))
        row = cursor.fetchone()
        if row is not None:
            user = User(id=row[0], name=row[1], sex=row[2], partner_name=row[3], level=row[4], current_task=row[5])
        else:
            user = User(id='0', name='', sex='', partner_name='', level='', current_task=0)
        cursor.close()
        db.disconnect(db_conn)
    else:
        logs.logging.error('Connection to database failed')
    return user


class User:
    def __init__(self, id, name, sex, partner_name, level, current_task):
        self.id = id
        self.name = name
        self.sex = sex
        self.partner_name = partner_name
        self.level = level if level is not None else None
        self.current_task = int(current_task) if current_task is not None else 0

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_level(self):
        return self.level

    def get_partner_name(self):
        return self.partner_name

    def get_current_task(self):
        return self.current_task

    def save(self):
        db_conn = db.pg_connect(env.db_host, env.db_port, env.db_user, env.db_pass, env.db_name)
        if db_conn != -1:
            cursor = db_conn.cursor()
            cursor.execute("""INSERT INTO play_telegramusers (id, name, sex, partner_name, level, current_task) VALUES (%s, %s, %s, %s, %s, %s);""",
                           (self.id, self.name, self.sex, self.partner_name, self.level, self.current_task))
            db_conn.commit()
            cursor.close()
            db.disconnect(db_conn)
        else:
            logs.logging.error('Connection to database failed')

    def update(self, user_id):
        db_conn = db.pg_connect(env.db_host, env.db_port, env.db_user, env.db_pass, env.db_name)
        if db_conn != -1:
            cursor = db_conn.cursor()
            cursor.execute("""UPDATE play_telegramusers SET name = %s, sex = %s, partner_name = %s, level = %s, current_task = %s WHERE id = %s;""",
                           (self.name, self.sex, self.partner_name, self.level, self.current_task, user_id))
            db_conn.commit()
            cursor.close()
            db.disconnect(db_conn)
        else:
            logs.logging.error('Connection to database failed')
