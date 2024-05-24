from twitter.scraper import Scraper

import json


# sign-in with cookies
scraper = Scraper(
    cookies={
        "ct0": "39acaaddec983399cc6c4a37e83d4f9e2539cad87d2acebf822c68672ac707bb11c12ff0cbae1656995d6cbe6d2cb7646b9228bf99dfc7ce06b06dfdf46406d62c2764ba4c0772bb91a082c91a279b94",
        "auth_token": "277359860d70c22db5f99899d364b67b3aaaeb6a"
    }
)

followings = scraper.following([785677020881530880])
data = []

for follower in followings:
    if "data" in follower and "user" in follower["data"] and "result" in follower["data"]["user"] and \
            "timeline" in follower["data"]["user"]["result"] and "timeline" in follower["data"]["user"]["result"]["timeline"] and \
            "instructions" in follower["data"]["user"]["result"]["timeline"]["timeline"]:
        entries = follower["data"]["user"]["result"]["timeline"]["timeline"]["instructions"][0]
        if "entries" in entries:
            entries = entries["entries"]
        else:
            continue

        for entry in entries:
            if "content" in entry and "itemContent" in entry["content"] and "user_results" in entry["content"]["itemContent"] and \
                    "result" in entry["content"]["itemContent"]["user_results"] and "legacy" in entry["content"]["itemContent"]["user_results"]["result"]:
                result = entry["content"]["itemContent"]["user_results"]["result"]["legacy"]

                data.append({
                    "id": entry["content"]["itemContent"]["user_results"]["result"]["rest_id"],
                    "name": result["name"],
                    "screen_name": result["screen_name"],
                    "created_at": result["created_at"],
                })

print(json.dumps(data, indent=4))
