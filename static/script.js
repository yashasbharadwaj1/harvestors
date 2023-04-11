//information card slider
"use strict";

const initSwiper = () => {
  const mySwiper = new Swiper(".swiper-container", {
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    slidesPerView: 2.7,
    centeredSlides: true,
    breakpoints: {
      1440: {
        slidesPerView: 2.6
      },
      1439: {
        slidesPerView: 1.45
      },
      1024: {
        slidesPerView: 1.45
      },
      1023: {
        slidesPerView: 2
      },
      768: {
        slidesPerView: 2
      },
      568: {
        slidesPerView: 1.5,
        spaceBetween: 10
      },
      414: {
        slidesPerView: 1.09,
        spaceBetween: 3
      },
      320: {
        slidesPerView: 1.09,
        spaceBetween: 3
      }
    }
  });

  const $revealCardContentBtn = $(".sl--card-nav-container"),
    $contentContainer = $(".sl-card-wrapper .sl--content-wrapper .sl--content-container"),
    $navGFX = $(".sl-card-wrapper .sl--content-wrapper .sl--card-nav-container .sl--content-btn .card-nav-gfx");

  $revealCardContentBtn.on("click", () => {
    const $parent = $(this).closest(".swiper-slide");

    // IC Container
    $parent
      .siblings()
      .find($contentContainer)
      .removeClass("sl--card-reveal")
      .addClass("sl--card-hide");
    $parent.find($contentContainer).toggleClass("sl--card-hide sl--card-reveal");

    // IC Nav wrapper
    $parent
      .siblings()
      .find(".sl--content-wrapper")
      .removeClass("sl--content-wrapper-active")
      .addClass("sl--content-wrapper-inactive");
    $parent
      .find(".sl--content-wrapper")
      .toggleClass("sl--content-wrapper-inactive sl--content-wrapper-active");

    // IC Nav GFX
    $parent
      .siblings()
      .find($navGFX)
      .removeClass("sl--close-card-info")
      .addClass("sl--show-card-info");
    $parent.find($navGFX).toggleClass("sl--show-card-info sl--close-card-info");
  });

  mySwiper.on("slideChange", () => {
    if ($contentContainer.hasClass("sl--card-reveal")) {
      const $CI_ContentWrapper = $(".sl--content-wrapper");

      $contentContainer.removeClass("sl--card-reveal").addClass("sl--card-hide");
      $navGFX.removeClass("sl--close-card-info").addClass("sl--show-card-info");
      $CI_ContentWrapper.removeClass("sl--content-wrapper-active").addClass("sl--content-wrapper-inactive");
    }
  });
};

$(document).ready(() => {
  initSwiper();

  // Media Query
  const windowWidth = $(window).width();
  switch (windowWidth) {
    case 320:
      break;
    case 375:
      break;
    case 414:
      break;
    case 768:
      break;
    case 1024:
      break;
    default:
      break;
  }
});

$(document).ready(function() {
  "use strict";

  /* Swiper
	-------------------------------------------------------*/
  //initialize swiper when document ready
  var mySwiper = new Swiper(".swiper-container", {
    // Navigation arrows
    nextButton: ".swiper-button-next",
    prevButton: ".swiper-button-prev",
    slidesPerView: 2.7,
    centeredSlides: true,
    breakpoints: {
      1440: {
        slidesPerView: 2.6
      },
      1439: {
        slidesPerView: 1.45
      },
      1024: {
        slidesPerView: 1.45
      },
      1023: {
        slidesPerView: 2
      },
      768: {
        slidesPerView: 2
      },
      568: {
        slidesPerView: 1.5,
        spaceBetween: 10
      },
      414: {
        slidesPerView: 1.09,
        spaceBetween: 3
      },
      320: {
        slidesPerView: 1.09,
        spaceBetween: 3
      }
    }
  });

  /* Info Card
	-------------------------------------------------------*/
  var $revealCardContentBtn = $(".sl--card-nav-container"),
    $contentContainer = $(
      ".sl-card-wrapper .sl--content-wrapper .sl--content-container"
    ),
    $navGFX = $(
      ".sl-card-wrapper .sl--content-wrapper .sl--card-nav-container .sl--content-btn .card-nav-gfx"
    );

  $revealCardContentBtn.on("click", function() {
    var parent = $(this).closest(".swiper-slide");

    // IC Container
    parent
      .siblings()
      .find($contentContainer)
      .removeClass("sl--card-reveal");
    parent
      .siblings()
      .find($contentContainer)
      .addClass("sl--card-hide");
    parent.find($contentContainer).toggleClass("sl--card-hide sl--card-reveal");

    // IC Nav wrapper
    parent
      .siblings()
      .find(".sl--content-wrapper")
      .removeClass("sl--content-wrapper-active");
    parent
      .siblings()
      .find(".sl--content-wrapper")
      .addClass("sl--content-wrapper-inactive");
    parent
      .find(".sl--content-wrapper")
      .toggleClass("sl--content-wrapper-inactive sl--content-wrapper-active");

    // IC Nav GFX
    parent
      .siblings()
      .find($navGFX)
      .removeClass("sl--close-card-info");
    parent
      .siblings()
      .find($navGFX)
      .addClass("sl--show-card-info");
    parent.find($navGFX).toggleClass("sl--show-card-info sl--close-card-info");
  });

  /* Hide content on slide change
	-------------------------------------------------------*/
  mySwiper.on("onSlideChangeStart", function() {
    if ($contentContainer.hasClass("sl--card-reveal")) {
      var $CI_ContentWrapper = $(".sl--content-wrapper");

      $contentContainer.removeClass("sl--card-reveal");
      $contentContainer.addClass("sl--card-hide");
      $navGFX.removeClass("sl--close-card-info");
      $navGFX.addClass("sl--show-card-info");
      $CI_ContentWrapper.removeClass("sl--content-wrapper-active");
      $CI_ContentWrapper.addClass("sl--content-wrapper-inactive");
    }
  });

  // Media Query
  var windowWidth = $(window).width();
  if (windowWidth === 320) {
  }
  if (windowWidth === 375) {
  }
  if (windowWidth === 414) {
  }
  if (windowWidth === 768) {
  }
  if (windowWidth === 1024) {
  }
}); //END: $(document)











