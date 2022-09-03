
from itertools import chain
import os
import re
import sys
from typing import List, Tuple
from PIL import ImageDraw, ImageColor, Image


def extractXMLLeaves(xmlString: str) -> List[str]:
    # matches <...>...</...> with no '<' in the ...s
    uncollapsedLeafRegex = r'<[^(<|/)]+>[^<]*</[^<]+>'
    # matches <.../> with no '<' in the ...
    collapsedLeafRegex = r'<[^<]*/>'
    return list(chain.from_iterable(map(lambda p: re.findall(p, xmlString), [uncollapsedLeafRegex, collapsedLeafRegex])))


# Caveat: Returns empty string if attr not found
def getXMLNodeAttributeValue(xmlNode: str, attr: str) -> str:
    res = re.search(rf'{attr}="(.*)"', xmlNode)
    return res.group(1) if res else ""


def drawDashedRect(draw, leftUpperCoord: Tuple[int, int], rightBottomCoord: Tuple[int, int], color, width, dashFreq=0.5):
    (x1, y1), (x2, y2) = leftUpperCoord, rightBottomCoord
    for x in range(x1, x2, int(width // dashFreq)):
        draw.line(((x, y1), (x+width, y1)),
                  color, width)
        draw.line(((x, y2), (x+width, y2)),
                  color, width)
    for y in range(y1, y2, int(width // dashFreq)):
        draw.line(((x1, y), (x1, y+width)),
                  color, width)
        draw.line(((x2, y), (x2, y+width)),
                  color, width)
def main():
    if len(sys.argv) <= 1:
        sys.exit("Usage: python3 main.py [file_path1] [file_path2] ...")
    filePaths = sys.argv[1:]
    os.makedirs(f"annotated/", exist_ok=True)
    for filePath in filePaths:
        # Finds xml file from root
        with Image.open(f"{filePath}.png") as im:
            draw = ImageDraw.Draw(im)
            with open(f"{filePath}.xml") as f:
                # Parse the xml file and find leaves. It's simpler with a XML-aware library, but I will be environmentally friendly and be home grown here.
                xml = f.read()
                leaves = extractXMLLeaves(xml)
                for l in leaves:
                    bounds = getXMLNodeAttributeValue(l, "bounds")
                    if bounds:
                        # bounds examples: "[0,96][224,320]" Note that 0 to 224 is the width, 96 to 320 is the height
                        ((x1, y1), (x2, y2)) = re.findall(
                            r'\[([0-9]*),([0-9]*)[0-9]*]', bounds)
                        x1, x2, y1, y2 = int(x1), int(
                            x2), int(y1), int(y2)
                        # draw rectangular bound onto image
                        drawDashedRect(draw, (x1, y1), (x2, y2),
                                       ImageColor.getrgb("yellow"), 5)
            im.save(f"annotated/{os.path.basename(filePath)}.png")
            
if __name__ == "__main__":
    main()
