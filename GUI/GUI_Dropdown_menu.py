import c4d
from c4d import gui

class MyDialog(gui.GeDialog):
    def CreateLayout(self):
        # Set the window title
        self.SetTitle("Dockable Dropdown Example")

        # Add a dropdown menu
        self.AddStaticText(1000, c4d.BFH_LEFT, name="Select an Option:")
        self.AddComboBox(1001, c4d.BFH_SCALEFIT, initw=150)
        
        # Populate dropdown menu
        self.AddChild(1001, 0, "Option 1")
        self.AddChild(1001, 1, "Option 2")
        self.AddChild(1001, 2, "Option 3")

        # Add OK and Cancel buttons on the same line
        self.GroupBegin(2000, c4d.BFH_CENTER, cols=2, rows=1, title="")
        self.AddButton(1002, c4d.BFH_SCALEFIT, name="OK")
        self.AddButton(1003, c4d.BFH_SCALEFIT, name="Cancel")
        self.GroupEnd()


    def Command(self, id, msg):
        if id == 1002:  # OK button
            selected_index = self.GetInt32(1001)  # Get selected index
            selected_item = {0: "Option 1", 1: "Option 2", 2: "Option 3"}.get(selected_index, "Unknown")
            gui.MessageDialog(f"You selected: {selected_item}")
        elif id == 1003:  # Cancel button
            self.Close()
        
        return True

# Main function
def main():
    # Create an instance of the custom dialog
    dlg = MyDialog()

    # Open the dialog as a dockable window
    dlg.Open(c4d.DLG_TYPE_ASYNC, defaultw=300, defaulth=150)

if __name__ == "__main__":
    main()
