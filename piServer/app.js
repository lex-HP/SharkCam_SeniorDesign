const express = require("express");
const app = express();
const http = require("http");
const WebSocket = require("ws");
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

//const { spawn } = require('child_process');


function startPythonProcess() {
    const { spawn } = require('child_process'); // Move this line here
    const child = spawn('python', ['piCommunication.py', 30]);

    // use child.stdout.setEncoding('utf8'); if you want text chunks
    child.stdout.on('data', (chunk) => {
        const pythonMessage = chunk.toString();// data from the standard output is here as buffers
        console.log(pythonMessage);
        if (pythonMessage.includes('take pic')) {
            wss.clients.forEach(function each(client) {
                if (client.readyState === WebSocket.OPEN) {
                    client.send("pic command");
                    console.log("sending message to take pic");
                }
            });
        }
    });

    // log any errors that occur
    child.stderr.on('data', (data) => {
        console.error(`child process stderr:\n${data}`);
    });

    child.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });

    return child; // Return the child process object instead of the undefined "process" variable
}

function stopPythonProcess() {
    const { spawn } = require('child_process'); // Move this line here
    const child = spawn('python', ['stopCommand.py']);

    // log any errors that occur
    child.stderr.on('data', (data) => {
        console.error(`child process stderr:\n${data}`);
    });

    child.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });

    return child;

}

let currentProcess = null;

wss.on("connection", function connection(ws) {
    console.log('New connection');
    var incomingMsg;
    ws.on('message', (data) => { // this loops forever. Why?
        incomingMsg = data.toString();
        if (incomingMsg == 'start') {
            console.log("start message received");
            if (!currentProcess) {
                console.log("starting routine code")
                currentProcess = startPythonProcess();
            }
        } else if (incomingMsg == 'stop') {
            console.log("stop message received");
            currentProcess.kill();
            currentProcess = stopPythonProcess();

        } else {
            console.log(incomingMsg);
        }
    });
    ws.onclose = (e) => {
        console.log("connection closed");
        if (currentProcess) {
            currentProcess.kill();
            currentProcess = null;
        }
    }
});
server.listen(8080, () => {
    console.log("Listening to port 8080");
});

