$(document).ready(function() {
    // Initialize textillate.js
    $('.text').textillate({
     loop: true,
     sync: true,
     in: {
         effect: 'bounceIn',
     },
      out: {
         effect: 'bounceOut',
     },
    });
});
