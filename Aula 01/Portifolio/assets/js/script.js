let nome = document.querySelector("#nome");
let email = document.querySelector("#email");
let msg = document.querySelector("#mensagem");
let enviar = document.querySelector("#enviar")

nome.addEventListener("keyup", () => {
  if (nome.value.length < 3) {
    nome.style.borderColor = "red";
  } else {
    nome.style.borderColor = "green";
  }
});

email.addEventListener('keyup', () => {
    if(email.value.indexOf('@') == -1 || email.value.indexOf('.') == -1){
        email.style.borderColor = "red";
    } else {
        email.style.borderColor = "green";
    }
})

msg.addEventListener('keyup', () => {
    if(msg.value.length > 100){
        msg.style.borderColor = "red";
    } else {
        msg.style.borderColor = "green";
    }
})

enviar.addEventListener('click', () => {
    alert('Enviado')
})