# Piskel to String Converter

This tool converts `.piskel` files into a string-based representation.

## Usage

Use the **config** section to:

- Specify the path to your `.piskel` file.
- Define `piskelMap`, which maps hex color values to single-character codes.

## Installation & Running

The commands below assume Windows (PowerShell, VSCode Terminal, Command Prompt, etc.).  
On macOS/Linux, you may need to use `python3` and `source venv/bin/activate` instead.

```sh
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
python piskelConvert.py
```

## Requirements

- The `.piskel` image **width and height must both be multiples of 11**.  
  Any other dimensions will result in an error.
- `piskelMap` **must include every color present in the `.piskel` file**.  
  Missing mappings will cause an error.

## Disclaimer

By using this tool, you acknowledge that:

- You may encounter bugs or unexpected behavior.
- You are solely responsible for verifying and fixing any issues you encounter.
- This tool **must not** be used as justification in any grading or assessment disputes.

Use it at your own risk.