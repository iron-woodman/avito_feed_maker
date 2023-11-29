from PIL import Image
import os


SOURCE_FOLDER = 'source'
RESULT_FOLDER = 'result' # with water makr
LOGO_FILE = 'Домасауна_m.png'
# LOGO_FILE = 'logo1.png'
WATERMARK_POS = (0, 1)


def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path,
                                position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path).convert("RGBA")
    width, height = base_image.size

    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)
    # transparent.show()
    # transparent.save(output_image_path)
    transparent.convert('RGB').save(output_image_path)





if __name__ == '__main__':
    if os.path.isdir(SOURCE_FOLDER):
        source_images = os.listdir(SOURCE_FOLDER)
        if len(source_images) == 0:
            print('Исходные изображения не обнаружены')
            exit(1)
        for source_img in source_images:
            print(source_img)
            watermark_with_transparency(SOURCE_FOLDER + "\\" + source_img, RESULT_FOLDER + "\\" + source_img, LOGO_FILE, position=WATERMARK_POS)

        print('работа завершена')