class Image:

    def __init__(self, resolution, title, extension):
        self.resolution = str(resolution)
        self.title = str(title)
        self.extension = str(extension)

    def resize(self, heigth, width):
        self.resolution = f'{heigth}x{width}'

    def rename(self, new_name):
        self.title = new_name

    def formatting(self, new_format):
        self.extension = new_format

    def __str__(self):
        return self.title + self.extension + f" ({self.resolution})"


image_1 = Image('1920x1080', 'Image_1', '.png')
print(image_1.resolution, image_1.title, image_1.extension)
print(image_1)


image_1.resize(960, 540)
image_1.rename('New_name_image_2')
image_1.formatting('.jpeg')

print(image_1.resolution, image_1.title, image_1.extension)
print(image_1)
