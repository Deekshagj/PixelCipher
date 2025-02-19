function showTab(tab) {
    document.getElementById("encrypt").style.display = tab === "encrypt" ? "block" : "none";
    document.getElementById("decrypt").style.display = tab === "decrypt" ? "block" : "none";

    document.querySelectorAll(".tab-btn").forEach(btn => btn.classList.remove("active"));
    document.querySelector(`[onclick="showTab('${tab}')"]`).classList.add("active");
}

async function encryptImage() {
    let file = document.getElementById("encrypt-image").files[0];
    let message = document.getElementById("encrypt-message").value;
    let password = document.getElementById("encrypt-password").value;

    if (!file || !message || !password) {
        alert("Please fill all fields!");
        return;
    }

    let formData = new FormData();
    formData.append("image", file);
    formData.append("message", message);
    formData.append("password", password);

    let response = await fetch("/encrypt", { method: "POST", body: formData });
    let data = await response.json();
    
    if (data.image_url) {
        document.getElementById("encrypted-result").innerHTML = `<p>Encrypted Image:</p><img src="${data.image_url}" width="200">`;
    } else {
        alert("Encryption failed!");
    }
}

async function decryptImage() {
    let file = document.getElementById("decrypt-image").files[0];
    let password = document.getElementById("decrypt-password").value;

    if (!file || !password) {
        alert("Please fill all fields!");
        return;
    }

    let formData = new FormData();
    formData.append("image", file);
    formData.append("password", password);

    let response = await fetch("/decrypt", { method: "POST", body: formData });
    let data = await response.json();
    
    if (data.decrypted_text) {
        document.getElementById("decrypted-message").innerHTML = `<p>Decrypted Message: ${data.decrypted_text}</p>`;
    } else {
        alert("Decryption failed!");
    }
}
