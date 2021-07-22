let nome = document.querySelector("#nome");
let email = document.querySelector("#email");
let msg = document.querySelector("#mensagem");
let enviar = document.querySelector("#enviar");

nome.addEventListener("keyup", () => {
  if (nome.value.length < 3) {
    nome.style.borderColor = "red";
  } else if (nome.value.length >= 3) {
    nome.style.borderColor = "green";
  }
  if (nome.value == "") {
    nome.style.borderColor = "c###";
  }
});

email.addEventListener("keyup", () => {
  if (email.value.indexOf("@") == -1 || email.value.indexOf(".") == -1) {
    email.style.borderColor = "red";
  } else {
    email.style.borderColor = "green";
  }
  if (email.input.value == "") {
    email.style.borderColor = "c###";
  }
});

msg.addEventListener("keyup", () => {
  if (msg.value.length > 100) {
    msg.style.borderColor = "red";
  } else {
    msg.style.borderColor = "green";
  }
  if (msg.value == "") {
    msg.style.borderColor = "c###";
  }
});

enviar.addEventListener("click", () => {
  alert("Enviado");
});   
