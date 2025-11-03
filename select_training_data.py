import os
import random
import shutil
import math

if __name__ == "__main__":
    directory = "./original_training_data"
    patients = set()
    for filename in os.listdir(directory):
        name, _ = os.path.splitext(filename)
        name = name.split("_")[0]
        patients.add(name)
    patients = list(patients)
    random.shuffle(patients)
    print(len(patients))
    for i, id in enumerate(patients):
        if i < math.floor(len(patients)*0.8):
            for filename in os.listdir(directory):
                if id in filename:
                    shutil.copyfile(f"{directory}/{filename}", f"./training_dataset_v3/{filename}")
        elif i < math.floor(len(patients)*0.9):
            for filename in os.listdir(directory):
                if id in filename:
                    shutil.copyfile(f"{directory}/{filename}", f"./test_dataset_v3/{filename}")
        else:
            for filename in os.listdir(directory):
                if id in filename:
                    shutil.copyfile(f"{directory}/{filename}", f"./validation_dataset_v3/{filename}")


