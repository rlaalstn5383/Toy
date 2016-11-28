// USAGE
// c = register(과목이름, 분반) -> 분반 안 넣어도 됨
// 콘솔에 정보 출력
// 실행을 원할 경우->  c()
// 다시 검색을 하고 싶을 경우-> c = register(...)

function register(courseName, lectureClass) {
    if (typeof jQuery == 'undefined') {
        var script = document.createElement('script');
        script.type = "text/javascript";
        script.src = "http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js";
        document.getElementsByTagName('head')[0].appendChild(script);
    }
    if (!(typeof courseName == 'string')) {
        courseName = '';
    }
    if (!(typeof lectureClass == 'string')) {
        lectureClass = '';
    }
    var nameSel = "tr:contains('" + courseName + "')";
    var classSel = ":contains('" + lectureClss + "')";
    var a = $("table#listTable").find(nameSel).filter(classSel).find("a");

    console.log("found " + tr.length + " class");
    return function() { setInterval(function() { a.click(); }, 1000); };
}
