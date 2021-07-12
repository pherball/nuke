import nuke
#import cryptomatte_utilities
#cryptomatte_utilities.setup_cryptomatte()

#OVERRIDES
#def prefs_onCreate():
#	nuke.thisNode()['ArrowColorUp'].setValue(0xff4c00ff)
#	nuke.Viewer()['hide_input'].setValue(0)
#	nuke.thisNode()['Read'].setValue(0xff4c00ff)
#nuke.addOnCreate(prefs_onCreate, nodeClass='Preferences')

#nuke.pluginAddPath( './' )
nuke.pluginAddPath( './gizmos' )
#LUMA
nuke.pluginAddPath( './gizmos/luma/Channel')
nuke.pluginAddPath( './gizmos/luma/Filter')
nuke.pluginAddPath( './gizmos/luma/Image')
nuke.pluginAddPath( './gizmos/luma/Keyer')
nuke.pluginAddPath( './gizmos/luma/Merge')
nuke.pluginAddPath( './gizmos/luma/Transform')
#
nuke.pluginAddPath( './gizmos/X_Tools/Icons')
nuke.pluginAddPath( './gizmos/X_Tools/Tools')
nuke.pluginAddPath( './gizmos/HeatWave_3.0')
# apTools
nuke.pluginAddPath( './gizmos/ap_tools/apColorSampler')
nuke.pluginAddPath( './gizmos/ap_tools/apComma')
nuke.pluginAddPath( './gizmos/ap_tools/apDespill')
nuke.pluginAddPath( './gizmos/ap_tools/apMatte')

#
nuke.pluginAddPath( './gizmos/CellNoise')


##Hagbarth Tools
nuke.pluginAddPath('./gizmos/Silk/hagbarth')
nuke.pluginAddPath('./gizmos/Silk/hagbarth/icons')
nuke.pluginAddPath('./gizmos/Silk/hagbarth/tools')
nuke.pluginAddPath('./gizmos/Silk/hagbarth/grapichs')
nuke.pluginAddPath( './gizmos/Silk/hagbarth/tools')


nuke.pluginAddPath( './gizmos/mmColorTarget_v2.0' )
nuke.pluginAddPath( './python' )
nuke.pluginAddPath( './plugins' )
nuke.pluginAddPath( './scripts' )


nuke.knobDefault('Dot.note_font_size', '100')
nuke.knobDefault('Comma.note_font_size', '11')
nuke.knobDefault('Dilate.channels', 'alpha')
nuke.knobDefault('Blur.channels', 'alpha')
nuke.knobDefault('Difference.gain', '100')
nuke.knobDefault('FilterErode.channels', 'alpha')
nuke.knobDefault('Erode.channels', 'alpha')
nuke.knobDefault('VectorBlur.channels', 'rgba')
nuke.knobDefault('Merge2.label', 'bbox|[value bbox]')
nuke.knobDefault('Keymix.label', 'bbox|[value bbox]')
nuke.knobDefault('ExponBlur_L_v05.crop_bounding_box', 'False')
nuke.knobDefault('Read.before', '0')
nuke.knobDefault('Read.after', '0')
nuke.knobDefault('Read.postage_stamp', 'False')
nuke.knobDefault('Viewer.hide_input', 'True')
nuke.knobDefault('Viewer.tile_color', '4294902015')
nuke.knobDefault('Viewer.frame_increment', '3')
nuke.knobDefault('BackdropNode.tile_color', '320017407')
nuke.knobDefault('BackdropNode.note_font_size', '50')
nuke.knobDefault('ScanlineRender.label', '[value filter]')
nuke.knobDefault('Transform.label', '[value filter]')
nuke.knobDefault('Shuffle.label', '[value in]')
nuke.knobDefault('ShuffleCopy.label', '[value out]')
#nuke.knobDefault('LumaOutput_v03_2.label', '[value format]')
#nuke.knobDefault('Camera2.label', '[join [lrange [split [file tail [value [topnode].file]] _] 4 4] _]')

nuke.pluginAddPath('./rvnuke')
