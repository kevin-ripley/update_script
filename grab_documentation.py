import re
filename = '/Users/kripley/Sites/wisetail-api-documentation/Contents.md'
temp_file = 'content.md'
# First Regex
regex_class = '\[\w*\s*\w*\s*\w*\]*'
regex_delete = '(\[|\])'
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

with open(temp_file, 'r') as f:
    lines = f.readlines()

for line in lines:
    place = re.sub(regex_delete, '')