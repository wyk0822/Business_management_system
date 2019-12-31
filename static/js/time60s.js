// 获取验证码倒计时
$(function () {
    var countdown = 60;

    $('#numbtn').on('click', function () {
        var obj = $("#numbtn");
        settime(obj);
        // var email = document.getElementById("useremail_id").innerText;
        var email_id = $("#useremail_id").val();
        console.log(email_id);
        $.ajax({
            url:"/userInfo/email_modfiy_pwd/",
            type:'get',
            data:{"useremail_id":email_id},
            dataType:'json',
            success:function (data) {
                alert(data.msg);
            }
        })
    });
    function settime(obj) { //发送验证码倒计时
        if (countdown == 0) {
            obj.attr('disabled', false);
//obj.removeattr("disabled");
            obj.html("免费获取验证码");
            countdown = 60;
            return;
        } else {
            obj.attr('disabled', true);
            obj.html("重新发送(" + countdown + ")");
            countdown--;
        }

        setTimeout(function () {
                settime(obj)
            }
            , 1000)
    }
});
