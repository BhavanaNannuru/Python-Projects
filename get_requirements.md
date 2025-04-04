# How to Generate and Use requirements.txt for Python Scripts

## Step 1: Install pipreqs
pip install pipreqs

## Step 2: Navigate to the Project Folder
cd path_to_folder

## Step 3: Generate requirements.txt
pipreqs .

# This will create a `requirements.txt` file based on the actual imports used in your scripts.

------------------------------------------------------------

## How to Use This File Later

To install the dependencies listed in `requirements.txt`, run:

pip install -r requirements.txt

------------------------------------------------------------

## Limitations of pipreqs

- pipreqs works on **directories only**, not on individual `.py` files.

### Workaround:

1. Create a temporary folder.
2. Place your `.py` file inside that folder.
3. Run:

pipreqs path_to_temp_folder
