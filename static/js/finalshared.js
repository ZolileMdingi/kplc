window.onload = function() {
    var contentlist = document.getElementById('rwebdata').innerHTML.split('|');
    
    count = 0;
    contentlist.forEach((data) => {
        console.log(data);
        if(count==0){
            document.getElementById('welcomepg').innerHTML = data;
        } else if(count==1){
            document.getElementById('welcomepgdescr').innerHTML = data;
        } else if(count==2){
            document.getElementById('fblink').setAttribute('href', data);
        } else if(count==3){
            document.getElementById('twlink').setAttribute('href', data);
        } else if(count==4){
            document.getElementById('ytlink').setAttribute('href', data);
        }
         else{
            document.getElementById('instalink').setAttribute('href', data);
        }
        count++;
        
    });
    
};




