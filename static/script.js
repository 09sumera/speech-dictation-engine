let mediaRecorder;
let audioChunks = [];

// START RECORDING
async function startRecording() {

    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

    mediaRecorder = new MediaRecorder(stream);

    audioChunks = [];

    mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
    };

    mediaRecorder.start();

    alert("Recording started");
}


// STOP RECORDING
function stopRecording() {

    mediaRecorder.stop();

    mediaRecorder.onstop = async () => {

        const audioBlob = new Blob(audioChunks, { type: "audio/wav" });

        const file = new File([audioBlob], "recording.wav");

        const formData = new FormData();

        formData.append("audio", file);

        // Get selected tone
        let tone = "formal";

        let toneElement = document.getElementById("toneSelect");

        if (toneElement) {
            tone = toneElement.value;
        }

        formData.append("tone", tone);

        const response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        const html = await response.text();

        document.open();
        document.write(html);
        document.close();
    };

    alert("Recording stopped");
}


// THEME SWITCH
document.getElementById("themeBtn").onclick = function () {

    document.body.classList.toggle("dark-theme");

    if (document.body.classList.contains("dark-theme")) {
        this.innerText = "☀ Light Mode";
    }
    else {
        this.innerText = "🌙 Dark Mode";
    }

};


// DROPDOWN MENU
document.querySelectorAll('.dropdown').forEach(dropdown => {

    dropdown.addEventListener('click', function (e) {

        e.stopPropagation();

        const content = this.querySelector('.dropdown-content');

        if (content.style.display === "block") {
            content.style.display = "none";
        }
        else {
            document.querySelectorAll('.dropdown-content').forEach(dc => dc.style.display = 'none');
            content.style.display = "block";
        }

    });

});

document.body.addEventListener('click', () => {
    document.querySelectorAll('.dropdown-content').forEach(dc => dc.style.display = 'none');
});


// COPY TEXT
function copyText(id) {

    const text = document.getElementById(id).innerText;

    navigator.clipboard.writeText(text);

    alert("Copied!");

}