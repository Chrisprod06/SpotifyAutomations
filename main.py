import httpx

from secrets import client_id, client_secret

"""
- Create Favorite Playlists:
  - Extract favorite songs.

- Organize by Criteria:
  - Split by decade/genre.

- Generate Playlist Stats:
  - Analyze artist data.

- Auto-Remove Unheard:
  - Remove infrequent songs.
"""


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
    user_input = input("Please choose an option:")
    while not user_input:
        user_input = input("Please choose an option:")
    return user_input


def main():
    """
    This is the main function in the program that will handle all the logic
    :return:
    """
    # Indicate the start of the program
    print("Welcome to spotify-automations")
    try:
        # Authenticate the user
        access_token = auth_spotify()
        # Show menu and get input from user
        automation_choice = handle_menu()
        if automation_choice == 0:
            exit()

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
