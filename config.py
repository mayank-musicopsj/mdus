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

STRING_SESSION = getenv("STRING_SESSION", "BQC1WxSWFadXBQQ8osLp5B_wKXcNIExSpIyJNC35EhbXFzGk4H8wrXnbO0olRkZL5B35_ahVCk9i5COqOO6HyWSYZv1aTn50xzpOI-zkRDOIFO8ngjz4nVTPaDWr3Hi7jVBFwwSkvW_ktnBKMw3PN_JeiC07D2YwjOnYlF39zc6XXxJYH0E9GHQIQLzpd15YhZ6tOcv_OENuk77YjG65CG5nJ9Vwc8-akyhTsZm-rLyKYPhApWMEpxuDvz-ShjMylooy1jPlrz_TDGAGU5mNo0g5hiasZ6iBoGU39-8U9Zq15l180LOSDSqEqDlgI3FnSIEQZ5xz67fshZVnJNeAHqcnAAAAAUryi9sA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5463205082").split()))
