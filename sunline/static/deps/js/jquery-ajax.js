// Когда html документ готов (прорисован)
$(document).ready(function () {
  // берем в переменную элемент разметки с id jq-notification для оповещений от ajax
  var successMessage = $("#jq-notification");

  // Ловим собыитие клика по кнопке добавить в корзину
  $(document).on("click", ".add-to-cart", function (e) {
    // Блокируем его базовое действие
    e.preventDefault();

    // Берем элемент счетчика в значке корзины и берем оттуда значение
    var goodsInCartCount = $("#goods-in-cart-count");
    var cartCount = parseInt(goodsInCartCount.text() || 0);

    // Получаем id товара из атрибута data-product-id
    var product_id = $(this).data("product-id");

    // Из атрибута href берем ссылку на контроллер django
    var add_to_cart_url = $(this).attr("href");

    // делаем post запрос через ajax не перезагружая страницу
    $.ajax({
      type: "POST",
      url: add_to_cart_url,
      data: {
        product_id: product_id,
        csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
      },
      success: function (data) {
        // Сообщение
        successMessage.html(data.message);
        successMessage.fadeIn(400);
        // Через 7сек убираем сообщение
        setTimeout(function () {
          successMessage.fadeOut(400);
        }, 7000);

        // Увеличиваем количество товаров в корзине (отрисовка в шаблоне)
        cartCount++;
        goodsInCartCount.text(cartCount);

        // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
        var cartItemsContainer = $("#cart-items-container");
        cartItemsContainer.html(data.cart_items_html);
      },

      error: function (data) {
        console.log("Ошибка при добавлении товара в корзину");
      },
    });
  });

  // Ловим собыитие клика по кнопке удалить товар из корзины
  $(document).on("click", ".remove-from-cart", function (e) {
    // Блокируем его базовое действие
    e.preventDefault();

    // Берем элемент счетчика в значке корзины и берем оттуда значение
    var goodsInCartCount = $("#goods-in-cart-count");
    var cartCount = parseInt(goodsInCartCount.text() || 0);

    // Получаем id корзины из атрибута data-cart-id
    var cart_id = $(this).data("cart-id");
    // Из атрибута href берем ссылку на контроллер django
    var remove_from_cart = $(this).attr("href");

    // делаем post запрос через ajax не перезагружая страницу
    $.ajax({
      type: "POST",
      url: remove_from_cart,
      data: {
        cart_id: cart_id,
        csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
      },
      success: function (data) {
        // Сообщение
        successMessage.html(data.message);
        successMessage.fadeIn(400);
        // Через 7сек убираем сообщение
        setTimeout(function () {
          successMessage.fadeOut(400);
        }, 7000);

        // Уменьшаем количество товаров в корзине (отрисовка)
        cartCount -= data.quantity_deleted;
        goodsInCartCount.text(cartCount);

        // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
        var cartItemsContainer = $("#cart-items-container");
        cartItemsContainer.html(data.cart_items_html);
      },

      error: function (data) {
        console.log("Ошибка при добавлении товара в корзину");
      },
    });
  });

  // Теперь + - количества товара
  // Обработчик события для уменьшения значения
  $(document).on("click", ".decrement", function () {
    // Берем ссылку на контроллер django из атрибута data-cart-change-url
    var url = $(this).data("cart-change-url");
    // Берем id корзины из атрибута data-cart-id
    var cartID = $(this).data("cart-id");
    // Ищем ближайшеий input с количеством
    var $input = $(this).closest(".input-group").find(".number");
    // Берем значение количества товара
    var currentValue = parseInt($input.val());
    // Если количества больше одного, то только тогда делаем -1
    if (currentValue > 1) {
      $input.val(currentValue - 1);
      // Запускаем функцию определенную ниже
      // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
      updateCart(cartID, currentValue - 1, -1, url);
    }
  });

  // Обработчик события для увеличения значения
  $(document).on("click", ".increment", function () {
    // Берем ссылку на контроллер django из атрибута data-cart-change-url
    var url = $(this).data("cart-change-url");
    // Берем id корзины из атрибута data-cart-id
    var cartID = $(this).data("cart-id");
    // Ищем ближайшеий input с количеством
    var $input = $(this).closest(".input-group").find(".number");
    // Берем значение количества товара
    var currentValue = parseInt($input.val());

    $input.val(currentValue + 1);

    // Запускаем функцию определенную ниже
    // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
    updateCart(cartID, currentValue + 1, 1, url);
  });

  function updateCart(cartID, quantity, change, url) {
    $.ajax({
      type: "POST",
      url: url,
      data: {
        cart_id: cartID,
        quantity: quantity,
        csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
      },

      success: function (data) {
        // Сообщение
        successMessage.html(data.message);
        successMessage.fadeIn(400);
        // Через 7сек убираем сообщение
        setTimeout(function () {
          successMessage.fadeOut(400);
        }, 7000);

        // Изменяем количество товаров в корзине
        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);
        cartCount += change;
        goodsInCartCount.text(cartCount);

        // Меняем содержимое корзины
        var cartItemsContainer = $("#cart-items-container");
        cartItemsContainer.html(data.cart_items_html);
      },
      error: function (data) {
        console.log("Ошибка при добавлении товара в корзину");
      },
    });
  }

  // Берем из разметки элемент по id - оповещения от django
  var notification = $("#notification");
  // И через 7 сек. убираем
  if (notification.length > 0) {
    setTimeout(function () {
      notification.alert("close");
    }, 7000);
  }

  // При клике по значку корзины открываем всплывающее(модальное) окно
  $("#modalButton").click(function () {
    $("#exampleModal").appendTo("body");

    $("#exampleModal").modal("show");
  });

  // Собыите клик по кнопке закрыть окна корзины
  $("#exampleModal .btn-close").click(function () {
    $("#exampleModal").modal("hide");
  });

  // Обработчик события радиокнопки выбора способа доставки
  $("input[name='requires_delivery']").change(function () {
    var selectedValue = $(this).val();
    // Скрываем или отображаем input ввода адреса доставки
    if (selectedValue === "1") {
      $("#deliveryAddressField").show();
    } else {
      $("#deliveryAddressField").hide();
    }
  });

  // ====================adding review=====================

  const monthNames = [
    "Jan",
    "Feb",
    "Mar",
    "April",
    "May",
    "June",
    "July",
    "Aug",
    "Sept",
    "Oct",
    "Now",
    "Dec",
  ];

  $("#commentForm").submit(function (e) {
    e.preventDefault();

    let dt = new Date();
    let time =
      dt.getDay() +
      " " +
      monthNames[dt.getUTCMonth()] +
      ", " +
      dt.getFullYear();

    $.ajax({
      data: $(this).serialize(),

      method: $(this).attr("method"),

      url: $(this).attr("action"),

      dataType: "json",

      success: function (res) {
        console.log("Comment saved to DB...");
        if (res.bool == true) {
          $("#review-res").html("Review Added Successfully");
          $(".hide-comment-form").hide();
          $(".add-review").hide();

          let _html =
            '<div class="single-comment justify-content-between d-flex mb-30">';
          _html += '<div class="user justify-content-between d-flex">';
          _html += '<div class="thumb text-center">';
          _html += '<img src="assets/imgs/blog/author-2.png" alt="" />';
          _html +=
            '<a href="#" class="font-heading text-brand"> ' +
            res.context.user +
            " </a>";
          _html += "</div>";

          _html += '<div class="desc">';
          _html += '<div class="d-flex justify-content-between mb-10">';
          _html += '<div class="d-flex align-items-center">';
          _html += '<span class="font-xs text-muted"> ' + time + " </span>";
          _html += "</div>";

          for (var i = 1; i < res.context.rating; i++) {
            _html += '<i class="fas fa-star text-warning"> </i>';
          }
          _html += "</div>";
          _html += '<p class="mb-10"> ' + res.context.review + " </p>";
          _html += "</div>";
          _html += "</div>";
          _html += "</div>";

          $(".comment-list").prepend(_html);
        }
      },
    });
  });



  // =============adding wishlist=============

  // берем в переменную элемент разметки с id jq-notification для оповещений от ajax
  var successMessage = $("#jq-notification");

  // Ловим собыитие клика по кнопке добавить в корзину
  $(document).on("click", ".add-to-wishlist", function (e) {
    // Блокируем его базовое действие
    e.preventDefault();

    // Берем элемент счетчика в значке корзины и берем оттуда значение
    var goodsInWishlistCount = $("#goods-in-wishlist-count");
    var wishlistCount = parseInt(goodsInWishlistCount.text() || 0);

    // Получаем id товара из атрибута data-product-id
    var product_id = $(this).data("product-id");

    // Из атрибута href берем ссылку на контроллер django
    var add_to_wishlist_url = $(this).attr("href");

    // делаем post запрос через ajax не перезагружая страницу
    $.ajax({
      type: "POST",
      url: add_to_wishlist_url,
      data: {
        product_id: product_id,
        csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
      },
      success: function (data) {
        // Сообщение
        successMessage.html(data.message);
        successMessage.fadeIn(400);
        // Через 7сек убираем сообщение
        setTimeout(function () {
          successMessage.fadeOut(400);
        }, 7000);

        // Увеличиваем количество товаров в корзине (отрисовка в шаблоне)
        wishlistCount++;
        goodsInWishlistCount.text(wishlistCount);

        // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
        var wishlistItemsContainer = $("#wishlist-items-container");
        wishlistItemsContainer.html(data.wishlist_items_html);
      },

      error: function (data) {
        console.log("Ошибка при добавлении товара в корзину");
      },
    });
  });

  // Ловим собыитие клика по кнопке удалить товар из корзины
  $(document).on("click", ".remove-from-wishlist", function (e) {
    // Блокируем его базовое действие
    e.preventDefault();

    // Берем элемент счетчика в значке корзины и берем оттуда значение
    var goodsInWishlistCount = $("#goods-in-wishlist-count");
    var wishlistCount = parseInt(goodsInWishlistCount.text() || 0);

    // Получаем id корзины из атрибута data-cart-id
    var wishlist_id = $(this).data("wishlist-id");
    // Из атрибута href берем ссылку на контроллер django
    var remove_from_wishlist = $(this).attr("href");

    // делаем post запрос через ajax не перезагружая страницу
    $.ajax({
      type: "POST",
      url: remove_from_wishlist,
      data: {
        wishlist_id: wishlist_id,
        csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
      },
      success: function (data) {
        // Сообщение
        successMessage.html(data.message);
        successMessage.fadeIn(400);
        // Через 7сек убираем сообщение
        setTimeout(function () {
          successMessage.fadeOut(400);
        }, 7000);

        // Уменьшаем количество товаров в корзине (отрисовка)
        wishlistCount -= data.quantity_deleted;
        goodsInWishlistCount.text(wishlistCount);

        // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
        var wishlistItemsContainer = $("#wishlist-items-container");
        wishlistItemsContainer.html(data.wishlist_items_html);
      },

      error: function (data) {
        console.log("Ошибка при добавлении товара в корзину");
      },
    });
  });

  // Теперь + - количества товара
  // Обработчик события для уменьшения значения
  $(document).on("click", ".decrement", function () {
    // Берем ссылку на контроллер django из атрибута data-cart-change-url
    var url = $(this).data("wishlist-change-url");
    // Берем id корзины из атрибута data-cart-id
    var wishlistID = $(this).data("wishlist-id");
    // Ищем ближайшеий input с количеством
    var $input = $(this).closest(".input-group").find(".number");
    // Берем значение количества товара
    var currentValue = parseInt($input.val());
    // Если количества больше одного, то только тогда делаем -1
    if (currentValue > 1) {
      $input.val(currentValue - 1);
      // Запускаем функцию определенную ниже
      // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
      updateWishlist(wishlistID, currentValue - 1, -1, url);
    }
  });

  // Обработчик события для увеличения значения
  $(document).on("click", ".increment", function () {
    // Берем ссылку на контроллер django из атрибута data-cart-change-url
    var url = $(this).data("wishlist-change-url");
    // Берем id корзины из атрибута data-cart-id
    var wishlistID = $(this).data("wishlist-id");
    // Ищем ближайшеий input с количеством
    var $input = $(this).closest(".input-group").find(".number");
    // Берем значение количества товара
    var currentValue = parseInt($input.val());

    $input.val(currentValue + 1);

    // Запускаем функцию определенную ниже
    // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
    updateWishlist(wishlistID, currentValue + 1, 1, url);
  });

  function updateWishlist(wishlistID, quantity, change, url) {
    $.ajax({
      type: "POST",
      url: url,
      data: {
        wishlist_id: wishlistID,
        quantity: quantity,
        csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
      },

      success: function (data) {
        // Сообщение
        successMessage.html(data.message);
        successMessage.fadeIn(400);
        // Через 7сек убираем сообщение
        setTimeout(function () {
          successMessage.fadeOut(400);
        }, 7000);

        // Изменяем количество товаров в корзине
        var goodsInWishlistCount = $("#goods-in-wishlist-count");
        var wishlistCount = parseInt(goodsInWishlistCount.text() || 0);
        wishlistCount += change;
        goodsInWishlistCount.text(wishlistCount);

        // Меняем содержимое корзины
        var wishlistItemsContainer = $("#wishlist-items-container");
        wishlistItemsContainer.html(data.wishlist_items_html);
      },
      error: function (data) {
        console.log("Ошибка при добавлении товара в корзину");
      },
    });
  }

  // Берем из разметки элемент по id - оповещения от django
  var notification = $("#notification");
  // И через 7 сек. убираем
  if (notification.length > 0) {
    setTimeout(function () {
      notification.alert("close");
    }, 7000);
  }
});