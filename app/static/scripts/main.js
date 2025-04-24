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
        showPopup(`❌ Erro ao adicionar contatos: ${data.errors.length} falha(s).`);
      } else {
        showPopup(`✅ ${data.total_created} contato(s) adicionados com sucesso!`);
      }
    })
    .catch(error => {
      console.error("Erro:", error);
      showPopup("❌ Erro ao conectar com o servidor.");
    });
  }
  