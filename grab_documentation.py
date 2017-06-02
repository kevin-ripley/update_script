import re
filename = '/Users/kripley/Sites/wisetail-api-documentation/update_doc.txt'
temp_file = 'content.md'
# First Regex
regex_class = '[A-Z]\w*'

matches = []

with open(filename, 'r') as f:
    lines = f.readlines()

for line in lines:
    m_class = re.search(regex_class, line)

    if m_class:
        new_line = '\n' + m_class.group() + '\n'
        matches.append(new_line)


with open(temp_file, 'w') as f:
    f.seek(0)
    f.writelines(matches)
