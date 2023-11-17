import os

from flask import Flask, render_template, request

from PIL import Image

import numpy as np


app = Flask(__name__)


UPLOAD_FOLDER = 'uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def find_common_colors(image_path, num_colors=5):

    image = Image.open(image_path)

    image = image.convert('RGB')

    image_array = np.array(image)

    pixels = image_array.reshape(-1, 3)

    color_counts = {}

    for pixel in pixels:

        pixel_tuple = tuple(pixel)

    if pixel_tuple in color_counts:

        color_counts[pixel_tuple] += 1

    else:

        color_counts[pixel_tuple] = 1

    sorted_colors = sorted(color_counts, key=color_counts.get, reverse=True)

    return sorted_colors[:num_colors]

    @app.route('/', methods=['GET', 'POST'])
    def upload_file():

        if request.method == 'POST':

            if 'file' not in request.files:

                return render_template('index.html', error="No file part")

            file = request.files['file']

            if file.filename == '':

                return render_template('index.html', error="No selected file")

            if file:

                filename = file.filename

                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                file.save(file_path)

                common_colors = find_common_colors(file_path)

                os.remove(file_path)

                return render_template('result.html', colors=common_colors)

                return render_template('index.html')


if __name__ == '__main__':

    app.run(debug=True)
