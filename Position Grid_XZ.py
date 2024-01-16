import c4d

def arrange_objects_in_grid():
    # Get the active document
    doc = c4d.documents.GetActiveDocument()

    if doc is None:
        return

    # Get the selected objects
    selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)

    if not selected_objects:
        c4d.gui.MessageDialog("No objects selected.")
        return

    # Set the grid parameters
    num_columns = 5  # Adjust the number of columns as needed
    spacing = 500    # Adjust the spacing between objects as needed

    # Arrange objects in a grid on the X and Z axes
    for index, obj in enumerate(selected_objects):
        row = index // num_columns
        col = index % num_columns

        # Calculate the new position based on the grid
        new_pos = c4d.Vector(col * spacing, 0, row * spacing)
        obj.SetAbsPos(new_pos)

    # Update the Cinema 4D scene
    c4d.EventAdd()

if __name__ == '__main__':
    arrange_objects_in_grid()
