(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.tabs').tabs();
    $('.collapsible').collapsible();
    $(".owl-carousel").owlCarousel({
      rtl:true,
      loop:true,
      margin:10,
      nav:true,
      responsive:{
          0:{
              items:1
          },
          600:{
              items:3
          },
          1000:{
              items:5
          }
      }
    });
      $('.tooltipped').tooltip();
      $('.modal').modal();
      

  }); // end of document ready
})(jQuery); // end of jQuery name space
