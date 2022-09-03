# xml-leaf-highlighter
Parse android's `uiautomator` generated XML, draw yellow boxes onto the corresponding image's leaf elements.

### Usage
Input: Array of paths, each path corresponds to a `xml` file to parse and a `png` file to draw onto. See `tests/data` for example pairs.
Output: An `annotated/` directory consisting of annotated `png`s.
```bash
# Clone repo
pip install .
xlh [file_path1] [file_path2] ...
```
#### Example
```bash
# In cloned repo
xlh tests/data/com.apalon.ringtones tests/data/com.dropbox.android tests/data/com.giphy.messenger-2
```

 You could also directly execute the highlighter script:
```bash
# Clone repo
cd xml_leaf_highlighter
python3 main.py [file_path1] [file_path2]
```


`xlh` is just a wrapper around `xml_leaf_highlighter/main.py`.


### Requirements
python >= 3.8.10 works perfectly 
### Testing
Run python tests with `python3 -m unittest` 