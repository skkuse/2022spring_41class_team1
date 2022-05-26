var inputeditor;
var outputeditor;
var erroreditor;

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


    inputeditor = CodeMirror.fromTextArea(document.getElementById("inputeditor"),{
        mode:"python", 
        theme:"dracula", 
        lineNumbers: true,
    });
    inputeditor.setSize("100%","100%");
    outputeditor = CodeMirror.fromTextArea(document.getElementById("outputeditor"),{
        mode:"python", 
        theme:"dracula", 
        lineNumbers: true,
        readOnly: true
    });
    outputeditor.setSize("100%","100%");
    erroreditor = CodeMirror.fromTextArea(document.getElementById("erroreditor"),{
        mode:"python", 
        theme:"dracula", 
        lineNumbers: true,
        // readOnly: true
    });
    erroreditor.setSize("100%","100%");

    $("#send_editor").submit(function(e){
        e.preventDefault();
        
        $.ajax({
            type: "POST",
            url:  "/judge",
            data: $(this).serialize(), // serializes the form's elements.
            async : false,
            success: function(data)
            {
                outputeditor.setValue(data.out);
                erroreditor.setValue(data.log);
                if(data.success)
                    alert("정답")
                else
                    alert("오답")
            }
        });
    })
    
});