document.addEventListener('DOMContentLoaded', function () {
    var startButton = document.getElementById('startRecording');
    var stopButton = document.getElementById('stopRecording');
    var audioPlayer = document.getElementById('audioPlayer');
    var audioBlob; // Variable to store the recorded audio blob

    var recorder;
    var chunks = []; // Array to store the recorded audio data chunks

    startButton.addEventListener('click', function () {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(function (stream) {
                recorder = new MediaRecorder(stream);
                recorder.ondataavailable = function (e) {
                    chunks.push(e.data);
                };
                recorder.start();
                startButton.disabled = true;
                stopButton.disabled = false;
            })
            .catch(function (error) {
                console.error('Erreur lors de l\'obtention de l\'accès au microphone :', error);
            });
    });

    stopButton.addEventListener('click', function () {
        recorder.stop();
        recorder.onstop = function () {
            audioBlob = new Blob(chunks, { type: 'audio/webm' });
            audioPlayer.src = URL.createObjectURL(audioBlob);
            audioPlayer.style.display = 'block';
            startButton.disabled = false;
            stopButton.disabled = true;
        };
    });

    // Submit form with recorded audio data
    var form = document.querySelector('form');
    form.addEventListener('submit', function (e) {
        e.preventDefault();
        var formData = new FormData(form);
        formData.append('fichier_audio', audioBlob, 'enregistrement.webm');
        var xhr = new XMLHttpRequest();
        xhr.open('POST', form.action, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                // Handle response from server
            }
        };
        xhr.send(formData);
    });
});
