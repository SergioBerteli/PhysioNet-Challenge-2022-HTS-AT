import os
"""
Select and copy patient-level training, test, and validation splits from a directory
of original files.

This script performs a patient-level split of files found in "./original_training_data".
It infers a patient identifier from each filename by taking the substring before the
first underscore ("_"). All files that share the same patient identifier are kept
together and placed into one of three destination directories:

- "./training_dataset_v3/"      : first 80% of patients (floor)
- "./test_dataset_v3/"          : next 10% of patients (floor)
- "./validation_dataset_v3/"    : remaining patients

Behavior:
- Collects unique patient identifiers from filenames in "./original_training_data".
- Randomly shuffles the patient list using random.shuffle (non-deterministic unless
    the random seed is set externally).
- Uses math.floor(len(patients) * 0.8) and math.floor(len(patients) * 0.9) to determine
    split indices.
- For each patient id, iterates over all filenames in the original directory and
    copies any file whose filename contains the patient id as a substring into the
    corresponding destination directory using shutil.copyfile.

Assumptions and requirements:
- The script is intended to be run as a standalone program (guarded by if __name__ == "__main__").
- The working directory should contain the "./original_training_data" directory.
- Destination directories ("./training_dataset_v3", "./test_dataset_v3", "./validation_dataset_v3")
    must exist prior to running; the script does not create them.
- Filenames are expected to include the patient id as the first token before an underscore.
- The matching test uses substring containment ("if id in filename"), which can lead to
    incorrect matches if one patient id is a substring of another.
- The copy operation will overwrite files of the same name in the destination.

Caveats and possible improvements:
- Make the split deterministic by calling random.seed(...) or by using a fixed shuffle.
- Create destination directories if they do not exist (os.makedirs(..., exist_ok=True)).
- Use exact matching of the patient id token rather than substring containment to avoid
    accidental cross-matching when patient ids overlap.
- Avoid repeatedly listing the source directory inside the per-patient loop by caching its
    contents for efficiency.
- Consider using shutil.copy2 to preserve metadata if desired.

Example usage:
        Run the script from the repository root (or adjust paths) to perform the split:
                python select_training_data.py
"""
import random
import shutil
import math

if __name__ == "__main__":
    directory = "./original_training_data" # pasta contentendo o conjunto de dados
    patients = set() # estrutura de dados garantindo que haja valores unicos (id dos pacientes)
    for filename in os.listdir(directory): # para cada arquivo no diretório com os dados, é colado o nome do paciente que teve o som cardíaco gravado.
        name, _ = os.path.splitext(filename)
        name = name.split("_")[0]
        patients.add(name)
    patients = list(patients)
    random.shuffle(patients) # lista de pacientes é reorganizada  aleatóriamente
    for i, id in enumerate(patients): # 80 % dos pacientes são colocados na pasta de treino, 10 na de validação e 10 na de teste.
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


