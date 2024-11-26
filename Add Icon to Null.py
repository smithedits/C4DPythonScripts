import c4d
from c4d import gui
# Welcome to the world of Python


# Script state in the menu or the command palette
# Return True or c4d.CMD_ENABLED to enable, False or 0 to disable
# Alternatively return c4d.CMD_ENABLED|c4d.CMD_VALUE to enable and check/mark
#def state():
#    return True

# Main function
def main():
    nul = c4d.BaseObject(c4d.Onull)
    nul.SetName('New Test Icon')
    doc.InsertObject(nul)

    Custom_Icon = "PATH

    FolderIcon = "1052837"
    CircleIcon = "17106"
    StarIcon = "170141"
    TriangleIcon = "5174"
    HorseControllerIcon = "1022962"
    EyeIcon = "12499"
    ManControllerIcon = "1021433"
    FootIcon = "1022957"
    HandIcon = "1022956"



    nul[c4d.ID_BASELIST_ICON_FILE] = Custom_Icon
    c4d.EventAdd()

# Execute main()
if __name__=='__main__':
    main()
