from ddgs import DDGS

def search_web(query, max_results=5):
    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r.get("title"),
                "href": r.get("href"),
                "body": r.get("body")
            })

    return results


def build_context(results):
    context = ""

    for r in results:
        context += f"{r['title']}: {r['body']}\n"

    return context


def get_knowledge(query):
    results = search_web(query)
    return build_context(results)
