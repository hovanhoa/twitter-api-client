from twitter.account import Account


# sign-in with cookies
account = Account(
    cookies={
        "ct0": "39acaaddec983399cc6c4a37e83d4f9e2539cad87d2acebf822c68672ac707bb11c12ff0cbae1656995d6cbe6d2cb7646b9228bf99dfc7ce06b06dfdf46406d62c2764ba4c0772bb91a082c91a279b94",
        "auth_token": "277359860d70c22db5f99899d364b67b3aaaeb6a"
    }
)

for i in range(1000):
    account.reply("comment number {}".format(str(i)), tweet_id=1793566675477872893)
