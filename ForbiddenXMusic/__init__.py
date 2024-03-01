from ForbiddenXMusic.core.bot import Anony
from ForbiddenXMusic.core.dir import dirr
from ForbiddenXMusic.core.git import git
from ForbiddenXMusic.core.userbot import Userbot
from ForbiddenXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
