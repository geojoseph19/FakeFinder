
// function pVisibilityOff() {
//     var a = document.getElementById("t1");
//     var b = document.getElementById("textview-wrapper");
//     var c = document.getElementById("textrow-1");
//     a.style.display = "none";
//     b.style.display = "none";
//     c.style.display = "none";
//   }

// function pVisibilityOn() {
//     var a = document.getElementById("t1");
//     a.style.display = "block";
//     var a = document.getElementById("t2");
//     a.style.display = "block";

// }                                           src="{% static 'ffmain/js/ffhome.js' %}" type="text/javascript"

var p = "{{ prediction}}";

if(p)
{
    alert("Hello, world!");
}