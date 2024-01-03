import c4d



def main():

    # Get the active Cinema 4D document

    doc = c4d.documents.GetActiveDocument()

    

    # Get the currently selected object

    obj = doc.GetActiveObject()

    

    if obj is not None:

        # Get the bounding box of the object

        bbox = obj.GetRad()
        
        c4d.gui.MessageDialog(bbox)



        # Display the bounding box values using a message dialog

        msg = "Bounding Box Values:\n\n"

        msg += "Minimum: {}\n".format(bbox.x)

        msg += "Maximum: {}\n".format(bbox.y)

        msg += "Center: {}\n".format(bbox.z)

        msg += "Size: {}\n".format(bbox.y + bbox.x + bbox.z)

        

        c4d.gui.MessageDialog(msg)

    else:

        # If no object is selected, display an error message

        c4d.gui.MessageDialog("No object selected.")



# Execute the main() function

if __name__=='__main__':

    main()