//blog slider

var swiper = new Swiper('.blog-slider', {
  spaceBetween: 30,
  effect: 'fade',
  loop: true,
  mousewheel: {
    invert: false,
  },
  // autoHeight: true,
  pagination: {
    el: '.blog-slider__pagination',
    clickable: true,
  }
});










//main slider

const slides = document.querySelectorAll('.slide');
const next = document.querySelector('#next');
const prev = document.querySelector('#prev');
const intervalTime = 5000;
let slideInterval;

const nextSlide = () => {
  const current = document.querySelector('.current');
  current.classList.remove('current');
  if (current.nextElementSibling) {
    current.nextElementSibling.classList.add('current');
  } else {
    slides[0].classList.add('current');
  }
  setTimeout(() => current.classList.remove('current'));
};

const prevSlide = () => {
  const current = document.querySelector('.current');
  current.classList.remove('current');
  if (current.previousElementSibling) {
    current.previousElementSibling.classList.add('current');
  } else {
    slides[slides.length - 1].classList.add('current');
  }
  setTimeout(() => current.classList.remove('current'));
};

next.addEventListener('click', e => {
  nextSlide();
});

prev.addEventListener('click', e => {
  prevSlide();
});























$(document).ready(function() {
  $(".slider-youtube iframe").each(function (idx) {
    $(this).addClass("data-idx-" + idx).data("idx", idx);
  });

  function getPlayer (iframe, onPlayerReady, clonned) {
      var $iframe = $(iframe);
      if ($iframe.data((clonned ? "clonned-" : "") + "player")) {
        var isReady = $iframe.data((clonned ? "clonned-" : "") + "player-ready");
        if (isReady) {
          onPlayerReady && onPlayerReady($iframe.data((clonned ? "clonned-" : "") + "player"));
        }
        return player;
      }
      else {
        var player = new YT.Player($iframe.get(0), {
          events: {
            'onReady': function () {
              $iframe.data((clonned ? "clonned-" : "") + "player-ready", true);
              onPlayerReady && onPlayerReady(player);
            }
          }
        });
        $iframe.data((clonned ? "clonned-" : "") + "player", player);
        return player;
      }
  }

  //on first load, play the video
  $(".slider-youtube").on('init', function(event, slick, currentSlide) {
      var currentSlide, player, command;
      currentSlide = $(slick.$slider).find(".slick-current");
      getPlayer(currentSlide.find("iframe"), function (player) {
        player.playVideo();
      });
  });

  //when new slide displays, play the video
  $(".slider-youtube").on("afterChange", function(event, slick) {
      var currentSlide;
      currentSlide = $(slick.$slider).find(".slick-current");
      getPlayer(currentSlide.find("iframe"), function (player) {
        player.playVideo();
      });
  });

  function updateClonnedFrames () {
    frames = $(".slider-youtube").find(".slick-slide").not(".slick-cloned").find("iframe");
    frames.each(function () {
      var frame = $(this);
      var idx = frame.data("idx");
      clonedFrames = $(".slider-youtube").find(".slick-cloned .data-idx-" + idx);
      console.log("clonedFrames", frame, idx, clonedFrames);
      clonedFrames.each(function () {
        var clonnedFrame = this;
        getPlayer(frame[0], function (player) {
          getPlayer(clonnedFrame, function (clonedPlayer) {
            console.log("clonnedPlayer", clonedPlayer);
            clonedPlayer.playVideo();
            clonedPlayer.seekTo(player.getCurrentTime(), true);
            setTimeout(function () {
              clonedPlayer.pauseVideo();
            }, 0);
          }, true);
        });
      });
    });
  }

  //reset iframe of non current slide
  $(".slider-youtube").on('beforeChange', function(event, slick, currentSlide) {
      var currentSlide, iframe, clonedFrame;
      currentSlide = $(slick.$slider).find(".slick-current");
      iframe = currentSlide.find("iframe");
      getPlayer(iframe, function (player) {
        player.pauseVideo();
        updateClonnedFrames();
      });
  });

  //start the slider
  $('.slider-youtube').slick({
      slidesToShow: 1,
      arrows: false,
      centerMode: true,
      centerPadding: '50px',
      infinite: true,
      variableWidth: true
  });
});



















