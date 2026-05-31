#StringIndexing
# start : end : step

card = "1234-5678-9012-3456"
print(card[0])
print(card[1])
print(card[-1])
print(card[0:4])#Last No get excluded
print(card[:-2])
print(card[::2])#every second character
print(card[-4:])
print(f"xxxx-xxxx-xxxx-{card[-4:]}")
