var emailCheck = false;

$(document).ready(function(){
    //로그인 버튼
    var loginSubmit = $('#loginSubmit');
    //이메일 주소 입력 폼
    var loginEmail = $('#loginEmail');
    //로그인 폼의 비밀번호 입력 폼
    var loginPw = $('#loginPw');
    //로그인 버튼 클릭 이벤트
    loginSubmit.click(function(){
      //이메일 유효성 검사
      var regEmailPattern = /^[a-zA-Z_\-0-9]+@[a-z]+.[a-z]+$/;
      //아래 if문의 조건문은 위의 정규식을 이메일 주소가 따르는지 아닌지를 판별합니다.
      if(!regEmailPattern.test(loginEmail.val())){
        alert('입력한 이메일 주소가 올바르지 않습니다. ');
        return false;
      }
      if(loginPw.val().length < 8){
        alert('비밀번호를 입력하지 않았거나 8글자 이하입니다. ');
        return false;
      }
    });
    function timeOutCall(){
      //setTimoeout 함수는 어떠한 기능의 시간을
      //지연시킬 때 사용하는 내장 함수
      setTimeout(function(){
        $('#valueError').text('');
      },2000)
    }


    //중복체크 함수
    var duplication_check = function(){
      var userEmail = $('#userEmail');
      var valueError = $('#valueError');
      var checkIDText = $('#checkIDText');

      //이메일 유효성 확인
      var regEmailPattern = /^[a-zA-Z_\-0-9]+@[a-z]+.[a-z]+$/;
      if(regEmailPattern.test(userEmail.val())){
        console.log('exp email good');
      }else{
        valueError.text('정확한 이메일 주소를 입력하세요.');
        userEmail.focus();
        timeOutCall();
        return false;
      }
      //이메일 중복 확인
      $.ajax({
        type : 'post', //post 전송방식으로 전달
        dataType : 'json', //json 언어로 전달
        url : '/duplication_check', //이 주소에 데이터 전달
        data : {mode:'emailCheck', userEmail:userEmail.val()}, //전달할 데이터
        async : false, //값을 전달 받은 후 실행,
  
        success : function (data){
          //리턴된 정보를 콘솔로그로 확인
          console.log(data.result);
          if(data.result == true){
            //사용해도 좋은 이메일 주소인 경우a
            emailCheck = true;
            valueError.css('color','blue')
            valueError.text('사용 가능한 이메일 주소입니다.');
            userEmail.focus();
            timeOutCall();
            checkIDText.text('중복확인완료')
            
          }else{
            //이미 존재하는 이메일 주소인 경우
            emailCheck =false;
            valueError.css('color','red')
            valueError.text('이미 존재하는 이메일 주소입니다.');
            userEmail.focus();
            timeOutCall();
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
    $("#checkID").click(duplication_check);


    //회원가입 입력 정보 필터링
    //[회원가입] 버튼
    var signUpSubmit = $('#signUpSubmit');
    //이름 입력 폼
    var userName = $('#userName');
    //이메일 입력 폼
    var userEmail = $('#userEmail');
    //비밀번호 입력 폼
    var userPw = $('#userPw');
    //필터링 시 값이 오류일 때 무엇이 오류인지 보여주는 박스
    var valueError = $('#valueError');
    //[회원가입] 버튼 클릭 이벤트
    signUpSubmit.click(function(){
      //이름이 공백인지 확인
      if(userName.val() == ''){
        //알림 오류 메시지 입력
        valueError.text('이름을 입력하세요.');
        //이름 입력란에 포커스
        userName.focus();
        //오류 메시지를 2초 후 사라지게 하는 함수를 호출
        timeOutCall();
        return false;
      }
      //값이 공백이 아니면 해당 값이 유효한 값인지 확인
      //아래의 식은 PHP 학습 시 학습하므로 그냥 따라해 주세요.
      //입력한 값이 한글이거나 알파벳이라는 것을 확인하는 식입니다.
      var regNamePattern = /^[가-힣a-zA-Z]+$/;
      if(regNamePattern.test(userName.val())){
        //크롬 웹브라우저의 콘솔에서 확인하기 위함
        console.log('the value of userName is good');
      }else{
        valueError.text('정확한 이름을 입력하세요.');
        userName.focus();
        timeOutCall();
        return false;
      }
      if(emailCheck == false){
        valueError.text('이메일 중복체크를 해주세요.')
        return false;
      }
      //비밀번호 길이 8자 이상인지 확인
      if(userPw.val().length >= 8){
        console.log('the value of password is good');
      }else{
        valueError.text('비밀번호를 8자 이상 입력하세요.');
        userPw.focus();
        timeOutCall();
        return false;
      }
      //비밀번호 그리고 비밀번호 확인 같은지 확인
      if(userPw.val() == userPwCheck.val()){
        console.log('password and password check has same value');
      }else{
        valueError.text('비밀번호가 일치하지 않습니다');
        userPw.focus();
        timeOutCall();
        return false;
      }
      //여기까지 return false에 만나지 않았다면 true를 반환해 회원가입 정보를 제출
      return true;
  
    });
  
  });
  