let mediaRecorder;
let audioChunks = [];

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

function stopRecording() {

    mediaRecorder.stop();

    mediaRecorder.onstop = async () => {

        const audioBlob = new Blob(audioChunks, { type: "audio/wav" });

        const file = new File([audioBlob], "recording.wav");

        const formData = new FormData();

        formData.append("audio", file);

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