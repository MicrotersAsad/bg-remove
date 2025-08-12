from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO

app = Flask(__name__)

@app.route('/remove-background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return "No image file provided", 400

    image_file = request.files['image']

    # Process image using rembg
    input_image = image_file.read()
    output_image = remove(input_image)

    # Convert the image to a BytesIO object so that it can be returned in the response
    img_io = BytesIO(output_image)
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
