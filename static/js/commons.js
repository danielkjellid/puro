$(document).ready(function() {

    let toggle = (el) => {
        if (el.hasClass('hidden')) {
            el.removeClass('hidden');
            el.addClass('block');
        } else {
            el.removeClass('block');
            el.addClass('hidden');
        }
    }

    /* handler for filtering tables in b_overview.html files */
    $('#search-input').on('keyup', function() {
        let value = $(this).val().toLowerCase();
        $('#overview-table tr').filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    $('#user-menu-btn').click(function(e) {
        $('.toggle-user-menu').show();
        e.stopPropagation();
    });
    
    $('.note-menu-btn').click(function(e) {
        $(e.target).closest('.note-menu').find('.toggle-note-menu').show();
        e.stopPropagation();
    });

    $(document).click(function() {
        $('.toggle-user-menu').hide();
        $('.toggle-note-menu').hide();
    });
});