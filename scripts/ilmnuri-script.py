import os
from urllib.parse import quote

folders = []

base_url = "https://github.com/cyberspyde/ilmnuri/raw/master/audio/Abdulloh%20domla/"

for f in os.listdir('audio\\audio\\Abdulloh domla\\'):
    files = []
    folders.append(base_url+quote(f))
    for t in os.listdir('audio\\audio\\Abdulloh domla\\'+f):
        files.append(base_url+quote(f)+"/"+quote(t))

    with open(f'audio\\ADM\\ADM-{f}.txt', 'w') as file:
        file.write('\n'.join(files))





#All the files in the folder
# for f in os.listdir('audio\\Abdulloh domla\\'):
#     folders.append(base_url+quote(f))
#     for t in os.listdir('audio\\Abdulloh domla\\'+f):
#         files.append(base_url+quote(f)+"/"+quote(t))

# with open('ADM.txt', 'w') as f:
#     f.write('\n'.join(files))