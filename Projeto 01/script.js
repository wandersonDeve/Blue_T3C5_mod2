let atual = 0; // VARIAVEL USADA PARA CONTROLE DA GAMBIARRA QUE EU FIZ KKKKKK

// FUNÇÃO QUE MUDARÁ A IMAGEM E O TITULO
function novaImagem() {
  let texto = document.querySelector("h2"); // VARIAVEL COM O CAMINHO DA TAG H2 NO HTML, PODERIA NAO TER USADO, MAS O CODIGO FICA MELHOR DE VISUALIZAR NA MINHA OPNIÃO
  if (document.querySelector("section").id == "img"){
    if (atual == 0) {
      document.getElementById("imagem").setAttribute("src", "assets/img/chapado_g.jpg");
      document.getElementById("pequena").setAttribute("srcset", "assets/img/chapado_p.jpg");
      document.getElementById("media").setAttribute("srcset", "assets/img/chapado_m.jpg");
      texto.textContent = "E aêêêêêê";
      atual = 1;
    } else {
      document.getElementById("imagem").setAttribute("src", "assets/img/normal_g.jpg");
      document.getElementById("pequena").setAttribute("srcset", "assets/img/normal_p.jpg");
      document.getElementById("media").setAttribute("srcset", "assets/img/normal_m.jpg");
      texto.textContent = "Oi, o que você tá fazendo ?";
      atual = 0;
    } // FECHAMENTO DO ELSE DA OPÇÃO DA IMAGEM

  } else{
    if (atual == 0) {
      document.getElementById("video").setAttribute("src", "assets/img/parte2.mp4")
      texto.textContent = "E aêêêêêê";
      atual = 1;
    } else {
      document.getElementById("video").setAttribute("src", "assets/img/parte1.mp4")
      texto.textContent = "Oi, o que você tá fazendo ?";
      atual = 0;
    } // FECHAMENTO DO ELSE DA OPÇÃO DO VIDEO
  } // FECHAMENTO DO ELSE DA OPÇÃO GERAL (VIDEO/IMAGEM)
} // FECHAMENTO DA FUNÇÃO