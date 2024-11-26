import c4d
from c4d import gui

class CustomDialog(gui.GeDialog):
    def CreateLayout(self):
        # Set the dialog title
        self.SetTitle("Custom Asset Library")

        # Create a fold group for categories
        self.GroupBegin(1000, c4d.BFH_SCALEFIT, 1, 1, title="Categories")
        self.AddComboBox(1001, c4d.BFH_SCALEFIT)
        self.AddChild(1001, 0, "Doodads")
        self.AddChild(1001, 1, "Everyday Models")
        self.AddChild(1001, 2, "Neon Lettersets")
        self.GroupEnd()

        # Create a fold group for the asset grid
        self.GroupBegin(2000, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1, 1, title="Assets")
        self.ScrollGroupBegin(2001, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, scrollflags=c4d.SCROLLGROUP_VERT)
        self.GroupBegin(3000, c4d.BFH_SCALEFIT, cols=4)  # Grid layout with 4 columns
        for i in range(16):  # Add 16 assets as buttons
            self.AddButton(4000 + i, c4d.BFH_SCALE, name=f"Asset {i + 1}")
        self.GroupEnd()
        self.GroupEnd()  # End ScrollGroup
        self.GroupEnd()  # End fold group for assets

        # Create a fold group for search
        self.GroupBegin(5000, c4d.BFH_SCALEFIT, 1, 1, title="Search")
        self.AddStaticText(5001, c4d.BFH_LEFT, name="Search:")
        self.AddEditText(5002, c4d.BFH_SCALEFIT)
        self.GroupEnd()

        # Add a button for testing the fold states
        self.AddButton(6000, c4d.BFH_CENTER, name="Get Fold States")

        return True

    def Command(self, id, msg):
        # Button to check fold states
        if id == 6000:
            categories_folded = self.GetFolding(1000)
            assets_folded = self.GetFolding(2000)
            search_folded = self.GetFolding(5000)

            msg = (
                f"Categories Folded: {'Yes' if categories_folded else 'No'}\n"
                f"Assets Folded: {'Yes' if assets_folded else 'No'}\n"
                f"Search Folded: {'Yes' if search_folded else 'No'}"
            )
            gui.MessageDialog(msg)

        #return True


# Main function
def main():
    # Create and display the custom dialog
    dlg = CustomDialog()
    dlg.Open(c4d.DLG_TYPE_ASYNC, defaultw=300, defaulth=400)

if __name__ == '__main__':
    main()
