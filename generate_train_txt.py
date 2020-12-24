import os

with open("train.txt", 'w') as file:
    folder_path = 'FLIR_ADAS_1_3/train/Annotated_thermal_8_bit'
    current = os.getcwd()
    images = [image for image
              in os.listdir(folder_path)
              if image.endswith('.jpeg')]
    for image in images:
        file.write(os.path.join(os.getcwd(), folder_path, image))
        file.write('\n')

with open("valid.txt", 'w') as file:
    folder_path = 'FLIR_ADAS_1_3/val/Annotated_thermal_8_bit'
    current = os.getcwd()
    images = [image for image
              in os.listdir(folder_path)
              if image.endswith('.jpeg')]
    for image in images:
        file.write(os.path.join(os.getcwd(), folder_path, image))
        file.write('\n')
