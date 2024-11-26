import c4d
from c4d import gui

class ImageButtonDialog(gui.GeDialog):
    IMAGE_BUTTON_ID = 1000  # ID for the image button

    def CreateLayout(self):
        # Set the dialog title
        self.SetTitle("Image Button Example")

        # Load the image into a Cinema 4D bitmap object
        self.image = c4d.bitmaps.BaseBitmap()
        result, is_loaded = self.image.InitWith("/Users/xxxx/Desktop/Cube.png")  # Replace with your image path

        if result != c4d.IMAGERESULT_OK:
            gui.MessageDialog("Failed to load the image.")
            return False

        # Add the image as a button
        self.AddCustomGui(self.IMAGE_BUTTON_ID, c4d.CUSTOMGUI_BITMAPBUTTON, "", c4d.BFH_CENTER | c4d.BFV_CENTER, 200, 100)
        image_button = self.FindCustomGui(self.IMAGE_BUTTON_ID, c4d.CUSTOMGUI_BITMAPBUTTON)
        if image_button:
            image_button.SetImage(self.image, True)

        #return True

    def Command(self, id, msg):
        if id == self.IMAGE_BUTTON_ID:
            gui.MessageDialog("Image button clicked!")
        return True

# Main function
def main():
    dlg = ImageButtonDialog()
    dlg.Open(c4d.DLG_TYPE_ASYNC, defaultw=300, defaulth=150)

if __name__ == "__main__":
    main()
