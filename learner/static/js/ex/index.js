$(document).ready(function(){
    var signUpBtn = $('#signUpBtn');
    //회원가입폼
    signup = $('#signup');
    //로그인폼
    loginForm = $('#loginForm');
    //"온라인 머신러닝 클라스에 어서오세요" 문구
    introSite = $('#introSite');
    //[가입하기] 버튼 클릭 이벤트
    signUpBtn.click(function(){
      //로그인 폼 숨기기
      loginForm.slideUp();
      //회원가입 폼 보이기
      signup.slideDown();
      //"온라인 머신러닝 클라스에 어서오세요" 숨기기
      introSite.slideUp();
    });
    //로그인하기 버튼
    var goToLoginBtn = $('#goToLoginBtn');
    //로그인하기 버튼 클릭 이벤트
    goToLoginBtn.click(function(){
      //로그인 폼 보이기
      loginForm.slideDown();
      //회원가입 폼 숨기기
      signup.slideUp();
      //내가 만드는 첫 웹서비스 문구 보이기
      introSite.slideDown();
    })
    toGoToShort = false;
    $(window).resize(function(){
      if(window.innerWidth >= 1200){
        loginForm.slideDown();
        signup.slideDown();
        introSite.slideDown();
        toGoToShort = true;
      }else{
        if(toGoToShort == true){
          signup.slideUp();
        }
      }
    });
  })
  