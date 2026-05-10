function parseScores(scoresString) {
   // TODO: Compete the function
   var arr = [];
   arr = scoresString.split(" ")
   return arr;
}

function buildDistributionArray(scoresArray) {
   // TODO: Compete the function

   var par = scoresArray;
   var grades = [0,0,0,0,0];

   for (i=0; i<par.length; i++){

      if(parseInt(par[i])  >= 90 ){
         grades[0]++;
      }

      else if (parseInt(par[i]) >= 80 && parseInt(par[i]) <=89 ){
         grades[1]++;
      }

      else if (parseInt(par[i]) >= 70 && parseInt(par[i])<=79 ){
         grades[2]++;
      }
      else if (parseInt(par[i]) >= 60 && parseInt(par[i])<=69 ){
         grades[3]++;
      }
      else{
         grades[4]++;
      }
   }

   return grades;
}

function setTableContent(userInput) {
   // TODO: Compete the function
   
   // var x = buildDistributionArray(parseScores(userInput))
   var array = parseScores(userInput);
   var grades = buildDistributionArray(array);

   var a = grades[0] * 10;
   var b = grades[1] * 10;
   var c = grades[2] * 10;
   var d = grades[3] * 10;
   var f = grades[4] * 10

   var element = document.getElementById("distributionTable")

   if (userInput == ""){
      element.innerHTML = "<tr><td>No graph to display</td></tr>"
   }
   else {
   element.innerHTML = 
   "<tr><td><div style='height:"+a+"px' class='bar0'></div></td>"+
   "<td><div style='height:"+b+"px' class='bar1'></div></td>"+
   "<td><div style='height:"+c+"px' class='bar2'></div></td>"+
   "<td><div style='height:"+d+"px' class='bar3'></div></td>"+
   "<td><div style='height:"+f+"px' class='bar4'></div></td></tr>"+
   "<tr><td>A</td><td>B</td><td>C</td><td>D</td><td>F</td></tr>"+
   "<tr><td>"+grades[0]+"</td><td>"+grades[1]+"</td><td>"+grades[2]+"</td><td>"+grades[3]+"</td><td>"+grades[4]+"</td></tr>";
   }
}


// The argument can be changed for testing purposes
setTableContent("");