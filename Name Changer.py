import c4d
from c4d import gui

class MyDialog(gui.GeDialog):
    def CreateLayout(self):
        # Add a fold group with some elements
        self.GroupBegin(1000, c4d.BFH_SCALEFIT, 2, 1, title="My Fold Group")
        self.AddEditText(1001, c4d.BFH_SCALEFIT)
        # Add a button to retrieve folding state
        self.AddButton(1003, c4d.BFH_CENTER, name="rename")
        self.AddCheckbox(1002, c4d.BFH_SCALEFIT, initw=200, name="Option 1")
        self.GroupEnd()



        return True

    def Command(self, id, msg):
        if id == 1003:
            # Get the folding state of the fold group
            response = self.GetString(1001)

            # Get the active document
            doc = c4d.documents.GetActiveDocument()

            # Get the selected objects
            selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)
            if selected_objects:
                for index, obj in enumerate(selected_objects):
                    # Get the current name of the object
                    current_name = obj.GetName()

                    # Change the name of the object (you can modify the new_name variable)
                    new_name = response
                    obj.SetName(f"{new_name}_{index}")


                # Update the Cinema 4D scene
                c4d.EventAdd()
            else:
                c4d.gui.MessageDialog("No objects selected.")

        return True

# Main function
def main():
    # Create an instance of the custom dialog
    dlg = MyDialog()

    # Open the dialog as a dockable window
    dlg.Open(c4d.DLG_TYPE_ASYNC, defaultw=200, defaulth=150)

if __name__=='__main__':
    main()