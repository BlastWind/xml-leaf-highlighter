# User inputs file name (without prefix)

# Finds xml file from root

# Parse the xml file and find leaves. It's easy with a library, I can do better with some home grown parsing

# Get bounds from leaves

# Load image, draw yellow border around bounds, output new image

from functools import reduce
from itertools import chain
from nis import match
import re
from typing import List, Tuple


testXML = '''<hierarchy rotation="0">
<node index="0" text="" resource-id="" class="android.widget.FrameLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,0][1440,2368]">
<node index="0" text="" resource-id="" class="android.widget.LinearLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,0][1440,2368]">
<node index="0" text="" resource-id="" class="android.widget.FrameLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,96][1440,2368]">
<node index="0" text="" resource-id="com.dropbox.android:id/action_bar_root" class="android.widget.FrameLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,96][1440,2368]">
<node index="0" text="" resource-id="android:id/content" class="android.widget.FrameLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,96][1440,2368]">
<node index="0" text="" resource-id="" class="android.view.ViewGroup" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,96][1440,2368]">
<node index="0" text="" resource-id="com.dropbox.android:id/dbx_toolbar_layout" class="android.widget.LinearLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,96][1440,2368]">
<node index="0" text="" resource-id="com.dropbox.android:id/dbx_toolbar" class="android.view.ViewGroup" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,96][1440,320]">
<node index="0" text="" resource-id="" class="android.widget.ImageButton" package="com.dropbox.android" content-desc="Navigate up" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,96][224,320]"/>
<node index="1" text="Dropbox settings" resource-id="" class="android.widget.TextView" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[288,96][1440,320]"/>
</node>
<node index="1" text="" resource-id="com.dropbox.android:id/frag_container" class="android.widget.FrameLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,320][1440,2368]">
<node index="0" text="" resource-id="" class="android.widget.LinearLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,320][1440,2368]">
<node index="0" text="" resource-id="android:id/list_container" class="android.widget.FrameLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,320][1440,2368]">
<node index="0" text="" resource-id="com.dropbox.android:id/list" class="android.support.v7.widget.RecyclerView" package="com.dropbox.android" content-desc="preferences_fragment_list" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" scrollable="true" long-clickable="false" password="false" selected="false" bounds="[0,320][1440,2368]">
<node index="0" text="Dropbox account" resource-id="" class="android.widget.TextView" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,320][1440,460]"/>
<node index="1" text="" resource-id="" class="android.widget.LinearLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,524][1440,738]">
<node index="0" text="" resource-id="" class="android.widget.RelativeLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[64,524][1168,738]">
<node index="0" text="Account photo" resource-id="android:id/title" class="android.widget.TextView" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[64,588][483,674]"/>
</node>
<node index="1" text="" resource-id="android:id/widget_frame" class="android.widget.LinearLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[1168,524][1376,738]">
<node index="0" text="" resource-id="com.dropbox.android:id/preference_widget_avatar" class="android.widget.FrameLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[1232,559][1376,703]">
<node index="0" text="" resource-id="" class="android.widget.ImageView" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[1232,559][1376,703]"/>
</node>
</node>
</node>
<node index="2" text="" resource-id="" class="android.widget.LinearLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="true" enabled="false" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,742][1440,1032]">
<node index="0" text="" resource-id="" class="android.widget.RelativeLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="false" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[64,742][1376,1032]">
<node index="0" text="Email" resource-id="android:id/title" class="android.widget.TextView" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="false" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[64,806][223,892]"/>
<node index="1" text="kpmoran21@gmail.com" resource-id="android:id/summary" class="android.widget.TextView" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="false" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[64,892][658,968]"/>
</node>
</node>
<node index="3" text="" resource-id="" class="android.widget.LinearLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="true" enabled="false" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,1036][1440,1402]">
<node index="0" text="" resource-id="" class="android.widget.RelativeLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="false" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[64,1036][1376,1402]">
<node index="0" text="Space used" resource-id="android:id/title" class="android.widget.TextView" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="false" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[64,1100][395,1186]"/>
<node index="1" text="Dropbox plan: Pro 6.2% of 1.0 TB" resource-id="android:id/summary" class="android.widget.TextView" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="false" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[64,1186][518,1338]"/>
</node>
</node>
<node index="4" text="" resource-id="" class="android.widget.LinearLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,1406][1440,1620]">
<node index="0" text="" resource-id="" class="android.widget.RelativeLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[64,1406][1376,1620]">
<node index="0" text="Connect a computer" resource-id="android:id/title" class="android.widget.TextView" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[64,1470][644,1556]"/>
</node>
</node>
<node index="5" text="" resource-id="" class="android.widget.LinearLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,1624][1440,1838]">
<node index="0" text="" resource-id="" class="android.widget.RelativeLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[64,1624][1376,1838]">
<node index="0" text="Sign out of Dropbox" resource-id="android:id/title" class="android.widget.TextView" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[64,1688][629,1774]"/>
</node>
</node>
<node index="6" text="Get space" resource-id="" class="android.widget.TextView" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,1842][1440,1982]"/>
<node index="7" text="" resource-id="" class="android.widget.LinearLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,2046][1440,2260]">
<node index="0" text="" resource-id="" class="android.widget.RelativeLayout" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[64,2046][1376,2260]">
<node index="0" text="Invite friends" resource-id="android:id/title" class="android.widget.TextView" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[64,2110][432,2196]"/>
</node>
</node>
<node index="8" text="Camera uploads" resource-id="" class="android.widget.TextView" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,2264][1440,2368]"/>
</node>
</node>
</node>
</node>
</node>
</node>
</node>
</node>
</node>
</node>
<node index="1" text="" resource-id="android:id/statusBarBackground" class="android.view.View" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,0][1440,96]"/>
<node index="2" text="" resource-id="android:id/navigationBarBackground" class="android.view.View" package="com.dropbox.android" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,0][0,0]"/>
</node><a></a>
</hierarchy>'''


