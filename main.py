import re

message_list = []
dataset_file = open('dataset.txt', 'r')
type_regex = r"(.+)\.\s([0-1])"


for line in dataset_file.readlines():
    matches = re.finditer(type_regex, line)
    for matchNum, match in enumerate(matches, start=1):
        message_list.append([match.group(1), match.group(2)])

# Let's create our dictionary
# TODO: Create dictionary

print(message_list)
