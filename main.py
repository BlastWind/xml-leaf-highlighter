
from itertools import chain
import re
from typing import List

def extractXMLLeaves(xmlString: str) -> List[str]:
    # matches <...>...</...> with no '<' in the ...s
    uncollapsedLeafRegex = r'<[^(<|/)]+>[^<]*</[^<]+>'
    # matches <.../> with no '<' in the ...
    collapsedLeafRegex = r'<[^<]*/>'
    return list(chain.from_iterable(map(lambda p: re.findall(p, xmlString), [uncollapsedLeafRegex, collapsedLeafRegex])))



if __name__ == "__main__": 
    ### PROCEDUCRE ###
    # User inputs file name (without prefix)
    # Finds xml file from root
    # Parse the xml file and find leaves. It's easy with a library, I can do better with some home grown parsing
    # Get bounds from leaves
    # Load image, draw yellow border around bounds, output new image
    print("hi")
    a = "<a><b>asdf</b><c>asd</c><d df/></a>"
    print(extractXMLLeaves(a))