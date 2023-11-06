from app import create_app
from config import DevConfig

cdp_app = create_app(DevConfig)


# @cdp_app.route('/welcome')
# def welcome_add():
#     return "Welcome to calculation app"


if __name__ == '__main__':
    cdp_app.run()
