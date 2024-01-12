const tabItem = document.querySelectorAll(".gallery__btn");
const tabContent = document.querySelectorAll(".gallery__items");

tabItem.forEach(function (element) {
  element.addEventListener("click", open);
});

function open(evt) {
  const tabTarget = evt.currentTarget;
  const button = tabTarget.dataset.button;

  tabItem.forEach(function (item) {
    item.classList.remove("gallery__btn--active");
  });

  tabTarget.classList.add("gallery__btn--active");

  tabContent.forEach(function (item) {
    item.classList.remove("gallery__items--active");
  });

  document.querySelector(`#${button}`).classList.add("gallery__items--active");
}

$(function () {
  $(".menu__btn").on("click", function () {
    $(".menu__list").toggleClass("menu__list--active");
  });

  $(".shop__filter-btn").on("click", function () {
    $(".shop__filters").slideToggle();
  });

  $(".blog-page__slider").slick({
    prevArrow:
      '<button type="button" class="slick-prev"><svg width="10" height="18" viewBox="0 0 10 18" fill="none" xmlns="http://www.w3.org/2000/svg">  <path fill-rule="evenodd" clip-rule="evenodd" d="M9.63388 0.616117C10.122 1.10427 10.122 1.89573 9.63388 2.38388L3.01777 9L9.63388 15.6161C10.122 16.1043 10.122 16.8957 9.63388 17.3839C9.14573 17.872 8.35427 17.872 7.86612 17.3839L0.366117 9.88388C-0.122039 9.39573 -0.122039 8.60427 0.366117 8.11612L7.86612 0.616117C8.35427 0.127961 9.14573 0.127961 9.63388 0.616117Z" fill="#828282"/>   </svg> </button>',
    nextArrow:
      '<button type="button" class="slick-next"><svg width="10" height="18" viewBox="0 0 10 18" fill="none" xmlns="http://www.w3.org/2000/svg">  <path fill-rule="evenodd" clip-rule="evenodd" d="M0.366117 0.616117C0.854272 0.127961 1.64573 0.127961 2.13388 0.616117L9.63388 8.11612C10.122 8.60427 10.122 9.39573 9.63388 9.88388L2.13388 17.3839C1.64573 17.872 0.854272 17.872 0.366117 17.3839C-0.122039 16.8957 -0.122039 16.1043 0.366117 15.6161L6.98223 9L0.366117 2.38388C-0.122039 1.89573 -0.122039 1.10427 0.366117 0.616117Z" fill="#828282"/>  </svg> </button>',
    infinite: false,
  });
  $(".product-tabs__top-item").on("click", function (e) {
    e.preventDefault();
    $(".product-tabs__top-item").removeClass("product-tabs__top-item--active");
    $(this).addClass("product-tabs__top-item");

    $(".product-tabs__content-item").removeClass(
      "product-tabs__content-item--active"
    );
    $($(this).attr("href")).addClass("product-tabs__content-item--active");
  });
  $(".product-slide__thumb").slick({
    asNavFor: ".product-slide__big",
    focusOnSelect: true,
    slidesToShow: 4,
    slidesToScroll: 1,
    vertical: true,
    draggable: false,
  });
  $(".product-slide__big").slick({
    asNavFor: ".product-slide__thumb",
    draggable: false,
    arrows: false,
    fade: true,
    responsive: [
      {
        breakpoint: 1051,
        settings: {
          draggable: true,
        },
      },
    ],
  });

  $(".shop-content__filter-btn").on("click", function () {
    $(".shop-content__filter-btn").removeClass(
      "shop-content__filter-btn--active"
    );
    $(this).addClass("shop-content__filter-btn--active");
  });

  $(".button-list").on("click", function () {
    $(".product-item").addClass("product-item--list");
    $(".shop-content__inner").addClass("shop-content__nogrid");
  });

  $(".button-grid").on("click", function () {
    $(".product-item").removeClass("product-item--list");
    $(".shop-content__inner").removeClass("shop-content__nogrid");
  });

  $(".select-style, .product-one__item-num").styler();

  $(".filter-price__input").ionRangeSlider({
    type: "double",
    prefix: "$",
    onStart: function (data) {
      $(".filter-price__from").text(data.from);
      $(".filter-price__to").text(data.to);
    },
    onChange: function (data) {
      $(".filter-price__from").text(data.from);
      $(".filter-price__to").text(data.to);
    },
  });

  $(".star").rateYo({
    starWidth: "17px",
    normalFill: "#ccccce",
    ratedFill: "#ffc35b",
  });
  var mixer = mixitup(".gallery__inner", {
    load: {
      filter: ".living",
    },
  });

});

$(".top-slider__inner").slick({
  dots: true,
  arrows: false,
  fade: true,
  autoplay: true,
});