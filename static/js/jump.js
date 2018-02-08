/**
 * Created by wueiz on 2018/2/7.
 */
var search = function() {
    let key = document.getElementsByName('search')[0].value;
    if (key) {
       window.location.href = "/search?keyword=" + key;
    }
}

var pageJump = function() {
    let page = document.getElementsByName('page')[0].value;
    let t = document.getElementsByName('now_type')[0].value;
    let searchKeyword = document.getElementsByName('searchKeyword')[0].value;
    if (searchKeyword){
        if (page) {
        window.location.href = "/search?keyword=" + searchKeyword + "&page=" + page;
        }
    }
    if (t) {
        if (page) {
        window.location.href = "/list?type=" + t + "&page=" + page;
        }
    }
}

document.getElementById("page_jump_icon").onclick = pageJump
document.getElementById("keyword_search").onclick = search
document.getElementsByName('search')[0].onkeyup = function(e) {
    var code = e.charCode || e.keyCode;
    if (code == 13) {
        search();
    }
}
document.getElementsByName('page')[0].onkeyup = function(e) {
    var code = e.charCode || e.keyCode;
    if (code == 13) {
        pageJump();
    }
}