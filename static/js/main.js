(function($) {

    $('#light_enable').click(function(event) {
        $.ajax({
          url: '/admin',
          method: 'POST',
          data: {
              light_override: true
          }
        });
    });

    $('#light_disable').click(function(event) {
        $.ajax({
          url: '/admin',
          method: 'POST',
          data: {
              light_override: false
          }
        });
    });

}(jQuery));