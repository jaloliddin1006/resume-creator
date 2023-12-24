function postData() {
    const formData = new FormData($('#resumeForm')[0]);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });
       // CSRF tokenni ma'lumotlar bilan birga qo'shish
    //    data['csrfmiddlewaretoken'] = $('#csrfToken').val();

    console.log(data);

    $.ajax({
        type: 'POST',
        url: 'information/',
        contentType: 'application/json',
        headers: {
            'X-CSRFToken': $('#csrfToken').val() // CSRF tokenni qo'shing
        },
        data: JSON.stringify(data),
        success: function (result) {
            console.log(result);
            // 1-chi frame ni yoping
            // $('#frame1').hide();

            // // Olingan ma'lumotlarni 2-chi frame ga yuboring
            // const frame2 = $('#frame2')[0];
            // frame2.src = 'frame2.html'; // Frame 2 ni tozalash
            // $(frame2).show();
            // frame2.contentWindow.postMessage(result, '*');
        },
        error: function (xhr, status, error) {
            console.error('Xatolik yuz berdi:', xhr, error, status);
        }
    });
}