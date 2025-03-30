
# spotify_to_mp3

A simple tool to download all your favorite tracks in good quality mp3s.
The script is designed to work on a Linux based machine, so if you are a Windows user please consider using wsl. 





## Installation
Clone the project

```bash
  git clone https://github.com/roccolr/spotify_to_mp3.git
```

Go to the project directory

```bash
  cd ./spotify.mp3
```

python >3.10 is required:

```bash
  sudo apt update 
  sudo apt upgrade -y
  sudo apt install python3
```

after that, run on the current python environment:

```bash
  pip install -r requirements.txt
```

Now you can run the scipt. Provide the output path as an argument to the script and the spotify user id. The script will download every track in every playlist owned by the user provided, organizing files in directories according to the playlists' names.

```bash
  python3 main.py /absolute/output/path userid123456789 preserve
```

## Configuration
In order to run this script locally, you must create a .env file in modules directory. Make sure you have your spotify API credentials and you can initialize the file as follows:


```bash
  CLIENT_ID = "your_client_id"
  SECRET_ID = "your_secret_id"

```

## Usage
You have to pass 3 arguments to the script: output path, user id and a download mode. The download mode is either "preserve" or "no-preserve". The preserve mode will preserve the playlist structure creating a subdirectory for each playlist with the same name, while the no-preserve mode will download all the tracks togheter in the single directory specified in the first argument. 
    
