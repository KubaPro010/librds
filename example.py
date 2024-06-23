import librds

basic = librds.GroupGenerator.basic(0x3000)
print(basic)

ps = librds.GroupGenerator.ps(basic,"hi",0)
print(ps)

print(librds.GroupDecoder.decode(ps))