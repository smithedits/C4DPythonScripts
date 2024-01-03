import c4d

def main():
    # Create a new null object
    null = c4d.BaseObject(c4d.Onull)
    null.SetName("Focus")
    if null is None:
        return

    # Set the null object's position
    null[c4d.ID_BASEOBJECT_POSITION] = c4d.Vector(0, 0, 200)

    # Insert the null object into the scene
    doc = c4d.documents.GetActiveDocument()
    doc.InsertObject(null)
    doc.SetActiveObject(null)

    # Create a new camera object
    camera = c4d.BaseObject(c4d.Ocamera)
    if camera is None:
        return

    # Insert the camera into the scene
    doc.InsertObject(camera)
    doc.SetActiveObject(camera)

    # Add a target tag to the camera
    target_tag = c4d.BaseTag(c4d.Ttargetexpression)
    if target_tag is None:
        return

    Viberate_tag = c4d.BaseTag(c4d.Tvibrate)
    Viberate_tag[c4d.VIBRATEEXPRESSION_POS_ENABLE] = 1

    camera.InsertTag(target_tag)
    camera.InsertTag(Viberate_tag)

    # Set the target object of the target tag to the null object
    target_tag[c4d.TARGETEXPRESSIONTAG_LINK] = null

    # Update the scene
    c4d.EventAdd()

if __name__=='__main__':
    main()