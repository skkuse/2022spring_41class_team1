
var emailCheck = false;

function validate(){
    if(!emailCheck){
        alert("이메일 주소를 확인해주세요!")
        return false;
    }
    if($("#loginPw").val()==""){
        alert("비밀번호를 작성해주세요!")
        return false;
    }
    if($("#loginPw").val() != $("#loginPwChk").val()){
        alert("비밀번호가 다릅니다!")
        return false;
    }
    return true;
}

$(document).ready(function(){
    //ajax csrf 토큰 생성
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var duplication_check = function(){
        //이메일 유효성 확인
        var regEmailPattern = /^[a-zA-Z_\-0-9]+@[a-z]+.[a-z]+$/;
        if(!regEmailPattern.test($('#Email').val())){
            emailCheck = false;
            $("#dup_msg").css("display","block")
            $("#dup_msg").text("이메일 형식이 맞지 않습니다")
            $("#dup_msg").css("color","red")
            return false;
        }
        //이메일 중복 확인
        $.ajax({
            type : 'post', //post 전송방식으로 전달
            dataType : 'json', //json 언어로 전달
            url : '/duplication_check', //이 주소에 데이터 전달
            data : {userEmail:$('#Email').val()}, //전달할 데이터
            async : false, //값을 전달 받은 후 실행,

            success : function (data){
            //리턴된 정보를 콘솔로그로 확인
            if(data.result == true){
                //사용해도 좋은 이메일 주소인 경우
                emailCheck = true;
                $("#dup_msg").css("display","block")
                $("#dup_msg").text("사용 가능한 이메일 주소입니다")
                $("#dup_msg").css("color","blue")
                
            }else{
                //이미 존재하는 이메일 주소인 경우
                emailCheck = false;
                $("#dup_msg").css("display","block")
                $("#dup_msg").text("이미 존재하는 이메일 주소입니다")
                $("#dup_msg").css("color","red")
            }
            },
            //AJAX 통신 에러 발생시 에러코드 확인
            error: function (request, status, error){
            console.log('request ' + request);
            console.log('status ' + status);
            console.log('error ' + error);
            }
        });
    };
    $("#Email").focusout(duplication_check);
});