# No, that's not enough, I need to stronger, look ahead lexer


def extractXMLLeaves(xmlString: str) -> List[str]:
    # matches <...>...</...> with no '<' in the ...s
    uncollapsedLeafRegex = r'<[^(<|/)]+>[^<]*</[^<]+>'
    # matches <.../> with no '<' in the ...
    collapsedLeafRegex = r'<[^<]*/>'
    return list(chain.from_iterable(map(lambda p: re.findall(p, xmlString), [uncollapsedLeafRegex, collapsedLeafRegex])))


a = "<a><b>asdf</b><c>asd</c><d df/></a>"
print(extractXMLLeaves(a))

# # Find the leaf nodes in an xml string, return them in a list
# def extractXMLLeaves(xmlString: str) -> List[str]:
#     '''
#     If I can find <.../> or <...>...</...> without '<' in the ...s: Leaf located
#     Question: Would a regex solution be possible?
#     Parameters:
#         xmlString: A properly formatted XML string.
#     '''
#     #
#     def getCollapsedLeaf(xmlString: str, start: int) -> Tuple[bool, str]:
#         '''
#         Find collapsed leaf node <.../> starting from i
#         Parameters:
#             start: Index in xmlString to start searching from
#         '''
#         for j in range(start+1, len(xmlString)):
#             cur = xmlString[j] if xmlString[j] != '/' else xmlString[j: j+2]
#             if cur == '<':
#                 break
#             if cur == '/>':
#                 return (True, xmlString[start: j+2])
#         return (False, '')

#     # Though uiautomator seems to always collapse leaf, I can't be sure of it and thus wrote this function
#     def getUncollaspedLeaf(xmlString: str, start: int) -> Tuple[bool, str]:
#         matches = ['/>', '</', '>']
#         matchInd = 0
#         for j in range(start+1, len(xmlString)):
#             nextMatch = matches[matchInd]
#             # cur is either current letter, or '<' plus the letter immediately after
#             # this immediately after trick is the lookahead technique used often in interpreters
#             cur = xmlString[j] if xmlString[j] != '<' else xmlString[j: j+2]
#             if cur == '<':
#                 # if match start symbol, xml node starting at "i" must correspond to a parent node: ABORT!
#                 break
#             if cur != nextMatch:
#                 continue
#             # matched
#             if matchInd == len(matches) - 1:
#                 return (True, xmlString[start: j + 1])
#             matchInd += 1
#         return (False, '')

#     startIndices = [i for i in range(
#         len(xmlString)) if xmlString[i] == '<' and xmlString[i: i+2] != '</']
#     leaves = []
#     for i in startIndices:
#         ok, result = getCollapsedLeaf(xmlString, i)
#         if not ok:
#             ok, result = getUncollaspedLeaf(xmlString, i)
#         if ok:
#             leaves.append(result)

#     return leaves


# for leaf in extractXMLLeaves(testXML):
#     print(leaf)
#     print('\n')
