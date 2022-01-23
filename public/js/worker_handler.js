var w;

function startWorker() {
    if (typeof(Worker) !== "undefined") {
        if (typeof(w) == "undefined") {
            w = new Worker("../js/py_linker.js");
        }
        w.onmessage = function(event) {
            console.log(event.data);
            document.getElementById("english-transcript").innerHTML += "<b>Speaker " + event.data[0] + ":</b> " + event.data[1] + "<br>";
            document.getElementById("translated-transcript").innerHTML += "<b>Speaker " + event.data[0] + ":</b> " + event.data[2] + "<br>";
            document.getElementById("sentiment_img_1").src = "../sentiment/" + event.data[3];
            document.getElementById("sentiment_img_2").src = "../sentiment/" + event.data[4];
        };
    } else {
        document.getElementById("result").innerHTML = "Sorry! No Web Worker support.";
    }
}

function stopWorker() {
    w.terminate();
    w = undefined;
}
