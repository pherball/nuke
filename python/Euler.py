"""
euler flip script, version 3, SDV


Description:
Fixes 3D Euler rotation flipping for animated cameras and axis nodes
in Nuke.

Euler rotation flipping occurs when rotation values exceed 360 degrees
in one frame.


Version 3 [2020-07-30] - David Cattermole:
    - Add usage docs.
    - Convert to a Python function for Nuke GUI.
    - Filter the X axis as well.
    - Script operates on multiple selected nodes at once.

Version 2 [2020-06-24]:
    - filter y- and z-curve of knob "rotate" in selected node

Version 1 [2020-06-23]:
    - filter y-curve of knob "rotate" in selected node


Installation:
To install this script, copy the file into your Nuke python directory,
for example on Linux, the home directory is here:
/home/<username>/.nuke/

Once the script is copied to your Nuke directory, you may add the following
lines to your "menu.py" file:

# CODE START
import transformRotationCurveEulerFilter
t = nuke.toolBar('Nodes')
toolMenu = t.addMenu('Custom menu name')
toolMenu.addCommand('Transform Rotation Curve Euler Filter', 'transformRotationCurveEulerFilter.main()')
# CODE END

These lines will add a new node button and node entry to the node bar
(left bar in the Nuke UI by default).

Alternatively, if you prefer not to add a new node button, open the Nuke
script editor, type the following and press CTRL + ENTER:

# CODE START
import transformRotationCurveEulerFilter
transformRotationCurveEulerFilter.main()
# CODE END

For more advanced installation, see the Nuke Python documentation:
https://learn.foundry.com/nuke/developers/latest/pythondevguide/installing_plugins.html


Usage:

1) Select Camera or Axis nodes.

2) Run the tool (with the Node menu bar, or manually with the Nuke
   script editor - see Installation above)

3) Done.
"""

import nuke
import math


def main():
    nodes = nuke.selectedNodes()
    if len(nodes) == 0:
        msg = "Please select nodes with 3D rotation keyframes."
        nuke.message(msg)
        return
    for node in nodes:
        euler_filter_node(node)
    return


def euler_filter_value(current_value, previous_value):
    if current_value - previous_value < -180:
        current_value += 360
    elif current_value - previous_value > +180:
        current_value -= 360
    else:
        pass
    return current_value


def euler_filter_node(node):
    # Get rotation knob of currently selected node
    knob_rotate = node.knob("rotate")
    if not knob_rotate:
        msg = "Please select a node with a 'rotate' knob."
        nuke.message(msg)
        return

    # Get boundaries of that knob
    key_list = knob_rotate.getKeyList()
    if len(key_list) == 0:
        msg = "Please select a node with 3D rotation keyframes."
        nuke.message(msg)
        return

    # We consider Euler-flipping around the y- and z-axis.
    x_prv = knob_rotate.getValueAt(key_list[0], 0)
    y_prv = knob_rotate.getValueAt(key_list[0], 1)
    z_prv = knob_rotate.getValueAt(key_list[0], 2)

    # In case we are supposed to respond correctly to rotation order,
    # we'll have to check this knob here:
    # knob_rot_order = node.knob("rot_order")
    # Default value for nuke and the movie industry is "ZXY".
    for i in key_list:
        x_cur = knob_rotate.getValueAt(i, 0)
        y_cur = knob_rotate.getValueAt(i, 1)
        z_cur = knob_rotate.getValueAt(i, 2)

    # Now compare the current value to the previous one
    # and check for discontinuities. All values are in degree.

    # x (tilt)
        x_cur = euler_filter_value(x_cur, x_prv)
    # y (pan)
        y_cur = euler_filter_value(y_cur, y_prv)
    # z (roll)
        z_cur = euler_filter_value(z_cur, z_prv)

    # Remember current values in the next pass
        x_prv = x_cur
        y_prv = y_cur
        z_prv = z_cur
    # Set corrected value.
        knob_rotate.setValueAt(x_cur, i, 0)
        knob_rotate.setValueAt(y_cur, i, 1)
        knob_rotate.setValueAt(z_cur, i, 2)
    return
