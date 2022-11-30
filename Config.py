import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25648308)
    API_HASH = os.environ.get("API_HASH", "7438ad395b27cd0d43b7d14308dcd011)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5559503630:AAHrPi2hSu7Ks29ASJwuzUI88j0D39_I1sc5559503630:AAHrPi2hSu7Ks29ASJwuzUI88j0D39_I1sc")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGUBuzmmOqlfs7k8MAdylJFzeANLtplYWa053CuOk7dibIzCSbTN2F-AXkKZ2qa1jQFoYMD2yiQCMw7Y93xyVVMBHVv_Z_tt2Tef31SUno0W1Q2UCo2T_G4QccGjBPoWhbOsqjVFKnrpThn0J6ik8HXAMvL9rQl863l9kcqOVnv8qWViXYOlrqMexaa6hn52PfMYOu3kvgoaKrFEogAsTF9uEIDHSNej42U0a_3T3Q2AOqUfgpkfDp-YkKgb1CBuemPn9C_7bxOcNOsiN7L2pFxsjc1JN647ESIa_BJMJOS_Ku6CvhiHaHQBltKdVbZj3GQG381Oi5kjx8F2A7QwrbbyVoE=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Arunplaymusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "YARO_KI_MEHFIL) # Your Support
    CHANNEL = os.environ.get("CHANNEL", "BEST_FRIENDS_FOR_EVERRR) # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5513450014")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
