(function register() {
    var a = $("a[name = 'saveCourse']");
    $.each(a.parent().parent(), function(i, v) {
        if ($(v).find(".macro").length == 0) {
            $(v).append("<td><a href='#' class='macro'>매크로</a></td>");
            var m = $(v).find(".macro");
            var c = $(v).find("a[name = 'saveCourse']");
            m.click(function() {
                setInterval(function() { c.click();}, 1000);
            });
        }
    });
})();
