const vscode = require('vscode');

function getOpenTerminalsCount() {
  const terminals = vscode.window.terminals;
  return terminals.length;
}

// Example usage
const openTerminalsCount = getOpenTerminalsCount();
console.log('Open Terminals Count:', openTerminalsCount);
