
var  icon_sos = document.getElementsByClassName("icon_sosial");
const contact_me = document.getElementById("show_contact");
const sendtext = document.getElementById("text_send");




function send_message(){
  sendtext.style.display='none';
  console.log("benar");
}


/*give element clik on send text */
contact_me.style.cursor = 'pointer';
contact_me.onclick = function(){
  sendtext.style.display='block';
}




/* give element click on medsos icon */
for(let i=0;i<icon_sos.length;i++){
  icon_sos[i].addEventListener('click',function(event){
    if(i==1){
      window.open("https://www.facebook.com/NoverHalomoan","","height=260,width=500,left=100,top=100,menubar=0");
    }
    if(i==0){
      window.open("https://www.instagram.com/vernover/","","height=260,width=500,left=100,top=100,menubar=0");
    }

});
}



