import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname("../"))))

from grid_vid import generate_interpolation_video
import typer
from pathlib import Path
import dropbox
from tqdm import tqdm
import moviepy.editor
KEY = "sl.AnbDqyYjg1X8mn03l6uMasEphd4KOJLSmCqNHYC5joeD1sMg0D7yFo5tWtP0LuwSuB99QmKrJGaLYTsZ3CWyAPJdMbejaUacL6X2Ui5xzgGTbMRbEOqPasDy3VbBEu-WREOBHSKPnZE"


if __name__ == "__main__":
    dbx = dropbox.Dropbox(KEY)
    
    filename = "./temp.mp4"
    for i in tqdm(range(13)):
        if os.path.isfile(f'./audio/{i}.wav'):
            audiopath = f'./audio/{i}.wav'
        elif os.path.isfile(f'./audio/{i}.mp3'):
            audiopath = f'./audio/{i}.mp3'
        audioclip = moviepy.editor.AudioFileClip(audiopath)
        generate_interpolation_video(
            net=Path("network-snapshot-009456.pkl"), 
            random_seed=i, mp4=Path(filename), output_width=None, grid_size=(2,2),
            duration_sec=audioclip.duration,
            audio=audioclip
        )

        pathname = os.path.join("/league_of_legends", f'{i}.mp4')

        with open(filename, "rb") as f:
            dbx.files_upload(f.read(), pathname, mode=dropbox.files.WriteMode.overwrite)
        
