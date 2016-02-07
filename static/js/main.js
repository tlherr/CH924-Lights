(function($) {

    $('#light_enable').click(function(event) {
        $.ajax({
          statusCode: {
            url: '/',
            method: 'POST',
            data: {
                light_override: true
            }
          }
        });
    });

    $('#light_disable').click(function(event) {
        $.ajax({
          statusCode: {
            url: '/',
            method: 'POST',
            data: {
                light_override: false
            }
          }
        });
    });

}(jQuery));