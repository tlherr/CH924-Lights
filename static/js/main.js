(function($) {

    $('#light_enable').click(function(event) {
        $.ajax({
          url: '/admin',
          method: 'POST',
          data: {
              light_override: 1
          }
        });
    });

    $('#light_disable').click(function(event) {
        $.ajax({
          url: '/admin',
          method: 'POST',
          data: {
              light_override: 0
          }
        });
    });

}(jQuery));