import kagglehub

path = kagglehub.dataset_download("abdelghaniaaba/wildfire-prediction-dataset")
print("Path to dataset files:", path)

# Move the dataset folder to the git repository folder and rename it to 'dataset'