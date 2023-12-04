import json
import re
import pandas as pd

'''Read ../Steam-Games-Scraper/games.json'''

# "pc_requirements": {
#             "minimum": "<strong>Minimum:</strong><br><ul class=\"bb_ul\"><li><strong>OS:</strong> Windows 7<br></li><li><strong>Processor:</strong> Intel i3 Processor<br></li><li><strong>Memory:</strong> 2 GB RAM<br></li><li><strong>Graphics:</strong> NVIDIA GeForce GTX 660<br></li><li><strong>DirectX:</strong> Version 11<br></li><li><strong>Storage:</strong> 390 MB available space</li></ul>"
#         },

print('Reading Games Database')
games_db_file = open('../Steam-Games-Scraper/games_30_percent.json', encoding='utf-8')
games_db = json.load(games_db_file)

organized_games_db = []
for game in games_db:
    name = games_db[game]['name']
    pc_requirements = games_db[game]['pc_requirements']
    if type(pc_requirements) == dict and 'minimum' in pc_requirements.keys():
        if 'recommended' in pc_requirements.keys():
            min_spec = pc_requirements['recommended']
        else:
            min_spec = pc_requirements['minimum']
        cleaned_pc_reqs = re.sub('<.*?>', '', min_spec).replace('\n', '')
        if 'Graphics: ' in cleaned_pc_reqs:
            graphics = cleaned_pc_reqs.split('Graphics: ')[1]
            possible_next_entry = ['DirectX: ', 'Storage: ', 'Hard Drive: ', 'Additional Notes: ', 'Network: ', 'VR Support: ']
            for entry in possible_next_entry:
                if entry in graphics:
                    final_graphics = graphics.split(entry)[0]
                    organized_games_db.append([name, final_graphics])
                    break
            else:
                # print("Pattern not recognized: ", graphics)
                # print("--------------------------")
                organized_games_db.append([name, graphics])

games_db_file.close()

# organized_games_df = pd.DataFrame(organized_games_db)
# organized_games_df.to_csv('organized_games_database.csv', index=False, header=None)

# Now, we need to search those graphics requirements for names of GPUs
# This could go in a separate file but I'm doing it here for now, it gets the list of GPUs from the GPU Database

print("Reading GPU Database and linking")
GPU_df = pd.read_csv('../GPU_Database/organized_GPU_database.csv')
GPU_list = GPU_df.values.tolist()
final_games_list= []

for game in organized_games_db:
    requirements = game[1]

    for GPU_row in GPU_list:
        if GPU_row[0] in requirements:
            # print(GPU_row[0])
            final_games_list.append([game[0], GPU_row[0], GPU_row[1]])

            break


organized_games_df = pd.DataFrame(final_games_list)
organized_games_df.to_csv('organized_games_database.csv', index=False, header=['Game', 'GPU', 'Minimum Score'])
print('File saved to csv')
