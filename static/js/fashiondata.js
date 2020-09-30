//This file is for fashion index.html which allows the user to get the same data that is already on thier website everytime they wan to edit it

window.onload = function() {
    var contentlist = document.getElementsByClassName("webdata")[0].value.split('|');
    console.log("reached");
    if(contentlist.length >=1){
        console.log("yes greater than 1");
        count = 0;
        contentlist.forEach((data) => {

            if(count==0){
                document.getElementById('welcomemsg').value = data;
            } else if(count==1){
                document.getElementById('welcomemsgdescr').value = data;
            } else if(count==2){
                document.getElementById('fbsocial').setAttribute('href', data);
            } else if(count==3){
                document.getElementById('twsocial').setAttribute('href', data);
            } else if(count==4){
                document.getElementById('ytsocial').setAttribute('href', data);
            }
             else{
                document.getElementById('instasocial').setAttribute('href', data);
            }
            count++;

        });       
    };
    
    document.getElementById('lastlist').appendChild(document.getElementById('id_profile_pic'));

    
};

