import os
import glob

files = []

files += glob.glob("line_*.mp4")
files += glob.glob("smiley_*.mp4")
files += glob.glob("colors_to_corners_*.mp4")
print(files)

for file in files:
  print(file)
  file_no_audio = file.split(".mp4")[0]+"_no_audio.mp4"
  file_sped_up = file.split(".mp4")[0]+"_sped_up_no_pause.mp4"
  file_freeze_frame = file.split(".mp4")[0]+"_freeze.mp4"
  file_final = file.split(".mp4")[0]+"_sped_up.mp4"
  os.system(f"ffmpeg -i {file} -c copy -an {file_no_audio}")
  os.system(f'ffmpeg -i {file_no_audio} -filter:v "setpts=0.25*PTS" {file_sped_up}')
  os.system(f'ffmpeg -i {file_sped_up} -vf tpad=stop_mode=clone:stop_duration=50 {file_freeze_frame}')
  if 'colors_to_corners' in file:
    seconds_max = int(23 + 3)
  if 'line' in file:
    seconds_max = int(40 + 3)
  if 'smiley' in file:
    seconds_max = int(47 + 3)
  print(seconds_max)
  os.system(f'ffmpeg -ss 00:00:00 -to 00:00:{seconds_max} -i {file_freeze_frame}  -c copy {file_final}')
  # Just clean up
  os.system(f"rm {file_no_audio}")
  os.system(f"rm {file_sped_up}")
  os.system(f"rm {file_freeze_frame}")
