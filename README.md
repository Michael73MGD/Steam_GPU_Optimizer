# Steam_GPU_Optimizer
Calculate number of playable games on steam based on GPU performance and system requirements

# Steam Games Scraper

Modifications to the linked repo, 'Steam-Games-Scraper' allow scraping steam games for their system requirements. We are only interested in a games name and its recommended system requirements. These will be saved in a csv file. Then, the GPU Database will allow a conversion from GPU name to a G3D score. This will saved as well and used for comparisons. 

# GPU Database

GPU database was obtained from PassMark, and associates each GPU with a G3D score. For simplification, this score is used to measure the performance of GPUs for comparison. 

# Main

The main.py file will analyze GPUs on sale now using the prices from the GPU database. It will then analze how many games are playable by comparing the GPU's performance score with the performance score associated with each game. 