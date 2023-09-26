# third party
import httpx
# local
from secrets import client_id, client_secret

menu_options = ["Split by decade", "View statistics for playlist"]


def auth_spotify():
    """
    Function used to authenticate spotify
    :return: Access token
    """
    url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = httpx.post(url, data=data)
    access_token = response.json().get("access_token")
    if not access_token:
        raise Exception("Something went wrong while authenticating user.")
    return access_token


def handle_menu():
    """
    Print the available automations menu and get input from user. Remain in loop until he chooses an option
    :return:
    """
    for counter, option in enumerate(menu_options):
        print(f"{counter+1}. {option}")
    print("Press 0 to exit program")
    user_input = input("Please choose an option:")
    while not user_input:
        user_input = input("Please choose an option:")
    return user_input
