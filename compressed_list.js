function compress(v) {
  r = v.toString();
  b = document.getElementById("clb-"+r).innerHTML = "<input type=\"button\" value=\"+\" onclick=\"decompress("+r+")\">";
  t = document.getElementById("clt-"+r).style.display = "none";
};

function decompress(v) {
  r = v.toString();
  b = document.getElementById("clb-"+r).innerHTML = "<input type=\"button\" value=\"-\" onclick=\"compress("+r+")\">";
  t = document.getElementById("clt-"+r).style.display = "inline";
};

function compress_all() {
  h = document.getElementsByTagName("span");
  for (i=0;i<h.length;i++) {
    if (h[i].id=="") {continue;};
    if (h[i].id.slice(0,4)=="clb-") {
      compress(h[i].id.slice(4));
    };
  };
};
