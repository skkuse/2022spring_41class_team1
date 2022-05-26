
function timeOutCall()
 {
    setTimeout(function(){ //기능의 시간을 지연
        $('#valueError').text('');
     }, 2000);
 }

$(document).ready(function(){
    /*로그인 확인*/
    var loginSubmit = $('#loginSubmit'); //로그인 버튼
    var studentID = $('#studentID'); //이메일 주소 입력 폼
    var loginPw = $('#loginPw'); //로그인 폼 비밀번호 입력 폼
    //로그인하기 버튼 클릭 이벤트
    loginSubmit.click(function(){
        //이메일 유효성 검사
        var regEmailPattern = /^[a-zA-Z_\-0-9]+@[a-z]+.[a-z]+$/;
        //위 이메일 형식을 따라 하는지 검사
        if(!regEmailPattern.test(loginEmail.val())){
            alert('입력한 이메일 주소가 올바르지 않음');
            return false;
        }
        if(loginPw.val().length < 8){
            alert('비밀번호를 입력하지 않았거나 8글자 이하입니다');
            return false;
        }
    });

    /*회원가입 확인*/
    var signUpSubmit = $('#signUpSubmit'); //가입하기 버튼
    var userName = $('#userName'); //이름 입력 폼
    var studentID = $('#studentID'); //이메일 입력 폼
    var userPw = $('#userPw'); //비밀번호 입력 폼
    var userPwCheck = $('#userPwCheck'); //비밀번호 입력 폼
    var valueError = $('#valueError'); //필터링 시 값이 오류일 때 무엇이 오류인지 보여주는 박스

    signUpSubmit.click(function(){ //가입하기 버튼 클릭 이벤트
        /*이름이 공백인지 확인*/
        if(userName.val() == ''){
            valueError.text('이름을 입력하세요');// 알릴 오류 메시지 입력
            userName.focus(); //이름 입력란에 포커스
            timeOutCall(); //오류 메시지를 2초 후 사라지게 하는 함수를 호출
            return false;
        }
        /*공백이 아니면 유효한 값인지 확인*/
        var regNamePattern = /^[가-힣a-zA-Z]+$/;
        if(regNamePattern.test(userName.val())){
            console.log('the value of userName is good');
        }
        else{
            valueError.text('정확한 이름을 입력하세요');
            userName.focus();
            timeOutCall();
            return false;
        }
        /*학번 유효성 확인*/
        if(studentID.val().length >= 10){
            console.log('the value of password is good');
        }else{
            valueError.text('정확한 학번을 입력하세요');
            studentID.focus();
            timeOutCall;
            return false;
        }
        /*같은 학번 사용 확인*/
        
        /*비밀번호가 8자이상인지 확인*/
        if(userPw.val().length >= 8){
            console.log('the value of password is good');
        }else{
            valueError.text('비밀번호 8자 이상 입력');
            userPw.focus();
            timeOutCall;
            return false;
        }
        /*비밀번호 같은지 확인*/
        if(userPwCheck == userPW){
            console.log('value same with')
        }else{
            valueError.text('비밀번호 같지 않음');
            userPw.focus();
            timeOutCall;
            return false;
        }
        /*여기까지 return false에 만나지 않았다면 true를 만환해 회원가입 정보를 제출*/
        return true;
    });


});