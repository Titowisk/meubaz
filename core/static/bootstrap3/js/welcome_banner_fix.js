$('#menu').on('show.bs.collapse', function () {
    $('.banner-welcome').css('display', 'none')
})

$('#menu').on('hide.bs.collapse', function () {
    $('.banner-welcome').css('display', 'block')
})