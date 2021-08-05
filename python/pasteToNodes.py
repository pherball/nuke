import nuke
def pasteToNodes():
    for n in nuke.selectedNodes():
        for x in nuke.selectedNodes():
            x.setSelected(False)
        n.setSelected(True)
        nuke.nodePaste("%clipboard%")



import pasteToNodes
n.addCommand( "paste to nodes", 'pasteToNodes.pasteToNodes()', 'ctrl+shift+v',icon='ShuffleCopy.png')
