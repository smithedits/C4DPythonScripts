import c4d
import c4d.gui

def get_render_output_path():
    """Fetches the render output folder path from Cinema 4D and shows it in a dialog."""
    doc = c4d.documents.GetActiveDocument()
    render_data = doc.GetActiveRenderData()
    output_path = render_data[c4d.RDATA_PATH]  # Get the output path

    if not output_path:
        c4d.gui.MessageDialog("No render output path set.")
        return None

    c4d.gui.MessageDialog(f"Render Output Path:\n{output_path}")
    return output_path

def get_frame_step():
    """Fetches the Frame Step value from Cinema 4D's render settings and displays it."""
    doc = c4d.documents.GetActiveDocument()
    render_data = doc.GetActiveRenderData()
    frame_step = render_data[c4d.RDATA_FRAMESTEP]  # Get the Frame Step value

    message = f"Frame Step: {frame_step}"
    c4d.gui.MessageDialog(message)  # Show it in a dialog box
    return frame_step

def get_total_frames():
    """Calculates and displays the total number of frames to be rendered."""
    doc = c4d.documents.GetActiveDocument()
    render_data = doc.GetActiveRenderData()
    
    # Fetch frame settings
    from_frame = render_data[c4d.RDATA_FRAMEFROM].GetFrame(doc.GetFps())  # Convert to int
    to_frame = render_data[c4d.RDATA_FRAMETO].GetFrame(doc.GetFps())      # Convert to int
    frame_step = render_data[c4d.RDATA_FRAMESTEP]                          # Frame Step

    # Debugging output to verify frames
    debug_message = (
        f"From Frame: {from_frame}\n"
        f"To Frame: {to_frame}\n"
        f"Frame Step: {frame_step}"
    )
    c4d.gui.MessageDialog(debug_message)  # Show debug values

    # Validate frame_step
    if frame_step <= 0:
        c4d.gui.MessageDialog("Frame Step must be greater than 0.")
        return 0

    # Validate frame range
    if from_frame > to_frame:
        c4d.gui.MessageDialog("Invalid frame range: 'From Frame' is greater than 'To Frame'.")
        return 0

    # Calculate total frames
    total_frames = ((to_frame - from_frame) // frame_step) + 1  # +1 to include the end frame
    
    # If our calculation results in less than or equal to zero, return a warning
    if total_frames <= 0:
        c4d.gui.MessageDialog("No frames to render with the current settings.")
        return 0

    message = f"Total Frames to Render: {total_frames}"
    c4d.gui.MessageDialog(message)  # Show it in a dialog box
    return total_frames

# Run the functions
if __name__ == "__main__":
    get_render_output_path()
    get_frame_step()
    get_total_frames()