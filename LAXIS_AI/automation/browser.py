import webbrowser


class Browser:

    def open_google(self):
        webbrowser.open("https://www.google.com")

    def search(self, query):
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)