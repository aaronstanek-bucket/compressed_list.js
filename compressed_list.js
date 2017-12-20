function compress(v) {
  var r = v.toString();
  var b = document.getElementById("clb-"+r).innerHTML = "<input type=\"button\" value=\"+\" onclick=\"decompress("+r+")\">";
  var t = document.getElementById("clt-"+r).style.display = "none";
};

function decompress(v) {
  var r = v.toString();
  var b = document.getElementById("clb-"+r).innerHTML = "<input type=\"button\" value=\"-\" onclick=\"compress("+r+")\">";
  var t = document.getElementById("clt-"+r).style.display = "inline";
};

function compress_all() {
  var h = document.getElementsByTagName("span");
  for (let i=0;i<h.length;i++) {
    if (h[i].id=="") {continue;};
    if (h[i].id.slice(0,4)=="clb-") {
      compress(h[i].id.slice(4));
    };
  };
};
