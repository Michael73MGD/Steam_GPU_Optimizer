import pandas as pd
import csv
import matplotlib.pyplot as plt

'''This needs to investigate a list of GPUs and analze them. '''

test_GPUS = ["GeForce RTX 4090", 'GeForce RTX 3050', 'GeForce GTX 1060', 'GeForce GTX 760']

GPU_df = pd.read_csv('GPU_Database/organized_GPU_database.csv')
GPU_list = GPU_df.values.tolist()

games_df = pd.read_csv('Game_requirements_Database/organized_games_database.csv')
games_list = games_df.values.tolist()

results = []
price_percent = []
for gpu_info in GPU_list:
    if gpu_info[2] == 0.0:
        continue
    else:
        # print(gpu_info[0], 'scores', gpu_info[1])
        playable = 0
        unplayable = 0
        for game in games_list:
            if gpu_info[1] >= game[2]:
                playable += 1
            else:
                unplayable += 1
        percent = float(playable)/(unplayable + playable)*100
        result = [gpu_info[0], gpu_info[1], gpu_info[2], playable, unplayable, percent]
        results.append(result)
        if gpu_info[2] < 1500:
            price_percent.append([gpu_info[2],percent])

gpu_analysis = pd.DataFrame(results)
gpu_analysis.to_csv('gpu_analysis.csv', index=False, header=['GPU', 'Score', 'Price', 'Playable Games', 'Unplayable Games', 'Percent Playable'])
print('File saved to csv')


x, y = zip(*price_percent)

plt.scatter(x, y)
plt.title("Price to Performance")

plt.savefig("Price to Performance.png")
plt.show()