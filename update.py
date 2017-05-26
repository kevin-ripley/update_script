import re
filename = '/Users/admin/Sites/wisetail-api/routes/api.php'
new_f = 'routes.md'
pattern = ''
#(Route::(.*))
matches = []

with open(filename, 'r') as f:
    lines = f.readlines()

for line in lines:
    match = re.search(pattern, line)

    if match:
        new_line = match.group() + '\n' + '\n'

        matches.append(new_line)
with open(new_f, 'w') as f:
    f.seek(0)
    f.writelines(matches)
