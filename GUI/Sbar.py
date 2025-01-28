import c4d
from c4d import gui
import os
import importlib.util
import sys

class ScriptToolbar(gui.GeDialog):
    def __init__(self, scripts_folder):
        super().__init__()
        self.scripts_folder = scripts_folder  # Path to the folder containing scripts
        self.scripts = []  # List to store (script_name, script_path, image_path) tuples
        print(f"Toolbar initialized for folder: {self.scripts_folder}")

    def CreateLayout(self):
        """Creates the layout of the toolbar with buttons for each script."""
        print("Creating toolbar layout...")
        self.SetTitle("Sbar")

        # Check if the folder exists
        if not os.path.isdir(self.scripts_folder):
            print(f"Error: Folder not found - {self.scripts_folder}")
            return False

        # Load scripts from the folder
        for file_name in os.listdir(self.scripts_folder):
            if file_name.endswith('.py'):  # Only process .py files
                script_path = os.path.join(self.scripts_folder, file_name)
                script_name = os.path.splitext(file_name)[0]  # Remove .py extension
                image_path = os.path.join(self.scripts_folder, f"{script_name}.png")  # Image path for the script

                if os.path.exists(image_path):
                    self.scripts.append((script_name, script_path, image_path))
                else:
                    print(f"Image not found for script: {script_name}")

        if not self.scripts:
            print(f"No scripts found in folder: {self.scripts_folder}")
            return False

        # Create a grid layout for the buttons
        self.GroupBegin(0, c4d.BFH_SCALEFIT, 10, 10, "Button Group")  # 10x10 grid
        for idx, (script_name, script_path, image_path) in enumerate(self.scripts):
            button_id = idx + 1  # Use index + 1 as button ID (ID 0 is reserved)
            self.AddCustomGui(
                button_id,  # Button ID
                c4d.CUSTOMGUI_BITMAPBUTTON,  # Use a bitmap button
                "",  # No label
                c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT,  # Allow scaling
                50,  # Button width
                50,  # Button height
            )
            # Load the image and set it to the button
            bitmap = c4d.bitmaps.BaseBitmap()
            if bitmap.InitWith(image_path)[0] == c4d.IMAGERESULT_OK:
                button = self.FindCustomGui(button_id, c4d.CUSTOMGUI_BITMAPBUTTON)
                if button:
                    button.SetImage(bitmap, True)
                    print(f"Button added for script: {script_name} with image: {image_path}")
                else:
                    print(f"Failed to find button for script: {script_name}")
            else:
                print(f"Failed to load image: {image_path}")
        self.GroupEnd()

        return True

    def Command(self, id, msg):
        """Executes the script when a button is clicked."""
        if id > 0 and id <= len(self.scripts):
            script_name, script_path, image_path = self.scripts[id - 1]
            print(f"Button clicked: {script_name} (ID {id})")
    
            if os.path.exists(script_path):
                try:
                    # Attempt to load the script as a module
                    spec = importlib.util.spec_from_file_location("script_module", script_path)
                    script_module = importlib.util.module_from_spec(spec)
                    sys.modules["script_module"] = script_module
                    spec.loader.exec_module(script_module)
    
                    # Try calling `main()` if it exists
                    if hasattr(script_module, 'main'):
                        script_module.main()
                        print(f"Executed script via module: {script_name}")
                    else:
                        raise AttributeError(f"Script {script_name} has no 'main()' function.")
    
                except Exception as e:
                    print(f"Module execution failed: {e}. Falling back to exec().")
                    try:
                        # Fallback to exec()
                        with open(script_path, 'r') as script_file:
                            exec(script_file.read())
                            print(f"Executed script via exec(): {script_name}")
                    except Exception as e:
                        print(f"Fallback execution failed: {e}")
            else:
                print(f"Script not found: {script_path}")
        return True


def main():
    # Path to the folder containing scripts
    scripts_folder = "/Users/m2film/Documents/ROOT/PDF_MAKER/customscripts/"
    print(f"Scripts folder: {scripts_folder}")

    # Create and open the toolbar
    print("Creating toolbar...")
    toolbar = ScriptToolbar(scripts_folder)
    toolbar.Open(c4d.DLG_TYPE_ASYNC, defaultw=400, defaulth=400)  # Adjust size for grid layout
    print("Toolbar opened.")


if __name__ == "__main__":
    print("Starting script...")
    main()