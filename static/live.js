// Speech recognition setup

let recognition;
let finalTranscript = "";
let lastSpokenText = "";

if ('webkitSpeechRecognition' in window) {

    recognition = new webkitSpeechRecognition();

    recognition.continuous = true;
    recognition.interimResults = false; // FIX: disable interim results for mobile stability
    recognition.lang = "en-US";

    // When recording starts
    recognition.onstart = function () {
        console.log("Speech recognition started");
    };

    // When speech result comes
    recognition.onresult = function (event) {

        for (let i = event.resultIndex; i < event.results.length; i++) {

            let text = event.results[i][0].transcript;

            if (event.results[i].isFinal) {

                // Prevent duplicate phrases
                if (!finalTranscript.includes(text)) {
                    finalTranscript += text + " ";
                }

                let fullText = finalTranscript.trim();
                lastSpokenText = fullText;

                // Show transcript
                document.getElementById("liveText").value = fullText;

                // Get tone
                const toneSelect = document.getElementById("toneSelect");
                let selectedTone = "formal";

                if (toneSelect) {
                    selectedTone = toneSelect.value.toLowerCase();
                }

                console.log("Tone being sent:", selectedTone);

                // Send to backend
                fetch("/process_text", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        text: fullText,
                        tone: selectedTone
                    })
                })
                    .then(response => response.json())
                    .then(data => {

                        if (data.cleaned) {
                            document.getElementById("cleanOutput").innerText = data.cleaned;
                        }

                    })
                    .catch(error => {
                        console.error("Backend error:", error);
                    });
            }
        }
    };

    // Error handling
    recognition.onerror = function (event) {
        console.error("Speech recognition error:", event.error);
    };

    recognition.onend = function () {
        console.log("Speech recognition ended");
    };

} else {

    alert("Speech recognition is not supported in this browser. Please use Google Chrome.");

}


// Start recording
function startDictation() {

    finalTranscript = "";

    document.getElementById("liveText").value = "";

    document.getElementById("listeningIndicator").style.display = "block";

    let micIcon = document.getElementById("micIcon");
    if (micIcon) {
        micIcon.classList.add("mic-active");
    }

    recognition.start();
}


// Stop recording
function stopDictation() {

    document.getElementById("listeningIndicator").style.display = "none";

    let micIcon = document.getElementById("micIcon");
    if (micIcon) {
        micIcon.classList.remove("mic-active");
    }

    recognition.stop();
}


// When tone changes, reprocess the last spoken text
const toneSelect = document.getElementById("toneSelect");

if (toneSelect) {

    toneSelect.addEventListener("change", function () {

        if (!lastSpokenText.trim()) return;

        const selectedTone = this.value.toLowerCase();

        fetch("/process_text", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: lastSpokenText,
                tone: selectedTone
            })
        })
            .then(res => res.json())
            .then(data => {

                if (data.cleaned) {
                    document.getElementById("cleanOutput").innerText = data.cleaned;
                }

            })
            .catch(err => console.error(err));

    });

}