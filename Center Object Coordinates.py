import c4d

def main():
    # Get the active document
    doc = c4d.documents.GetActiveDocument()

    if doc is None:
        return

    # Get the selected objects
    selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)
    
    if selected_objects:
        for index, obj in enumerate(selected_objects):
            obj.SetAbsPos(c4d.Vector(0, 0, 0))


            # Update the Cinema 4D scene
            c4d.EventAdd()
    else:
        c4d.gui.MessageDialog("No objects selected.")



    # Get the selected object

    # Set the object's position to (0, 0, 0)
    selected_object.SetAbsPos(c4d.Vector(0, 0, 0))

    # Update the scene
    c4d.EventAdd()

# Execute main()
if __name__=='__main__':
    main()

