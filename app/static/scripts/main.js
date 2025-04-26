function showPopup(message) {
    document.getElementById("popup-message").innerText = message;
    document.getElementById("popup").style.display = "flex";
  }
  
  function closePopup() {
    document.getElementById("popup").style.display = "none";
  }
  
  function addContacts() {
    fetch("/contacts/add", {
      method: "POST"
    })
    .then(response => response.json())
    .then(data => {
      if (data.errors && data.errors.length > 0) {
        showPopup(`❌ Error adding contacts: ${data.errors.length} falha(s).`);
      } else {
        showPopup(`✅ ${data.total_created} contacts added with success!`);
      }
    })
    .catch(error => {
      console.error("Error:", error);
      showPopup("❌ Error connecting to the server.");
    });
  }
  