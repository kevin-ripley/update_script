import re
filename = '/Users/kripley/Sites/wisetail-api/routes/api/api.php'
temp_file = 'routes.md'
new_file = 'compare.md'
regex_class = '(\*.*)'
regex_method = '(Route::(\w*))'
regex_endpoint = "(\('.*',)"
n_words = "(get)|(post)|(patch)|(delete)"
url = "(\'(.*)\')"
models = "([A-Z].*)"
non_routes = "((Route))"
matches = []

with open(filename, 'r') as f:
    lines = f.readlines()

for line in lines:
    m_class = re.search(regex_class, line)
    m_method = re.search(regex_method, line)
    m_endpoint = re.search(regex_endpoint, line)
    if m_class:
        new_line = m_class.group() + '\n'
        matches.append(new_line)
    if m_method:
        new_line = m_method.group()
        matches.append(new_line)
    if m_endpoint:
        new_line = m_endpoint.group() + '\n'
        matches.append(new_line)

with open(temp_file, 'w') as f:
    f.seek(0)
    f.writelines(matches)

# with open(temp_f, 'r') as f:
#     lines = f.readlines()
#
# for method in lines:
#     n_doc = re.search(n_words, method)
#     urls = re.search(url, method)
#     mods = re.search(models, method)
#     #mods = re.sub(non_routes,'', method)
#     if n_doc:
#         new_line = n_doc.group() + '\n'
#         n_match.append(new_line)
#     # if urls:
#     #     new_line = urls.group() + '\n'
#     #     n_match.append(new_line)
#     # if mods:
#     #     new_line = mods.group() + '\n' + '\n'
#     #     n_match.append(new_line)
#
# with open(new_f, 'w') as f:
#     f.seek(0)
#     f.writelines(n_match)
