import moviepy.editor as mp
import argparse
import os

# Construct argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=False,
                help="Folder location of videos for conversion")
ap.add_argument("-o", "--output", required=False,
                help="Extracted audio location")
args = vars(ap.parse_args())

directory = args["input"]
# output = args["output"]

for file in os.listdir(directory):
    if file.endswith(".mp4"):
        # print(os.path.join(directory, file))
        clip = mp.VideoFileClip(f"{directory}{file}")
        clip.audio.write_audiofile(f"extractedAudio/{file}.mp3")
        print(f"{file} has been converted to audio successfully")
        continue
    else:
        continue
