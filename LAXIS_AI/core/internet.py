from duckduckgo_search import DDGS


class InternetSearch:

    def search(self, query, limit=5):

        results = []

        try:

            with DDGS() as ddgs:

                data = ddgs.text(query, max_results=limit)

                for item in data:

                    results.append(
                        f"{item['title']}\n{item['body']}"
                    )

        except Exception as e:

            print(e)

        return "\n\n".join(results)