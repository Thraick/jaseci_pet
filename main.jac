walker init {
    report "init ran";
}



walker click_position{
    has x;
    has y;
    can mouse.click_mouse;

    // if (x and y): e = keyboard.click_mouse(x = x,y=y);
    e = mouse.click_mouse(x = "538.2100219726562",y="784.7853393554688");

    spawn here walker::type_command_with_keyBoard();
    report "click_position";
}

walker type_command_with_keyBoard{
    can keyboard.type_command;
    can keyboard.run_command_when_cursor_available;

    keyboard.run_command_when_cursor_available('jsctl -m');
    keyboard.run_command_when_cursor_available('actions list');
    report "type_command_with_keyBoard";
}

walker imgtotext{
    has anchor text;
    can screen.screenshot_to_text;

    text = screen.screenshot_to_text();
    report text;
}

walker record_mouse_positon{
    has anchor position;
    can mouse.record_first_mouse_click_position;

    position = mouse.record_first_mouse_click_position();
    report position;
}

// walker setup_project{

//     if('jaseci') in text{
//         // run actions
//     }
//     else{

//     }
// }

/*


run main.jac
get position
click position
type command to get id
better ocr img to text
run command with id
walker to set position

actions load local _project/mac/keyboard.py
actions load local _project/mac/imgtotext.py
actions load local _project/mac/mouse.py
jac build main.jac
sentinel register -set_active true -mode ir main.jir



walker run click_position
walker run type_command_with_keyBoard
walker run imgtotext








walker run run_commands -ctx "{\"text\": \"ls\"}"
walker run run_commands -ctx "{\"text\": \"cd ..\"}"


*/




// walker run_commands{
//     has text;
//     can keyboard.click_mouse_1;

//     r = keyboard.click_mouse_1(command=text);
//     std.out(r);
// }


// echo $$


/*
PROBLEMS OUTPUT DEBUGCONSOLE TERMINAL tv ws A xX
@- pet git:(main) x osascript -e ‘tell application "Terminal" to jaseci > jac build Find (t forh Aa ,ab, ,* x pI) zsh
id of window 1' Build of main.jirc , LD] python3...
35709 jaseci > sentinel register -set_active true -mode ir main.jir


*/