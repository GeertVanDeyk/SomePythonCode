import pprint
message = 'the quick brown fox jumps over the lazy black dog.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)
