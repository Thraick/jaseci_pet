walker init {
    can keyboard.click_mouse;
    can keyboard.type_command;
    // can keyboard.click_mouse_1;
    can keyboard.run_command;
    can screen.screenshot_to_text;

    e = keyboard.click_mouse(x = "538.2100219726562",y="784.7853393554688");
    // std.out(e);
    q = keyboard.type_command();

    text = screen.screenshot_to_text();
    report text;


    // a = keyboard.run_command(command="python");
    // std.out(a);

    // q = keyboard.type_command(command='python --version', window_id=e);
    // std.out(q);
    // r = keyboard.click_mouse_1(command='python');


}

/*


run main.jac
get position
click position
type command to get id
better ocr img to text
run command with id
walker to set position

actions load local keyboard.py
actions load local imgtotext.py
jac build main.jac
sentinel register -set_active true -mode ir main.jir



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