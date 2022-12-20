streamingservices = ["netflix", "hulu", "amazon prime"]

streamingservices.append("paramount plus")

print(min(streamingservices))

print(len(streamingservices))

streamingservices.append("hulu")

streamingservices.extend(["disney", "netflix"])

print(streamingservices.count("hulu"))

netflix = streamingservices.pop()

subscribed = []

if netflix == "netflix":
    subscribed.append(netflix)

print(subscribed)

subscribed.insert(1,"spotify")

print(subscribed)