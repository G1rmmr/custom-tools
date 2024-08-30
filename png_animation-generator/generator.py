from PIL import Image
import os

IMG_DIR = "frames"
SPRITE_DIR = "sprites"
ANIM_DIR = "animations"

class Sprite:
  def __init__(self, name: str):
    self.name = name
    self.imp_path = IMG_DIR + '/' + self.name
    self.exp_path = SPRITE_DIR + '/' + self.name
  
  def generate(self):
    if(os.path.exists(self.exp_path)):
      print(f"A sprite {self.name} is already exist!")
      return
    
    frame_files = [os.path.join(IMG_DIR, file)
      for file in os.listdir(IMG_DIR) if file.endswith(".PNG")]
    
    frame_files.sort()

    frames = [Image.open(file) for file in frame_files]

    frame_width, frame_height = frames[0].size

    sheet_width = frame_width * len(frames)
    sheet_height = frame_height

    sprite_sheet = Image.new("RGBA", (sheet_width, sheet_height))

    for i, frame in enumerate(frames):
      sprite_sheet.paste(frame, (i * frame_width, 0))

    sprite_sheet.save(self.exp_path + ".PNG")
    print(f"A sprite {self.name} saved in directory : {SPRITE_DIR}")

    return
  
class Anim:
  def __init__(self, name: str):
    self.name = name
    self.imp_path = SPRITE_DIR + '/' + self.name
    self.exp_path = ANIM_DIR + '/' + self.name
  
  def generate(self):
    if(os.path.exists(self.exp_path)):
      print("A animation set {self.name} is already exist!")
      return
    
    sprite_files = [os.path.join(SPRITE_DIR, file)
      for file in os.listdir(SPRITE_DIR) if file.endswith(".PNG")]
    
    sprite_files.sort()

    sprites = [Image.open(file) for file in sprite_files]

    anim_width = max(list(map(lambda sprite: sprite.size[0], sprites)))
    anim_height = sprites[0].size[1]

    anim_set = Image.new("RGBA", (anim_width, len(sprites) * anim_height))

    for i, sprite in enumerate(sprites):
      sprite_width, sprite_height = sprite.size
      anim_set.paste(sprite, (0, i * anim_height))

    anim_set.save(self.exp_path + ".PNG")
    print(f"A sprite {self.name} saved in directory : {ANIM_DIR}")

    return