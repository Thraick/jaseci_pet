walker check_for_terminal{
    has anchor status;
    can screen.screenshot_to_text;
    can jstopy.run_javascript_code;

    text = screen.screenshot_to_text();

    if("TERMINAL" in text){
        // check for jaseci else run jsctl -m
        status['terminal'] = true;
        if("jaseci" in text) {
            status['jaseci'] = true;
        }
        else{
            // status
            con = jstopy.run_javascript_code();
            
        }
    }
    else{
        // create terminal
    }
}
