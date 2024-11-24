## Running Locally 💻
Follow these steps to set up and run the service locally :

Create a virtual environment :
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

Install the required dependencies in the virtual environment :
```bash
pip install -r requirements.txt
```

Launch the chat service locally :
```bash
streamlit run drawio_editor.py
```

# c4-draw.io

This file is in [.png (with embedded XML)](https://www.diagrams.net/blog/xml-in-png) format and can be edited directly in draw.io

It will not require a draw.io plugin popup as it is not a plugin - making it easier for others to edit the diagram.

![draw.io-plugin-popup](/drawio_plugin_popup.png)

## Quick Start

Click the link below to load the file in [draw.io Online](https://www.draw.io/#Uhttps://github.com/kaminzo/c4-draw.io/raw/master/c4.drawio.png):

Classic: <https://www.draw.io/#Uhttps://raw.githubusercontent.com/ly2xxx/drawio/main/c4.drawio.png>

With Icons: <https://www.draw.io/#Uhttps://raw.githubusercontent.com/ly2xxx/drawio/main/c4-icons.drawio.png>

## Icons

An easy way to find the icons image URL for the container shape is to search Google Images for your "technology name " + "logo SVG".

## Loading the shapes library from XML

The `c4.drawio.library.xml` is a library definition that can be imported into an existing draw.io diagram and provides the C4 model shapes as a library.

To import the shapes library, download the XML. Then, in draw.io, go to *File* -> *Open library from* -> *Device* and select the XML file from your device.

## Editing

Simply copy and paste shapes.

Select a shape and press Cmd + M (on Mac) to edit shape data.

If you like, save the file as .png (with embedded XML) for ease of viewing.

## Diagram

### Classic

[![c4-draw.io](/c4.drawio.png)](https://www.draw.io/#Uhttps://raw.githubusercontent.com/kaminzo/c4-draw.io/master/c4.drawio.png)

### With Icons

[![c4-icons--draw.io](/c4-icons.drawio.png)](https://www.draw.io/#Uhttps://raw.githubusercontent.com/kaminzo/c4-draw.io/master/c4-icons.drawio.png)

## Credits

C4Model Author: Simon Brown - <https://c4model.com/> [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/)


Inspired by: https://github.com/kaminzo/c4-draw.io 
