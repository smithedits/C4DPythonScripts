import c4d
from c4d import gui

class MyDialog(gui.GeDialog):
    def CreateLayout(self):
        # Add a fold group with some elements
        self.GroupBegin(1000, c4d.BFH_SCALEFIT, 2, 1, title="My Fold Group")
        self.AddEditText(1001, c4d.BFH_SCALEFIT)
        self.AddCheckbox(1002, c4d.BFH_SCALEFIT, initw=200, name="Option 1")
        # Add a button to retrieve folding state
        self.AddButton(1003, c4d.BFH_CENTER, name="Get Folding State")
        self.GroupEnd()



        return True

    def Command(self, id, msg):
        if id == 1003:
            # Get the folding state of the fold group
            folding_state = self.GetFolding(1000)

            if folding_state:
                gui.MessageDialog("Fold group is folded.")
            else:
                gui.MessageDialog("Fold group is unfolded.")

        return True

# Main function
def main():
    # Create an instance of the custom dialog
    dlg = MyDialog()

    # Open the dialog as a dockable window
    dlg.Open(c4d.DLG_TYPE_ASYNC, defaultw=200, defaulth=150)

if __name__=='__main__':
    main()
