// 获取验证码倒计时
$(function () {
    var countdown = 60;

    $('#numbtn').on('click', function () {
        var email_id = $("#useremail_id").val();
        var user_id = $("#user_id").val();
        var obj = $("#numbtn");
        chack_null = check_userid_useremail(user_id, email_id);
        // alert(chack_null);
        if (chack_null == 1) {
            settime(obj);
            $.ajax({
                url:"/userInfo/send_email/",
                type:'get',
                data:{
                    "useremail_id":email_id,
                    "user_id": user_id
                },
                dataType:'json',
                success:function (data) {
                    alert(data.msg);
                }
            })

        }else {
            // alert("false");
            return false;
        }
        // check_userid_useremail(user_id, email_id);



        // console.log(email_id);

    });

    function settime(obj) { //发送验证码倒计时
        if (countdown == 0) {
            obj.attr('disabled', false);
//obj.removeattr("disabled");
            obj.html("重新获取验证码");
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

    function check_userid_useremail(userid, useremail) {
        if (userid == ""){
            alert("jsuser id cannot be empty");
            return 0;
        } else if (useremail == ""){
            alert("jsUser mailbox cannot be empty");
            return 0;
        }else {
            return 1;
        }

    }
});
