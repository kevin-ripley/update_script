import re
filename = '/Users/kripley/Sites/wisetail-api/routes/api/api.php'
temp_f = 'routes.md'
new_f = 'compare.md'
p_class = '(\*.*)'
p_method = '(Route::(\w*))'
p_endpoint = "(\('.*',)"
n_words = "[^*,\n]*"
n_match = []
matches = []

with open(filename, 'r') as f:
    lines = f.readlines()

for line in lines:
    m_class = re.search(p_class, line)
    m_method = re.search(p_method, line)
    m_endpoint = re.search(p_endpoint, line)
    if m_class:
        new_line = m_class.group() + '\n' + '\n'
        matches.append(new_line)
    if m_method:
        new_line = m_method.group()
        matches.append(new_line)
    if m_endpoint:
        new_line = m_endpoint.group() + '\n'
        matches.append(new_line)

with open(temp_f, 'w') as f:
    f.seek(0)
    f.writelines(matches)

with open(temp_f, 'r') as f:
    lines = f.readlines()

for method in lines:
    n_doc = re.search(n_words, method)
    if n_doc:
        new_line = n_doc.group() + '\n'
        n_match.append(new_line)

with open (new_f, 'w') as f:
    f.seek(0)
    f.writelines(n_match)