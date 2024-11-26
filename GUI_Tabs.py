import c4d
from c4d import gui

class TabbedDialog(gui.GeDialog):
    TAB_GROUP_ID = 1000  # ID for the tab group
    TAB_1_ID = 1001      # ID for Tab 1
    TAB_2_ID = 1002      # ID for Tab 2
    CONTENT_GROUP_ID = 2000  # ID for the content area

    def CreateLayout(self):
        # Add tabs at the top
        self.TabGroupBegin(self.TAB_GROUP_ID, c4d.BFH_SCALEFIT | c4d.BFV_TOP)
        self.GroupBegin(self.TAB_1_ID, c4d.BFH_SCALEFIT | c4d.BFV_TOP, 1, 1, "Tab 1")
        self.GroupEnd()
        self.GroupBegin(self.TAB_2_ID, c4d.BFH_SCALEFIT | c4d.BFV_TOP, 1, 1, "Tab 2")
        self.GroupEnd()
        self.GroupEnd()

        # Content area for the tabs
        self.GroupBegin(self.CONTENT_GROUP_ID, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1, 0)
        self.GroupBorderSpace(10, 10, 10, 10)

        # Default content for Tab 1
        self.AddStaticText(3001, c4d.BFH_CENTER, name="Content for Tab 1")
        self.GroupEnd()



    def Command(self, id, msg):
        # Check if a tab was clicked
        if id == self.TAB_GROUP_ID:
            # Remove the current content
            self.LayoutFlushGroup(self.CONTENT_GROUP_ID)

            # Check which tab is active
            active_tab = self.GetInt32(self.TAB_GROUP_ID)
            if active_tab == self.TAB_1_ID:
                # Add content for Tab 1
                self.AddStaticText(3002, c4d.BFH_CENTER, name="Content for Tab 1")
            elif active_tab == self.TAB_2_ID:
                # Add content for Tab 2
                self.AddStaticText(3003, c4d.BFH_CENTER, name="Content for Tab 2")

            # Refresh the layout to display the new content
            self.LayoutChanged(self.CONTENT_GROUP_ID)

        #return True

# Main function
def main():
    dlg = TabbedDialog()
    dlg.Open(c4d.DLG_TYPE_ASYNC, defaultw=400, defaulth=300)

if __name__ == "__main__":
    main()
