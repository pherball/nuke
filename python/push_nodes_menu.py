push_menu = nuke.menu('Nuke').addMenu('Push')

push_menu.addCommand(
    'Down',
    'from nuke_move_nodes import push_nodes; push_nodes.push(down=True)',
     'ctrl+PgDown',
     shortcutContext=2
)
push_menu.addCommand(
    'Up',
    'from nuke_move_nodes import push_nodes; push_nodes.push(up=True)',
     'ctrl+PgUp',
     shortcutContext=2
)
push_menu.addCommand(
    'Left',
    'from nuke_move_nodes import push_nodes; push_nodes.push(left=True)',
)
push_menu.addCommand(
    'Right',
    'from nuke_move_nodes import push_nodes; push_nodes.push(right=True)',
)
