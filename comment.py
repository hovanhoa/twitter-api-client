from twitter.scraper import Scraper

import json


# sign-in with cookies
scraper = Scraper(
    cookies={
        "ct0": "39acaaddec983399cc6c4a37e83d4f9e2539cad87d2acebf822c68672ac707bb11c12ff0cbae1656995d6cbe6d2cb7646b9228bf99dfc7ce06b06dfdf46406d62c2764ba4c0772bb91a082c91a279b94",
        "auth_token": "277359860d70c22db5f99899d364b67b3aaaeb6a"
    }
)

tweet_details = scraper.tweets_details([1793566675477872893])
data = []

for tweet in tweet_details:
    if "data" in tweet and \
            "threaded_conversation_with_injections_v2" in tweet["data"] and \
            "instructions" in tweet["data"]["threaded_conversation_with_injections_v2"]:

        entries = tweet["data"]["threaded_conversation_with_injections_v2"]["instructions"][0]["entries"]
        for entry in entries:

            if "content" in entry and "items" in entry["content"]:
                item = entry["content"]["items"][0]["item"]
                if "itemContent" in item and "tweet_results" in item["itemContent"] and \
                        "result" in item["itemContent"]["tweet_results"] and \
                        "legacy" in item["itemContent"]["tweet_results"]["result"]:

                    comment = item["itemContent"]["tweet_results"]["result"]["legacy"]
                    name = item["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["legacy"]["name"]

                    data.append({
                        "user_id": comment["user_id_str"],
                        "name": name,
                        "full_text": comment["full_text"],
                        "created_at": comment["created_at"],
                    })

json_data = json.dumps(data, indent=4)

print(json_data)
print(len(data))
