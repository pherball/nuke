############
#CTRL == ^
#SHIFT == +
#ALT == #


# FRAMEHOLD
def frameHold():
    if nuke.selectedNodes():
            for n in nuke.selectedNodes():
                try:
                    n['first_frame'].setValue(nuke.frame())
                except NameError:
                    pass
    else:
        nuke.createNode("FrameHold")

# DISABLE GUI NODES
def DisableGui():
    for n in nuke.allNodes(): 
        try: 
            k = n['disable']
            if k.hasExpression():
                k.clearAnimated()
                k.setValue(False)
        except:
            pass

# GUI TOGGLE
def guiToggle():
    for n in nuke.selectedNodes(): 
        try: 
            k = n['disable']
            if not k.hasExpression():
                n['disable'].setExpression("$gui")
            else: 
                k.clearAnimated()
                k.setValue(False)
        except:
            pass
# SET BBOX TO B
def bboxB():
    for a in nuke.selectedNodes():
        classTypes = ['Merge' , 'Keymix', 'Copy', ]
        for n in classTypes:
            if n in a.Class():
                for p in a['bbox'].values():
                    if 'B' in p:
                        a['bbox'].setValue(a['bbox'].values().index(p))
                        
# OPEN PROPERTIES
def openProp():
    for n in nuke.selectedNodes():
        nuke.show(n)
# CLOSE PROPERTIES
def closeProp():
    for n in nuke.allNodes() + [nuke.root(), ]: 
        n.hideControlPanel()

m = nuke.menu('Nuke')
n = nuke.menu('Nodes')
s = nuke.menu('Nuke').addMenu('CMI')

# RELOAD SELECTED
def reloadSelected():
    for n in nuke.selectedNodes():
        if n.Class() in ('Read', 'Group'):
            try:
                n.knob("reload").execute()
            except:
                pass

# DEFAULT HOTKEY CHANGE
def snapAll():
    n = nuke.allNodes();
    for i in n:
      nuke.autoplaceSnap(i)
def snapSel():
    n = nuke.selectedNodes()
    for i in n:
      nuke.autoplaceSnap(i)

    
# BACKWARD INCREMENT
m.addCommand('CMI/Hotkey/BACK3', 'nuke.activeViewer().frameControl(-2)',"#Q")
# FORWARD INCREMENT
m.addCommand('CMI/Hotkey/FORWARD3', 'nuke.activeViewer().frameControl(2)',"#W")
# BACKWARD 1 FRAME
m.addCommand('CMI/Hotkey/BACK1', 'nuke.activeViewer().frameControl(-1)',"F1")
# FORWARD 1 frame
m.addCommand('CMI/Hotkey/FORWARD1', 'nuke.activeViewer().frameControl(1)',"F2")
# BACKWARD 1 KEY
m.addCommand('CMI/Hotkey/KEY-', 'nuke.activeViewer().frameControl(-4)',"#+Q")
# FORWARD 1 KEY
m.addCommand('CMI/Hotkey/KEY+', 'nuke.activeViewer().frameControl(4)',"#+W")


m.addCommand('CMI/Util/Framehold', 'frameHold()' ,'+F')
m.addCommand('CMI/Util/Set bbox to B', 'bboxB()', '^B')
m.addCommand('CMI/Hotkey/Snap Sel', 'snapSel()',"+`")
m.addCommand('CMI/Hotkey/Open Properties', 'openProp()',"`")
m.addCommand('CMI/Hotkey/Close Properties', 'closeProp()',"^`")
m.addCommand('CMI/Util/Reload Selected', 'reloadSelected()', '+R')
m.addCommand('CMI/Hotkey/Tracker', "nuke.createNode('Tracker4')","^+T")
m.addCommand('CMI/Hotkey/Transform Masked', "nuke.createNode('TransformMasked')",'+T')
m.addCommand('CMI/Hotkey/KeyMix', "nuke.createNode('Keymix')",'+A')
m.addCommand('CMI/Hotkey/Keyer', "nuke.nodePaste(os.path.expanduser('~/.nuke/keyer.nk'))", '^+K')
m.addCommand('CMI/Hotkey/WeightedBlur', "nuke.nodePaste(os.path.expanduser('~/.nuke/weightedBlur.nk'))", '^#W')
m.addCommand('CMI/Hotkey/Clear Caches', 'nukescripts.clearAllCaches()', 'Alt+`')
m.addCommand("CMI/Hotkey/Stencil", "nuke.createNode('Merge', 'operation stencil bbox B label {bbox|[value bbox]}')", '^M')
m.addCommand("CMI/Hotkey/Mask", "nuke.createNode('Merge2', 'operation mask bbox intersection label {bbox|[value bbox]}')", '+M')
m.addCommand('CMI/Hotkey/Clear Caches', 'nukescripts.clearAllCaches()', 'F4`')
m.addCommand('CMI/Hotkey/Version Up', 'nukescripts.version_up()', "Ctrl+Up")
m.addCommand('CMI/Hotkey/Version Down', 'nukescripts.version_down()', "Ctrl+Down")
m.addCommand('CMI/Disable $GUI', 'DisableGui()')
m.addCommand('CMI/Util/$gui Toggle', 'guiToggle()', '+D')

m.addCommand('CMI/Hotkey/CC', 'nuke.loadToolset("/u/chmi/.nuke/ToolSets/CC.nk")', "Shift+C")


#import W_smartAlign

#menuBar = nuke.menu("Nuke")
#menuBar.addCommand("Edit/Node/Align/Left", 'W_smartAlign.alignNodes("left")', "Alt+left", shortcutContext=2)
#menuBar.addCommand("Edit/Node/Align/Right", 'W_smartAlign.alignNodes("right")', "Alt+right", shortcutContext=2)
#menuBar.addCommand("Edit/Node/Align/Up", 'W_smartAlign.alignNodes("up")', "Alt+up", shortcutContext=2)
#menuBar.addCommand("Edit/Node/Align/Down", 'W_smartAlign.alignNodes("down")', "Alt+down", shortcutContext=2)

#import link_tools

#m.addCommand('CMI/Util/Link Roto', 'link_tools.link("roto")', "#O")

#import BrushReduction
#import comma

#import autoContactSheet.py

#import rv_this

#m.addCommand('CMI/Util/Open in RV', 'rv_this.rv_this()', "^R")




