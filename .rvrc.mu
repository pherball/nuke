require rvui;

documentation:
"Called when a session is first created";

\: initialize (object;)
{
    //
    //  To override default bindings just set them after you call this,
    //  otherwise, you need to provide all of the bindings if you
    //  replace it.
    //

    rvui.defineDefaultBindings();
    //bind("key-down--q", cycleStackForward, "Cycle Image Stack Forwards");

    //
    //  You can add to rvui.mainMenu before calling this
    //

    defineModeMenu("default", rvui.buildMainMenu());

    //
    //  Make a new State object. Any object can be returned here
    //  (tuple, etc). In this case we're going to provide the default
    //  State object. 
    //

    return rvui.newStateObject();
}


// CUSTOM HOTKEYS

function: setup(void;)
{
    app_utils.bind("key-down--q", \:(void; Event event)
    {
        rvui.cycleStackForward(nil);
    });

}
