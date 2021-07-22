const itens = document.querySelectorAll('.itens') /* pega todos os elementos que possuem a class itens */

itens.forEach((item)=>{ /* Varre a lista de itens, item a item */
   item.addEventListener('click', () => { /* quando o item atual do forEach for clicado executa a arrow function */
      if(item.style.textDecoration == ''){ /* se a decoração do texto for vazia faça:*/
         item.style.textDecoration = 'line-through' /*  coloque um traço no meio do texto atual */
         item.style.backgroundColor = '#ccc' /* muda a cor do backgroud do item atual */
      } else { /* se já existir decoração faça: */
         item.style.textDecoration = '' /* limpa a decoração do texto */
         item.style.backgroundColor = '#fff' /* muda a cor do background do item atual */
      }
   })
})

