$(document).ready(function() {
    /* handler for filtering tables in b_overview.html files */
    $('#search-input').on('keyup', function() {
        let value = $(this).val().toLowerCase();
        $('#overview-table tr').filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});