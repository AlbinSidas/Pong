from screen import Screen

if __name__ == "__main__":
    game = Screen()

    # This should be switched to live server at later stage
    url = "http://localhost:3000"

    game.start(url)