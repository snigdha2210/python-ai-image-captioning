# README: Image Captioning with BLIP

## Overview

This project is a simple application that uses the **BLIP (Bootstrapped Language-Image Pretraining)** model to generate captions for uploaded images. The application leverages the Gradio library to provide an easy-to-use web interface for interacting with the image captioning system.

## Features

- **Image Upload:** Users can upload an image to the application.
- **Caption Generation:** Automatically generates a descriptive caption for the uploaded image using the BLIP model.
- **User-Friendly Interface:** The web interface is built with Gradio, making it intuitive and accessible.

## Screenshot

![Web Interface](images/readme.png)

## Prerequisites

Before running the script, ensure you have the following installed:

1. **Python** (version 3.7 or higher)
2. Required Python libraries:
   - `transformers`
   - `gradio`
   - `Pillow` (for handling images)

You can install these dependencies using pip:

```bash
pip install transformers gradio Pillow
```

## How It Works

1. The script uses the **BLIP model** for image captioning. It loads the `Salesforce/blip-image-captioning-base` model and processor from the Hugging Face Transformers library.
2. Users upload an image via the Gradio interface.
3. The script processes the image using the BLIP model to generate a caption.
4. The generated caption is displayed as output on the Gradio interface.

## File Structure

- **Script:** The main script (`gradio-imageCaptioning.py`) contains the logic for loading the model, processing images, and launching the Gradio interface.
- **Screenshot:** (Optional) Screenshot of the interface for documentation purposes.

## How to Run

1. Save the script as `gradio-imageCaptioning.py`.
2. Run the script in your terminal:

   ```bash
   python gradio-imageCaptioning.py
   ```

3. A local server will start, and a link will be displayed (e.g., `http://127.0.0.1:7860`). Open the link in your browser.
4. Upload an image and view the generated caption.

## Example Usage

1. **Upload an Image:** Drag and drop an image or use the upload button in the interface.
2. **View the Caption:** The application will process the image and display a descriptive caption.

## Learning Experience

This project was an excellent opportunity to learn how to use **Gradio** for creating web interfaces and explore **BLIP** for image captioning. By combining these tools, I was able to build an interactive application that bridges AI and user-friendly interfaces.

## Future Improvements

- Allow users to save captions to a file.
- Enhance the model for more diverse and accurate captioning.
- Add support for batch image processing.

---

Feel free to explore the application and provide feedback! 😊
