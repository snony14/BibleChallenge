var disp_chapter = false;

function chapterOrWhole(elem) {
   var selected_chapter = elem.value;
   if(selected_chapter==0){
     disp_chapter = false;
     document.getElementById("for_chapters").style.display = "none";
   }else{
     disp_chapter = true;
     document.getElementById("for_chapters").style.display = "block";
   }
}

validate = function(){
  var challengeType =  document.getElementById('sel1');
  var desc = document.getElementById('comment');
  var title = document.getElementById('title');
  var start_date = document.getElementById('start_date');
  var end_date = document.getElementById('end_date');

}

var added_goals = [];
function dynamicEvent(){

  //console.log(added_goals.length);
}
//TODO add pagination here
addGoal = function(){

  var para = document.createElement("div");
  var node = document.createTextNode("0");
  para.appendChild(node);
  para.onclick = dynamicEvent;
  var element = document.getElementById("goals");
  element.appendChild(para);
  added_goals.push(para);

}

var toGoal=function(){

  var val = document.getElementById("for_goals").value - 1;
  var chapters = document.getElementById("chapters").value;
  var select = document.getElementById("book");
  var book = select.options[select.selectedIndex].text;
  added_goals[val].innerHTML = book+" ch.:"+chapters;
}
getHtmlText = function(numb){

}


/*

*/
updateChapterCount = function(){
  var select = document.getElementById("book");
  var value = select.value;
  var path = "/bible/" + value+"/";

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var response = xhttp.responseText
     document.getElementById('quantity').innerHTML = response;
    }
  };
  //
  xhttp.open("GET",path, true);
  xhttp.send();
}
