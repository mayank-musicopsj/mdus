from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "15599295"))
API_HASH = getenv("API_HASH", "4ce42998f7df4a64934294dadca28ae0")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN", "5889054634:AAGu_lt5U8XmHwZTvVutBhQ75B_16N2q5cY")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001621682412"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://its_star_boi:7234049299@cluster0.8twjh9e.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5463205082").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c5952790fa8235f499749.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/9ad3fc6c595e55438e759.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Best_FriendsFor_Ever ")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/Star_X_Network ")

STRING_SESSION = getenv("STRING_SESSION", "BQAku-Pbl9BuiJYB1515r4zKrg4Yq5FQ-KyLEBITrGydOMz3N0VU_LSUufs0TUWytWna1S8i5CXgmHqdWKjyEOfbPZzugXKQmsX3lC2dbOYf5WY0C2v6aV00_2JSxAgXi_R7nH8Yj3_deytcgb8VLRYnLee-KLVU47RGdHbUhQyvoVVWdKVSIsknSVWncXJ0xB107Wfqtw6V3g8KScVIvGatTc9TWO-SNO7TIhW1EOselNNsmh0cb4wAo5Pg8g8I_fepHY2_Hecg9yMdmFZKz_PEDOcreKNa_HaSdnX-VADtZLXSPJ0X6rhuvY7P9e7zX3SWluMn1zpmFECDIB8MoF10AAAAAUryi9sA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5463205082").split()))
