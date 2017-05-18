# coding=utf-8
import os
import sys

COOKIE_SECRET = "R8sEDELfR3yy0M2dfvOgEEIUUZ=Vxbhw3TSWZCzwQeGxff"
COOKIE_DOMAIN = "kanjian.com"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

DB_URL = None
REDIS_SETTINGS = None
DEBUG = False

SEARCH_API_HOST = 'http://192.168.28.123:8060/'  # TODO
ARTIST_SEARCH_API = ''
ALBUM_SEARCH_API = ''
TRACK_SEARCH_API = ''
MV_SEARCH_API = ''

EXPORT_EXCEL_BASEDIR = ''

ENV = None


def apply_env(env):

    global DB_URL
    global ENV
    global REDIS_SETTINGS
    global SEARCH_API_HOST
    global ARTIST_SEARCH_API
    global ALBUM_SEARCH_API
    global TRACK_SEARCH_API
    global MV_SEARCH_API
    global EXPORT_EXCEL_BASEDIR
    ENV = env
    if env == 'personal':
        DB_URL = 'mysql+pymysql://root:@localhost/trade_backend?charset=utf8&use_unicode=1'
        EXPORT_EXCEL_BASEDIR = '/data/music/sell_backend/export'
        REDIS_SETTINGS = {
            'PORT': 15010,
            'DB': 0,
        }
    elif env == 'dev':
        DB_URL = 'mysql+pymysql://root:root@192.168.0.13/sell_backend?charset=utf8&use_unicode=1'
        SEARCH_API_HOST = 'http://192.168.0.11:8060/'
        EXPORT_EXCEL_BASEDIR = '/data/music/sell_backend/export'
        REDIS_SETTINGS = {
            'PORT': 15010,
            'DB': 0,
        }
    elif env == 'production':
        DB_URL = 'mysql+pymysql://sell_backend:j4t2HqD5vewMm9Nc@192.168.100.50/sell_backend?charset=utf8&use_unicode=1'
        SEARCH_API_HOST = 'http://192.168.100.81:19049/'
        EXPORT_EXCEL_BASEDIR = '/data/music/sell_backend/export'
        REDIS_SETTINGS = {
            'HOST': '192.168.100.16',
            'PORT': 15050,
            'DB': 9,
        }
    else:
        raise NotImplementedError

    ARTIST_SEARCH_API = SEARCH_API_HOST + 'searchArtist.htm'
    ALBUM_SEARCH_API = SEARCH_API_HOST + 'searchAlbum.htm'
    TRACK_SEARCH_API = SEARCH_API_HOST + 'searchTrack.htm'
    MV_SEARCH_API = SEARCH_API_HOST + 'searchMV.htm'


def parse_cmd():
    from tornado.options import options, define, parse_command_line
    define(name="config", default="personal")
    define(name="port", default="10037")

    args = sys.argv
    new_args = [args[0]]
    for i in range(1, len(args)):
        if not args[i].startswith("-") or args[i] == "--":  # ignore arguments not startswith '-'
            break
        arg = args[i].lstrip("-")
        key, equals, value = arg.partition("=")
        key = key.replace('_', '-')
        if key in options._options:
            new_args.append(args[i])

    parse_command_line(args=new_args)

    apply_env(options.config)


parse_cmd()
