const express = require("express");
const app = express();
const http = require("http");
const WebSocket = require("ws");
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });
const port = 3000;

//const { spawn } = require('child_process');

const { spawn } = require('child_process');
const child = spawn('ls',);
// use child.stdout.setEncoding('utf8'); if you want text chunks
child.stdout.on('data', (chunk) => {
    // data from the standard output is here as buffers
});
// since these are streams, you can pipe them elsewhere
child.stderr.pipe(dest);
child.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
});


function startPythonProcess() {
    const process = spawn('python', ['piCommunication.py']);
    process.stdout.on('data', function (data) {
        console.log("Data from python script");
        const data1 = data.toString();
        console.log(data1);
    });
    return process;
}

let currentProcess = null;

wss.on("connection", function connection(ws) {
    console.log('New connection');
    ws.send('howdy');
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


