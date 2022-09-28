# xml-leaf-highlighter
Parse android's `uiautomator` generated XML, draw yellow boxes onto the corresponding image's leaf elements. Sample inputs are in `tests/data` and sample outputs are in [`annotated/`](annotated/). **This is a school project, a little warmup for my software engineering class. So please do not use in production!**

### Usage
Input: Array of paths, each path corresponds to a `xml` file to parse and a `png` file to draw onto. See `tests/data` for example pairs.
Output: Create an `annotated/` directory in the current directory consisting of annotated `png`s.
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
# Clone repo, and make sure you have Pillow
cd xml_leaf_highlighter
python3 main.py [file_path1] [file_path2]
```


`xlh` is just a wrapper around `xml_leaf_highlighter/main.py`.

### Design Decisions
How this project should be realistically approached: 
- Utilize a xml parsing and drawing library
- Profit.
I wanted to practice my codesmanship a bit. So, although I don't have enough time to research and write my own png manipulation library (I tried looking into ), I did write a regex to [parse out the xml leaf nodes](xml_leaf_highlighter/main.py). Note that in the programming community, parsing html/xml with regex in production is a heresy to many, and, borderline satanic to [some](https://stackoverflow.com/a/1732454). I used python because I don't use it enough, it's slowly becoming my favorite language.


### Requirements
python >= 3.8.10 works perfectly 
### Testing
Run python tests with `python3 -m unittest` 
