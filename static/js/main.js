(function($) {

    $(document).ready(function() {
        var timeRemaning = $('#time_remaining');

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