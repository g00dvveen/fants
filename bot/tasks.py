import db
import env
import logs


class Task:
    def __init__(self, id, image, level, description, sex, section, deferred):
        self.id = id
        self.image = image
        self.level = level
        self.description = description
        self.sex = sex
        self.section = section
        self.deferred = deferred


def get_tasks():
    tasks = []
    db_conn = db.pg_connect(env.db_host, env.db_port, env.db_user, env.db_pass, env.db_name)
    if db_conn != -1:
        cursor = db_conn.cursor()
        cursor.execute("""SELECT id, image, level, description, sex, section, deferred  FROM play_tasks""")
        rows = cursor.fetchall()
        for row in rows:
            task = Task(id=row[0], image=row[1], level=row[2], description=row[3], sex=row[4], section=row[5], deferred=row[6])
            tasks.append(task)
            task = None
        cursor.close()
        db.disconnect(db_conn)
    else:
        logs.logging.error('Connection to database failed')
    return tasks
