import os


# telegram settings
token = '1600600333:AAGXJhbx5-RCSRqKJIJ1sUtaq_5obGVoLsw'

# database settings
db_host = os.getenv('DB_HOST', '192.168.1.212')
db_port = os.getenv('DB_PORT', 5432)
db_user = os.getenv('DB_USER', 'python_user')
db_pass = os.getenv('DB_PASS', 'Password.1')
db_name = os.getenv('DB_NAME', 'fants')

# logs settings
log_level = os.getenv('LOG_LEVEL', 'ERROR')