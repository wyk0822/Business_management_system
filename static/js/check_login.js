//异步向服务器发送请求，检查用户的登录状态
function check_login() {
    $.get('/check_login/',function (data) {
        var html = ""
        if(data.loginStatus == 1){
            //有用户
            html+="欢迎"+data.uname;
            html+="&nbsp;&nbsp;|&nbsp;&nbsp;"
            html+="<a href='/logout'>退出</a>";
        }else{
            //无用户
            html+="<a href='/login/'>[登录]</a>"
            html+="<a href='/register/'>[注册,有惊喜]</a>"
        }
        //将html赋值给#rightNav>li:first
        $("#rightNav>li:first").html(html)
    },'json');
}

$(document).ready(function () {
    //检查用户的登录状态
    check_login();
})

function a_visited(){
    var $a = $('#list_left ol a');       //找到你的a标签在哪一个元素下面
    $a.click(function(){         //给a标签添加点击事件
        console.log('asa')
        var $this = $(this);
        $a.removeClass();
        $this.addClass('current');
    }); 
}
