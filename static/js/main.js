(function($) {

    $(document).ready(function() {
        var timeRemaning = $('#time_remaining');
        refreshInfo();

        refreshInfo = function() {
            $.getJSON( "api", function( data ) {
                $.each( data, function( key, val ) {
                    $('span#'+key).text(val);
                 });
            }

            setTimeout(refreshInfo, 5000);
        }

        $('#light_enable').click(function(event) {
            $.ajax({
              url: '/api',
              method: 'POST',
              data: {
                  light_override: 1
              }
            });
        });

        $('#light_disable').click(function(event) {
            $.ajax({
              url: '/api',
              method: 'POST',
              data: {
                  light_override: 0
              }
            });
        });
    });

}(jQuery));