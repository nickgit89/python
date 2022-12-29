streamingservices = ["netflix", "hbo max", "hulu", "amazon prime"]

print(sorted(streamingservices))

for streamingservice in streamingservices:
    print(streamingservice)

streamingservices.insert(2, "disney plus")

print(streamingservices)