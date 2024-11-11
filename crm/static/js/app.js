document.addEventListener('DOMContentLoaded', function() {
  console.log("app.js loaded");
  const messages = document.querySelectorAll('.message-timer');
  messages.forEach(function(message) {
      setTimeout(function() {
          message.style.display = "none";
          console.log("Message hidden");
      }, 2000);
  });
});
