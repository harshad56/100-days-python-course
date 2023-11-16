from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk, ImageFont, ImageDraw


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")

        self.image_label = Label(root)
        self.image_label.pack()

        self.upload_button = Button(
            root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.watermark_button = Button(
            root, text="Add Watermark", command=self.add_watermark)
        self.watermark_button.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        self.image = Image.open(file_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)

    def add_watermark(self):
        # Create a transparent image for the watermark
        width, height = self.image.size
        transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))

        # Load a font
        try:
            font = ImageFont.truetype("assets/Agbalumo-Regular.ttf", size=36)
        except IOError:
            font = ImageFont.load_default()

        # Get a drawing context
        draw = ImageDraw.Draw(transparent)
        text = "Matt Still"

        # Calculate text size and position
        text_width, text_height = draw.textsize(text, font)
        text_position = ((width - text_width) // 2,
                         (height - text_height) // 2)

        # Draw the text on the transparent image
        draw.text(text_position, text, fill=(255, 255, 255, 128), font=font)

        # Paste the watermark onto the original image
        self.image.paste(transparent, (0, 0), transparent)

        # Update the displayed image
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)


root = Tk()
app = WatermarkApp(root)
root.mainloop()
