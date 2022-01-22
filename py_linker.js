var i = 0;

function timedCount() {
    i = i + 1;
    //english =
    //speaker =
    //translated =
    //sentiment_1 = get from analyse if new message
    //sentiment_2 = get from analyse if new message
    let english = "hello there!";                   //get from deepgram
    let speaker = 0;                                //get from deepgram (0 = first speaker, 1 = second speaker)
    let translated = "bonjour!";                    //get from translated(english)
    let sentiment = [0.8, -0.2];                    //get from analyse(english)
    let sentiment_img = ["meh.png", "meh.png"];
    if (sentiment[speaker] < -0.2) {
        sentiment_img[speaker] = "frown.png";
    } else if (sentiment[speaker] > 0.2) {
        sentiment_img[speaker] = "happy_face.png";
    } else {
        sentiment_img[speaker] = "meh.png";
    }
    
    postMessage([english, translated, sentiment_img[0], sentiment_img[1]]);
    setTimeout("timedCount()",500);
}

timedCount();
