import c4d

def main():
    # Get the active object
    active_obj = doc.GetActiveObject()
    if active_obj is None:
        c4d.gui.MessageDialog("No active object found.")
        return

    # Get the selected polygons
    selected_polys = active_obj.GetPolygonS()
    if selected_polys is None:
        c4d.gui.MessageDialog("No selected polygons found.")
        return

    # Store the original active object
    original_active_obj = active_obj

    # Split the polygons
    poly_count = active_obj.GetPolygonCount()
    c4d.gui.MessageDialog(poly_count)
    for i in range(poly_count):
        # Select one polygon at a time
        selected_polys.DeselectAll()
        selected_polys.Select(i)

        # Split the polygon
        result = c4d.CallCommand(14046)  # Splits

        # Restore the original active object
        doc.SetActiveObject(original_active_obj)

        # if not result:
        #     c4d.gui.MessageDialog("Split command failed for polygon at index: " + str(i))

    # Update the selection tag
    active_obj.Message(c4d.MSG_UPDATE)

    # Update the Cinema 4D scene
    c4d.EventAdd()
    if selected_polys.GetCount() > 0:
        c4d.gui.MessageDialog("Polygon splitting successful.")
    else:
        c4d.gui.MessageDialog("No polygons were split.")

# Execute the main() function
if __name__ == '__main__':
    main()
