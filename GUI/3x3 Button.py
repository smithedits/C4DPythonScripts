import c4d

class MyDialog(c4d.gui.GeDialog):
    def CreateLayout(self):
        # Create a 3x3 grid of buttons
        self.GroupBegin(0, c4d.BFH_SCALEFIT, 3, 3, "Button Group")
        self.AddButton(1, c4d.BFH_SCALEFIT, name="◽")
        self.AddButton(2, c4d.BFH_SCALEFIT, name="◽")
        self.AddButton(3, c4d.BFH_SCALEFIT, name="◽")
        self.AddButton(4, c4d.BFH_SCALEFIT, name="◽")
        self.AddButton(5, c4d.BFH_SCALEFIT, name="◽")
        self.AddButton(6, c4d.BFH_SCALEFIT, name="◽")
        self.AddButton(7, c4d.BFH_SCALEFIT, name="◽")
        self.AddButton(8, c4d.BFH_SCALEFIT, name="◽")
        self.AddButton(9, c4d.BFH_SCALEFIT, name="◽")
        self.GroupEnd()
        
        return True

    def Command(self, id, msg):
        # Handle button click events
        if id >= 1 and id <= 9:
            c4d.gui.MessageDialog("Button {} clicked!".format(id))
        
        return True

# Main function
def main():
    # Create an instance of the dialog
    dialog = MyDialog()
    # Open the dialog
    dialog.Open(c4d.DLG_TYPE_MODAL, defaultw=200, defaulth=200)

# Execute main()
if __name__=='__main__':
    main()
