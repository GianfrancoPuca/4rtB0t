const converter = new showdown.Converter({ 
    sanitize: true 
  });
  
  document.addEventListener("DOMContentLoaded", function() {
    console.log("Script loaded. DOM is ready.");
  
    // Gestione Dark Mode
    const toggleDarkModeBtn = document.getElementById("toggleDarkMode");
    toggleDarkModeBtn.addEventListener("click", function() {
      document.body.classList.toggle("dark-mode");
    });
  });
  
  // Funzione di invio messaggio
  function sendMessage() {
    console.log("Sending message...");
    let userInput = document.getElementById("chat-input").value;
    let chatContainer = document.getElementById("chatlogs");
  
    if (userInput.trim() === "") return; 
  
    // Messaggio dell'utente
    let userDiv = document.createElement("div");
    userDiv.className = "chat self";
    let userText = document.createElement("p");
    let userImage = document.createElement("div");
    userText.textContent = userInput;
    userText.className = "chat-message";
    userImage.className = "user-photo";
    userDiv.appendChild(userText);
    userDiv.appendChild(userImage);
    chatContainer.appendChild(userDiv);
  
    document.getElementById("chat-input").value = "";
    chatContainer.scrollTop = chatContainer.scrollHeight;
  
    // Invio richiesta al backend
    fetch("/api/query", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ question: userInput }),
    })
    .then((response) => response.json())
    .then((data) => {
      // Risposta del bot
      let botDiv = document.createElement("div");
      botDiv.className = "chat robot";
  
      let botImage = document.createElement("div");
      botImage.className = "robot-photo";
  
      let rawMarkdown = data.answer;
      let htmlAnswer = converter.makeHtml(rawMarkdown);
  
      let botText = document.createElement("div");
      botText.className = "chat-message";
      botText.innerHTML = htmlAnswer;
  
      botDiv.appendChild(botImage);
      botDiv.appendChild(botText);
  
      chatContainer.appendChild(botDiv);
      chatContainer.scrollTop = chatContainer.scrollHeight;
  
      // Feedback
      if (data.request_feedback) {
          askForFeedback(userInput);
      }
    })
    .catch((error) => {
        console.error("Errore nella richiesta:", error);
    });
  }
  
  // Feedback (se usi questa funzione)
  function askForFeedback(userInput) {
    let chatContainer = document.getElementById("chatlogs");
  
    let feedbackDiv = document.createElement("div");
    feedbackDiv.className = "feedback-container";
  
    let promptText = document.createElement("p");
    promptText.textContent = "Per favore, fornisci un feedback sulla risposta:";
    feedbackDiv.appendChild(promptText);
  
    let positiveEmoji = document.createElement("span");
    positiveEmoji.textContent = "👍";
    positiveEmoji.style.fontSize = "24px";
    positiveEmoji.style.cursor = "pointer";
    feedbackDiv.appendChild(positiveEmoji);
  
    let negativeEmoji = document.createElement("span");
    negativeEmoji.textContent = "👎";
    negativeEmoji.style.fontSize = "24px";
    negativeEmoji.style.cursor = "pointer";
    feedbackDiv.appendChild(negativeEmoji);
  
    chatContainer.appendChild(feedbackDiv);
  
    positiveEmoji.addEventListener("click", function() {
      sendFeedback(userInput, "positivo");
      feedbackDiv.remove();
    });
  
    negativeEmoji.addEventListener("click", function() {
      sendFeedback(userInput, "negativo");
      feedbackDiv.remove();
    });
  }
  
  function sendFeedback(userInput, feedback) {
    console.log("Sending feedback for:", userInput, "with feedback:", feedback);
    fetch("/api/feedback", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ question: userInput, feedback: feedback }),
    })
    .then((response) => response.json())
    .then((feedbackData) => {
        console.log("Feedback response:", feedbackData);
        alert('Grazie per il feedback!');
    })
    .catch((error) => {
        console.error("Errore nell'invio del feedback:", error);
    });
  }
  
  // Attach event listener per click e tasto Enter
  document.getElementById("send").addEventListener("click", sendMessage);
  document.getElementById("chat-input").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
      e.preventDefault();
      sendMessage();
    }
  });
  