# OpenBCI
EEG signals are collected using OpenBCI, during the execution of motor activities, motor imaging and motion observation!
- Last Changes (18/02/2024)

New version of data acquisition in folder **"AcquisitionProgram_V2.0"** , with two methods.
- Method 1 : Using pyLSL (Library) and OpenBCI_GUI
- Method 2 : Using Brainflow (Library)

Note: Check the path of the images and the folder to save the files

⭐ Explanatory Video of Data Acquisition Codes:
- https://www.youtube.com/watch?v=h6JpvZ4K_Ik

⭐ When using this resource, please cite the original publication:
- [Asanza, V., Lorente-Leyva, L. L., Peluffo-Ordóñez, D. H., Montoya, D., & Gonzalez, K. (2023). MILimbEEG: A dataset of EEG signals related to upper and lower limb execution of motor and motor imagery tasks. Data in Brief, 50, 109540.](https://doi.org/10.1016/j.dib.2023.109540)

# MILimbEEG
Biomedical Electroencephalography (EEG) signals are the result of measuring the electric potential difference generated on the scalp surface by neural activity corresponding to each brain area. Accurate and automatic detection of neural activity from the upper and lower limbs using EEG may be helpful in rehabilitating people suffering from mobility limitations or disabilities. This article presents a dataset containing 7440 CSV files from 60 test subjects during motor and motor imagery tasks. The motor and motor imagery tasks performed by the test subjects were: Closing Left Hand (CLH), Closing Right Hand (CRH), Dorsal flexion of Left Foot (DLF), Plantar flexion of Left Foot (PLF), Dorsal flexion of Right Foot (DRF), Plantar flexion of Right Foot (PRF) and Resting in between tasks (Rest). The volunteers were recruited from research colleagues at ESPOL and patients at the Luis Vernaza Hospital in Guayaquil, Ecuador. Each CSV file has 501 rows, of which the first one lists the electrodes from 0 to 15, and the remaining 500 rows correspond to 500 data recorded during the task is performed due to sample rate. In addition, each file has 17 columns, of which the first one indicates the sampling number and the remaining 16 columns represent 16 surface EEG electrodes. As a data recording equipment, the OpenBCI is used in a monopolar setup with a sampling rate of 125 Hz. This work includes statistical measures about the demographic information of all recruited test subjects. Finally, we outline the experimental methodology used to record EEG signals during upper and lower limb task execution. This dataset is called MILimbEEG and contains microvolt (µV) EEG signals acquired during motor and motor imagery tasks. The collected data may facilitate the evaluation of EEG signal detection and classification models dedicated to task recognition.

- Main Code: https://github.com/Human-Machine-Interface/OpenBCI_Data_Acquisition
- Data Mendeley: http://dx.doi.org/10.17632/w9xfz56txv.1
- More Matlab Examples: https://github.com/Human-Machine-Interface
- Hardware: FM=16 chanels , Cyton + Dasy , Campling Rate = 125 Hz
- Subjects: 24
