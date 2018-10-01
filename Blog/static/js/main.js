function  animate() {
    var el=document.getElementById('anim')
    el.className="bounce";
}
let k=document.getElementById('anim');
 k.addEventListener('focus',animate,false);