$('.owl-carousel').owlCarousel({
  stagePadding: 200,
  loop:true,
  margin:10,
  items:1,
  nav:true,
responsive:{
      0:{
          items:1,
          stagePadding: 60
      },
      600:{
          items:1,
          stagePadding: 100
      },
      1000:{
          items:1,
          stagePadding: 200
      },
      1200:{
          items:1,
          stagePadding: 250
      },
      1400:{
          items:1,
          stagePadding: 300
      },
      1600:{
          items:1,
          stagePadding: 350
      },
      1800:{
          items:1,
          stagePadding: 400
      }
  }
})

var playerSettings = {
    controls : ['play-large'],
    fullscreen : { enabled: false},
    resetOnEnd : true,
    hideControls  :true,
clickToPlay:true,
    keyboard : false,
  }

const players = Plyr.setup('.js-player', playerSettings);

players.forEach(function(instance,index) {
          instance.on('play',function(){
              players.forEach(function(instance1,index1){
                if(instance != instance1){
                      instance1.pause();
                  }
              });
          });
      });

$('.video-section').on('translated.owl.carousel', function (event) {
players.forEach(function(instance,index1){
                instance.pause();
              });
});
























































function myFunction() {
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("myBtn");

    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "Read more";
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "Read less";
      moreText.style.display = "inline";
    }
  }
  function myFunction1() {
    var dots = document.getElementById("dots1");
    var moreText = document.getElementById("more1");
    var btnText = document.getElementById("myBtn1");

    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "Read more";
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "Read less";
      moreText.style.display = "inline";
    }
  }
  function myFunction2() {
    var dots = document.getElementById("dots2");
    var moreText = document.getElementById("more2");
    var btnText = document.getElementById("myBtn2");

    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "Read more";
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "Read less";
      moreText.style.display = "inline";
    }
  }
  function myFunction3() {
    var dots = document.getElementById("dots3");
    var moreText = document.getElementById("more3");
    var btnText = document.getElementById("myBtn3");

    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "Read more";
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "Read less";
      moreText.style.display = "inline";
    }
  }
  function myFunction4() {
    var dots = document.getElementById("dots4");
    var moreText = document.getElementById("more4");
    var btnText = document.getElementById("myBtn4");

    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "Read more";
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "Read less";
      moreText.style.display = "inline";
    }
  }
  function myFunction5() {
    var dots = document.getElementById("dots5");
    var moreText = document.getElementById("more5");
    var btnText = document.getElementById("myBtn5");

    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "Read more";
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "Read less";
      moreText.style.display = "inline";
    }
  }
  function myFunction6() {
    var dots = document.getElementById("dots6");
    var moreText = document.getElementById("more6");
    var btnText = document.getElementById("myBtn6");

    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "Read more";
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "Read less";
      moreText.style.display = "inline";
    }
  }













  (() => {
    const tabs = document.querySelectorAll(".tab");
    const contents = document.querySelectorAll(".tab-content");
    const tabsWrap = document.querySelector(".tabs-titles-wrap");
    const activeClass = "active";
  //обрабатываем клик по родителю с табами
    tabsWrap.addEventListener("click", e => {
      //если произошел клик по элементу с классом tab
      if (e.target.classList.contains("tab")) {
        //идем циклом по всем tab
        [...tabs].forEach((tab, tabIndex, tabArray) => {
          //у всех tab и tab-content удаляем класс active
          tab.classList.remove(activeClass);
          contents[tabIndex].classList.remove(activeClass);
          //если кликнули по tab
          if (e.target === tab) {
            //добавляем этому элементу(tab) класс active
            tab.classList.add(activeClass);
            //добавляем соотв-щему tab-content класс active
            contents[tabIndex].classList.add(activeClass);
          }
        });
      }
    });
  })();





  const sliderContainer = document.querySelector(".slider-container");
const prevButton = document.querySelector(".slider-prev");
const nextButton = document.querySelector(".slider-next");

let slideIndex = 0;

prevButton.addEventListener("click", () => {
  if (slideIndex === 0) {
    slideIndex = 2;
  } else {
    slideIndex--;
  }
  sliderContainer.style.transform = `translateX(-${slideIndex * 33.33}%)`;
});

nextButton.addEventListener("click", () => {
  if (slideIndex === 2) {
    slideIndex = 0;
  } else {
    slideIndex++;
  }
  sliderContainer.style.transform = `translateX(-${slideIndex * 33.33}%)`;
});