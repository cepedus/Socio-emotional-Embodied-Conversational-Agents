
# Upper Facial Gesture Generation based on Speech Prosody (INF642 2020-2021)

**Part of the curriculum of the Master in Artificial Intelligence and Advanced Visual Computing at École Polytechnique**

*Author: Martín Cepeda*

Repo for the mini-project of the course "Socio-emotional Embodied Conversational Agents". Lab Instructor: Mireille Fares ([mf.upmc@gmail.com](mailto:mf.upmc@gmail.com))

All the scripts and snippets are made and run on my own system:

- CPU: i7-9750H @ 2.60GHz
- RAM: 16 GB @ 2667MHz
- Disk: 970 EVO Plus 1TB
- GPU: GTX 1650
- OS: Microsoft Windows 10 Pro
- Shell: Windows PowerShell

## Lab 1: Acoustic and Visual Data Preprocessing

### Getting the data

1. Download youtube-dl binary from [here](http://ytdl-org.github.io/youtube-dl/download.html), save to `.\tools\youtube-dl` subdirectory

2. Download videos in `.mp4` format:
```powershell
cd $HERE
.\tools\youtube-dl\youtube-dl -o ".\data\%(id)s.%(ext)s" --batch-file ".\VideoIDs.txt" -f mp4
```

3. Extract audio to a `.wav` file (original quality):
```powershell
foreach ($i in @(gci ".\data" -file *.mp4)){ffmpeg -i ".\data\$i" -vn -acodec pcm_s16le -ar 44100 -ac 2 ".\data\audio\$i.wav"}
```

4. Rename audio files from `ID.mp4.wav` to `ID.wav`:
```powershell
foreach ($i in @(gci ".\data\audio" -file *.wav)){Rename-Item -path $i.FullName -newname $i.Name.Replace(".mp4","")}
```

Videos are now stored in `.\data` and corresponding audio in `.\data\audio`

### OpenSMILE

1. Download binaries from [here](https://github.com/audeering/opensmile/releases/tag/v3.0.0), extract to `.\tools\opensmile-3.0-win-x64` subdirectory.

2. Configuration file: see XXXXXX.md

3. Extract audio features (Fundamental Frequency F0, Mel Frequency, Jitter, Shimmer, and Harmonic to Noise Ratio HNR):
```powershell
cd $HERE
mkdir .\data\audio_features
foreach ($i in @(gci ".\data\audio" -file *.wav)){.\tools\opensmile-3.0-win-x64\bin\SMILExtract.exe -C ".\src\MyConf.conf" -I ".\data\audio\$i" -O ".\data\audio_features\$i.csv"}
```

4. Rename features files from `ID.wav.csv` to `ID.csv`:
```powershell
foreach ($i in @(gci ".\data\audio_features" -file *.csv)){Rename-Item -path $i.FullName -newname $i.Name.Replace(".wav","")}
```


### OpenFace

1. Download openface from [here](https://github.com/TadasBaltrusaitis/OpenFace/releases/tag/OpenFace_2.2.0) and extract to `.\tools\OpenFace_2.2.0_win_x64` subdirectory.  Command line usage info is [here](https://github.com/TadasBaltrusaitis/OpenFace/wiki/Command-line-arguments)

2. Download models (authorize external scripts previously from elevated shell with `Set-ExecutionPolicy Bypass`):
```powershell
cd $HERE
cd OpenFace_2.0.0_win_x64
.\download_models.ps1
```

3. Extract features for all videos: ⚠️⚠️ THIS TAKES LONG (2h30) AND USES 50% OF THE CPU AND 1GB OF RAM WHILE RUNNING ⚠️⚠️
```powershell
cd $HERE
foreach ($i in @(gci ".\data" -file *.mp4)){.\tools\OpenFace_2.2.0_win_x64\FeatureExtraction.exe -root .\data -f $i -out_dir .\data\face_features}
```

Face features are now stored in `.\data\face_features`. Format of the features is available [here](https://github.com/TadasBaltrusaitis/OpenFace/wiki/Output-Format#featureextraction)

### Python setup

I'll be using Python 3.8, managed by [Anaconda](https://www.anaconda.com/products/individual).

1. Setup environment:
```bash
cd $HERE
conda create --name chatbots python=3.8
conda activate chatbots
conda install -c conda-forge --file requirements.txt
```

2. Run Jupyter and open notebook `Lab_1.ipynb`:
```bash
cd $HERE
jupyter notebook
```

install opensmile `pip install opensmile`
install transformers `pip install transformers`