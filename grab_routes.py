import re
filename = '/Users/kripley/Sites/wisetail-api/routes/api/api.php'
temp_file = 'routes.md'
new_file = 'compare.md'
# First Regex
regex_class = '(\*\s[A-Z]\w*\s\w*)'
regex_method = '(\w*\(.*)\,'
# Final Regex
model = "([A-Z].*)"
url = "(\'(.*)\')"
r_get = "(get)"
r_post = "(post)"
r_patch = "(patch)"
r_delete = "(delete)"

matches = []
finds = []

with open(filename, 'r') as f:
    lines = f.readlines()

for line in lines:
    m_class = re.search(regex_class, line)
    m_method = re.search(regex_method, line)

    if m_class:
        new_line = '\n' + m_class.group() + '\n'
        matches.append(new_line)
    if m_method:
        new_line = m_method.group() + '\n'
        matches.append(new_line)


with open(temp_file, 'w') as f:
    f.seek(0)
    f.writelines(matches)

with open(temp_file, 'r') as f:
    lines = f.readlines()

for method in lines:
    models = re.search(model, method)
    urls = re.search(url, method)
    get = re.search(r_get, method)
    post = re.search(r_post, method)
    patch = re.search(r_patch, method)
    delete = re.search(r_delete, method)

    if models:
        new_line = models.group() + '\n'
        finds.append(new_line)
    if get:
        new_line = get.group() + ' '
        finds.append(new_line)
    if post:
        new_line = post.group() + ' '
        finds.append(new_line)
    if patch:
        new_line = patch.group() + ' '
        finds.append(new_line)
    if delete:
        new_line = delete.group() + ' '
        finds.append(new_line)
    if urls:
        new_line = urls.group() + '\n'
        finds.append(new_line)

with open(new_file, 'w') as f:
    f.seek(0)
    f.writelines(finds)

