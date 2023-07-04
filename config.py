
class EnvVariables():
    host = "localhost"
    port = "5432"
    database = "example"
    username = "username"
    password = "password"


def create_postgresql_connection_string(env: EnvVariables):
    return f'postgresql://{env.username}:{env.password}@{env.host}:{env.port}/{env.database}'


def postegres_string():
    return create_postgresql_connection_string(EnvVariables())
