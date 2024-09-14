from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = list(map(lambda pk: int(pk), env.list("ADMINS")))

# NOTIFY_BOT_TOKEN = env.str("NOTIFY_BOT_TOKEN")
# NOTIFY_CHANNEL_ID = env.str("NOTIFY_CHANNEL_ID")
STATUS_IDS = {
    4: 'Опубликован',
    5: "Удалён со стороны заказчика",
    7: "Отклонено модератором",
    10: "Протокол сформирован",
    11: "Отказан на протокол",
    12: "Торг не состоялся",
}
