let recognition;

if ('webkitSpeechRecognition' in window) {

    recognition = new webkitSpeechRecognition();

    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = "en-US";

    let finalTranscript = "";

    recognition.onstart = function () {
        console.log("Speech recognition started");
    };

    recognition.onresult = function (event) {

        console.log(event); // debug

        let interimTranscript = "";

        for (let i = event.resultIndex; i < event.results.length; i++) {

            let text = event.results[i][0].transcript;

            if (event.results[i].isFinal) {
                finalTranscript += text + " ";
            } else {
                interimTranscript += text;
            }

        }

        let fullText = finalTranscript + interimTranscript;

        document.getElementById("liveText").value = fullText;

        /* send text to backend */

        fetch("/process_text", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: fullText })
        })
            .then(res => res.json())
            .then(data => {
                document.getElementById("cleanOutput").innerText = data.cleaned;
            });

    };

    recognition.onerror = function (event) {
        console.error("Speech recognition error:", event.error);
    };

} else {

    alert("Speech recognition not supported in this browser");

}

function startDictation() {

    document.getElementById("listeningIndicator").style.display = "block";
    document.getElementById("micIcon").classList.add("mic-active");

    recognition.start();

}

function stopDictation() {

    document.getElementById("listeningIndicator").style.display = "none";
    document.getElementById("micIcon").classList.remove("mic-active");

    recognition.stop();

}