from duckduckgo_search import DDGS


class WebSearch:

    def search(self, query, max_results=5):

        results = []

        with DDGS() as ddgs:

            for item in ddgs.text(query, max_results=max_results):

                results.append({

                    "title": item["title"],

                    "body": item["body"],

                    "url": item["href"]

                })

        return results