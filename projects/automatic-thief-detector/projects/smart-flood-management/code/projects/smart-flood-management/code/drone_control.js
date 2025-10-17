// File: drone_control.js
// Simple idea: control drone movement based on sensor data
function moveDrone(direction) {
  console.log(`Drone moving ${direction}`);
}

function respondToFlood(level) {
  if (level > 75) moveDrone("up");
  else if (level > 50) moveDrone("hover");
  else moveDrone("land");
}

respondToFlood(82); // Example run
