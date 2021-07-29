const itens = document.querySelectorAll('.itens')

itens.forEach((item)=>{
   item.addEventListener('click', () => { 
      if(item.style.textDecoration == ''){ 
         item.style.textDecoration = 'line-through'
         item.style.backgroundColor = 'rgba(255, 255, 255, 0.2)' 
      } else { 
         item.style.textDecoration = '' 
         item.style.backgroundColor = ''
      }
   })
})

