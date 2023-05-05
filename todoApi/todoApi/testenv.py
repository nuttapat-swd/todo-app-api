import environ

env = environ.Env()
environ.Env.read_env()

print(env("DB_NAME"))

