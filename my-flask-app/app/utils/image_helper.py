def resize_image(image, target_size):
    from PIL import Image
    from io import BytesIO

    img = Image.open(image)
    img = img.resize(target_size, Image.ANTIALIAS)
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

def save_image(image, path):
    with open(path, 'wb') as f:
        f.write(image.read())

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_image_to_grayscale(image):
    from PIL import Image

    img = Image.open(image)
    grayscale_img = img.convert('L')
    return grayscale_img