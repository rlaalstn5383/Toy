// USAGE
// c = register(과목이름, 교수님) -> 교수님 안 넣어도 됨
// 콘솔에 정보 출력
// 실행을 원할 경우->  c(과목 인덱스)
// 다시 검색을 하고 싶을 경우-> c = register(...)

function register(courseName, prof) {
    if (typeof jQuery == 'undefined') {
        var script = document.createElement('script');
        script.type = "text/javascript";
        script.src = "http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js";
        document.getElementsByTagName('head')[0].appendChild(script);
    }
    if (!(typeof courseName == 'string')) {
        courseName = '';
    }
    if (!(typeof prof == 'string')) {
        prof = '';
    }
    var nameSel = "tr:contains('" + courseName + "')";
    var profSel = ":contains('" + prof + "')";
    var tr = $("table#listTable").find(nameSel).filter(profSel);
    var a = tr.find("a[name = 'saveCourse']");

    console.log("##########################");
    console.log("found " + a.length + " class");
    $.each(tr, function(index, value) {
        console.log("# " + index + ": " + $(value).children().eq(5).text());
    })

    console.log("call the return function with index");

    function ret(index) {
        $.each(tr, function(i, value) {
            if (index == i) {
                var a = $(value).find("a[name = 'saveCourse']");
                setInterval(function() { a.click();}, 1000);
                console.log("macro works!");
                console.log("# " + $(value).children().eq(6).text() + " " + $(value).children().eq(5).text());
                return;
            }
        });
        console.log("incorrect index: " + index);
    }
    return ret;
}
