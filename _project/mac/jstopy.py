import subprocess
from jaseci.actions.live_actions import jaseci_action

@jaseci_action(act_group=["jstopy"], allow_remote=True)
def run_javascript_code():
    javascript_file = 'get_open_terminals.js'
    command = ['node', javascript_file]
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the captured output
    print(result.stdout)

# Run the JavaScript code
run_javascript_code()
