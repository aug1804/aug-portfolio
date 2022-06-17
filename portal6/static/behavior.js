document.addEventListener("DOMContentLoaded", function(event) {

  // alert('Hello!');

  var thumbnailElement = document.getElementById("smart_thumbnail");
  
  thumbnailElement.addEventListener("click", function() {
      
    var thumbnailClassName = thumbnailElement.className;

    // alert("I saw you click! Class Name: " + thumbnailClassName + ".");

    if (thumbnailElement.className == "") {
      thumbnailElement.className = "small";
      //alert("New Class Name:" + thumbnailElement.className + ".");

    } else if (thumbnailElement.className == "small") {
      thumbnailElement.className = "";
      //alert("New Class Name: big.");

    } else {
      alert("thumbnailElement.className:" + thumbnailElement.className + ".");
      thumbnailElement.className = "small";
      //alert("New Class Name:" + thumbnailElement.className + ".");
    }

    
  });

});

//function inscreverse(){
//  window.open("https://apply.holbertonschool.com");
//}
