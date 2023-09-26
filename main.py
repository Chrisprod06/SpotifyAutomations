# local
from automations import split_by_decade, generate_playlist_statistics
from helpers import auth_spotify, handle_menu


def main():
    """
    This is the main function in the program that will handle all the logic
    :return:
    """
    # Indicate the start of the program
    try:
        # Authenticate the user
        access_token = auth_spotify()
        # Show menu and get input from user
        automation_choice = handle_menu()
        if automation_choice == 1:
            split_by_decade(access_token)
        elif automation_choice == 2:
            generate_playlist_statistics(access_token)
        elif automation_choice == 0:
            exit()

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
