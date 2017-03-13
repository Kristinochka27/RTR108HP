function dec2bin(dec){
var x = document.getElementsByName("field1").value;
var y = (x >>> 0).toString(2);
document.getElementById("field1").value="x";
}

