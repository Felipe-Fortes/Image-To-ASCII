import PIL.Image

ASCII_CHARS = ["@","%","#","*","+","=","-",":",".",",",";","?","!"]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[min(pixel//25, len(ASCII_CHARS)-1)] for pixel in pixels])
    return(characters)

def main(new_width=100):
    path = input("Caminho valido da imagem:\n")
    try:
        image = PIL.Image.open(path)
    except Exception as e:
        print(f"{path} nao e um caminho valido. Erro: {e}")
        return

    new_image_data = pixel_to_ascii(grayify(resize_image(image)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i +new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

main()